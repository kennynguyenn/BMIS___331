import json
import math
import os
import re
from typing import Dict, List
import urllib

from loguru import logger as log
from scrapfly import ScrapeApiResponse, ScrapeConfig, ScrapflyClient, ScrapflyScrapeError

SCRAPFLY = ScrapflyClient(key=os.environ["SCRAPFLY_KEY"])
BASE_CONFIG = {
    "asp": True,
    "country": "US",
}


def parse_search_page(result):
    data = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', result.content)
    data = json.loads(data[0])
    return {
        "results": data["metaData"]["mosaicProviderJobCardsModel"]["results"],
        "meta": data["metaData"]["mosaicProviderJobCardsModel"]["tierSummaries"],
    }


def _add_url_parameter(url, **kwargs):
    url_parts = list(urllib.parse.urlparse(url))
    query = dict(urllib.parse.parse_qsl(url_parts[4]))
    query.update(kwargs)
    url_parts[4] = urllib.parse.urlencode(query)
    return urllib.parse.urlunparse(url_parts)


async def scrape_search(url: str, max_results: int = 1000) -> List[Dict]:
    log.info(f"scraping search: {url}")
    result_first_page = await SCRAPFLY.async_scrape(ScrapeConfig(url, **BASE_CONFIG))
    data_first_page = parse_search_page(result_first_page)

    results = data_first_page["results"]
    total_results = sum(category["jobCount"] for category in data_first_page["meta"])
    if total_results > max_results:
        total_results = max_results

    print(f"scraping remaining {(total_results - 10) / 10} pages")
    other_pages = [
        ScrapeConfig(_add_url_parameter(url, start=offset), **BASE_CONFIG)
        for offset in range(10, total_results + 10, 10)
    ]
    log.info("found total pages {} search pages", math.ceil(total_results / 10))
    async for result in SCRAPFLY.concurrent_scrape(other_pages):
        if not isinstance(result, ScrapflyScrapeError):
            data = parse_search_page(result)
            results.extend(data["results"])
        else:
            log.error(f"failed to scrape {result.api_response.config['url']}, got: {result.message}")
    return results


def parse_job_page(result: ScrapeApiResponse):
    data = re.findall(r"_initialData=(\{.+?\});", result.content)
    data = json.loads(data[0])
    data = data["jobInfoWrapperModel"]["jobInfoModel"]
    return {
        "description": data['sanitizedJobDescription'],
        **data["jobMetadataHeaderModel"],
        **(data["jobTagModel"] or {}),
        **data["jobInfoHeaderModel"],
    }


async def scrape_jobs(job_keys: List[str]):
    log.info(f"scraping {len(job_keys)} job listings")
    results = []
    urls = [
        f"https://www.indeed.com/viewjob?jk={job_key}" 
        for job_key in job_keys
    ]
    to_scrape = [ScrapeConfig(url, **BASE_CONFIG) for url in urls]
    async for result in SCRAPFLY.concurrent_scrape(to_scrape):
        results.append(parse_job_page(result))
    return results

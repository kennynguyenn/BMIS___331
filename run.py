import asyncio
import csv
import json
from pathlib import Path
import indeed

output = Path(__file__).parent / "results"
output.mkdir(exist_ok=True)


async def run():
    
    indeed.BASE_CONFIG["cache"] = True

    print("running Indeed scrape and saving results to ./results directory")
# Change the job field and location if needed
    
    """url = "https://www.indeed.com/jobs?q=python&l=Seattle"
    result_search = await indeed.scrape_search(url, max_results=100)
    output.joinpath("search.json").write_text(json.dumps(result_search, indent=2, ensure_ascii=False))"""



    job_keys = []
    with open('allkey.csv', newline='') as csvfile:
        total_lines = sum(1 for line in csvfile)
        csvfile.seek(0)
        
        reader = csv.reader(csvfile)
        # It cannot go more than 100 per run, limit it here
        lines_to_skip = 100
        for _ in range(total_lines - lines_to_skip):
            next(reader)
        
        for row in reader:
            job_keys.append(row[0])

    
    result_jobs = await indeed.scrape_jobs(job_keys)
    output.joinpath("jobs.json").write_text(json.dumps(result_jobs, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(run())

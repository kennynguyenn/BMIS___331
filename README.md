# Indeed.com Scraper

This scraper is using [scrapfly.io](https://scrapfly.io/) and Python to scrape job listing data from Indeed.com. 

Full tutorial <https://scrapfly.io/blog/how-to-scrape-indeedcom/>

The scraping code is located in the `indeed.py` file. It's fully documented and simplified for educational purposes and the example scraper run code can be found in `run.py` file.

This scraper scrapes:
- Indeed job search for finding job listings
- Indeed job pages for job listing datasets

For output, see the `./results` directory.


## Setup and Use

This Indeed.com scraper uses __Python 3.10__ with [scrapfly-sdk](https://pypi.org/project/scrapfly-sdk/) package which is used to scrape and parse Indeed's data.

0. Ensure you have __Python 3.10__ and [poetry Python package manager](https://python-poetry.org/docs/#installation) on your system.
1. Retrieve your Scrapfly API key from <https://scrapfly.io/dashboard> and set `SCRAPFLY_KEY` environment variable:
    ```shell
    $ export SCRAPFLY_KEY="YOUR SCRAPFLY KEY"
    ```
2. Clone and install Python environment:
    ```shell
    $ git clone https://github.com/scrapfly/scrapfly-scrapers.git
    $ cd scrapfly-scrapers/indeed-scraper
    $ poetry install
    ```
3. Run example scrape:
    ```shell
    $ poetry run python run.py
    ```
4. Run tests:
    ```shell
    $ poetry install --with dev
    $ poetry run pytest test.py
    # or specific scraping areas


## Comparison
0. set up Tika in the tika files and run the server
1. change the path in the extracttika.py to the path to your resume
2. run the compare.py located in tika


FOR MORE INFORMATION ON HOW TO USE, VISIT THIS LINK: https://drive.google.com/file/d/1uEhYi4Y9Lpx7xAvH8iEPTa-04j9JJAJJ/view?usp=sharing


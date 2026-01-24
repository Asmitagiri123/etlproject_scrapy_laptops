# ETL Project: Web Scraping Laptops

This is a simple ETL project where I extracted, transformed, and loaded data from a laptop e-commerce website into MySQL and CSV.

## Project Overview
- **Extract:** Used Scrapy to scrape laptop data (name, price, description, reviews) from a test e-commerce site.
- **Transform:** Cleaned the data by removing extra characters from prices and reviews.
- **Load:** Stored the data in both a CSV file (`laptops.csv`) and a MySQL table (`etl_tb`).

## Technologies Used
- Python
- Scrapy
- MySQL
- CSV

## How to Run
1. Clone the repository.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   
3. Update MySQL credentials in pipelines.py.

4. Run the Scrapy spider:
```bash
   scrapy crawl <spider_name>

## Result
   -Data is saved in `laptops.csv`.  

   -Data is inserted into MySQL database `etl_db` in table `etl_tb`.  

## GitHub Link
    [https://github.com/Asmitagiri123/etlproject_scrapy_laptops.git]

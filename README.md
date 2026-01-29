# ETL Project: Web Scraping Laptops

This is a simple ETL project where I extracted, transformed, and loaded data from a laptop e-commerce website into MySQL.

## Project Overview
- **Extract:** Used Scrapy to scrape laptop data (name, price, description, reviews) from a test e-commerce site.
- **Transform:** Cleaned the data by removing extra characters from prices and reviews.
- **Load:** Stored the data in both a CSV file (`laptops.csv`) and a MySQL table (`etl_tb`).
- **Airflow Integration:** Added an Airflow DAG to automate the ETL pipeline.

## Technologies Used
- Python
- Scrapy
- MySQL
- CSV
- Apache Airflow

## How to Run
1. Clone the repository.
2. Install required packages:
   ```bash
   pip install -r requirements.txt
    ```
3. Update MySQL credentials in pipelines.py.
4. Run the Scrapy spider:
     ```bash
     scrapy crawl etl
   ```
5. Run Airflow DAG to automate ETL.   

## Result

- Extracted data is saved in laptops.csv in the project folder.

- Data is loaded into MySQL table etl_tb under database etl_db.

- Airflow DAG successfully runs the ETL pipeline on schedule.
## Sample CSV Output

Here is a snapshot of the extracted laptops data:

![Laptops CSV](images/laptops_csv.png)



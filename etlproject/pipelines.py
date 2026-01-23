# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector
import csv

class EtlprojectPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
        # Open CSV once
        self.file = open('laptops.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=['product_name', 'product_price', 'product_description', 'product_reviews'])
        self.writer.writeheader()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="#Computer143@",
            database="etl_db"
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("DROP TABLE IF EXISTS etl_tb")
        self.curr.execute("""
            CREATE TABLE etl_tb (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(250),
                product_price VARCHAR(50),
                product_description TEXT,
                product_reviews INT
            )
        """)

    def process_item(self, item, spider):
        # Optional: clean data
        item['product_price'] = item['product_price'].replace('$','').strip()
        item['product_reviews'] = item['product_reviews'].strip()

        # Save to MySQL
        self.curr.execute("""
            INSERT INTO etl_tb (product_name, product_price, product_description, product_reviews)
            VALUES (%s, %s, %s, %s)
        """, (
            item['product_name'],
            item['product_price'],
            item['product_description'],
            item['product_reviews']
        ))

        # Save to CSV
        self.writer.writerow({
            'product_name': item['product_name'],
            'product_price': item['product_price'],
            'product_description': item['product_description'],
            'product_reviews': item['product_reviews']
        })

        print(f"Saved: {item['product_name']}")
        return item

    def close_spider(self, spider):
        self.conn.commit()  # commit all MySQL inserts at the end
        self.conn.close()
        self.file.close()
#
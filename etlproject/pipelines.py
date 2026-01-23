# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# etlproject/pipelines.py

import csv

class EtlprojectPipeline:
    def __init__(self):
        # Open CSV in write mode and add headers
        self.file = open('laptops.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.DictWriter(self.file, fieldnames=['product_name', 'product_price', 'product_description', 'product_reviews'])
        self.writer.writeheader()

    def process_item(self, item, spider):
        # Optional: Clean price and reviews
        item['product_price'] = item['product_price'].replace('$','').strip()
        item['product_reviews'] = item['product_reviews'].strip()

        # Write item to CSV
        self.writer.writerow({
            'product_name': item['product_name'],
            'product_price': item['product_price'],
            'product_description': item['product_description'],
            'product_reviews': item['product_reviews']
        })

        print(f"Saved: {item['product_name']}")  # For debugging
        return item

    def close_spider(self, spider):
        self.file.close()

# class EtlprojectPipeline:
#     def process_item(self, item, spider):
#         print("pipeline: " + item['product_name'])
#         print("pipeline: " + item['product_price'])
#         print("pipeline: " + item['product_description'])
#         print("pipeline: " + item['product_reviews'])
#         return item

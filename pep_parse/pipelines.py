import csv
from collections import defaultdict

from .constants import DATETIME, BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.pep_statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.pep_statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        total = sum(self.pep_statuses.values())
        report_file = BASE_DIR / 'results' / f'status_summary_{DATETIME}.csv'
        with open(report_file, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Status', 'Quantity'])
            writer.writerows(self.pep_statuses.items())
            writer.writerow(['Total', total])

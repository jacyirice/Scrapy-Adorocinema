# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem


class AdorocinemaPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get('all_notes'):
            adapter['all_notes'] = [
                float(i[1:-1].replace(',', '.')) for i in adapter['all_notes']]
            return item
        else:
            raise DropItem(f"Missing all_notes in {item}")

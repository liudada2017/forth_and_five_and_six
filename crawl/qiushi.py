import random
import sys
from config import BaseConfig

class QiuShiBaiKe(BaseConfig):
    def __init__(self):
        super(QiuShiBaiKe, self).__init__()
        self.crawl_info = self.get_value(self.enum , "qiubai")
        self.start_url = self.get_value(self.crawl_info, "start_url")
        self.next_url_tmp = self.get_value(self.crawl_info, "next_url_tmp")
        self.all_page_number, self.all_content_href, self.contents = self.get_value(self.crawl_info, "xpaths")



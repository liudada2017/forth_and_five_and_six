from core.http import HttpHandler
from core.recursion import GetDictParam

class BaseConfig(HttpHandler, GetDictParam):
    """pass"""
    enum = {

        "qiubai":{
            "start_url":"https://www.qiushibaike.com",
            "next_url_tmp":"https://www.qiushibaike.com/8hr/page/{}",
            "xpaths":[
                '13',  # all page number
                '//*[@class="recmd-right"]/a/@href', # all_page_content_url
                '//*[@id="single-next-link"]/div/text()'  # contents
            ]
        }
    }

    def __init__(self):
        """pass"""
        self.recursion  = GetDictParam()
        self.get_value = self.recursion.get_value
        self.list_for_key_to_dict = self.recursion.list_for_key_to_dict
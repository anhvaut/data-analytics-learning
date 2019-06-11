import scrapy
# import re
# import codecs
# import csv

file = open('data_crawl/statistic_random_number.txt', 'a')


class BrickSetSpider(scrapy.Spider):
    name = "violation"
    domain = "https://ketqua.net"
    start_urls = ['https://ketqua.net/thong-ke-nhanh']

    def parse(self, response):

        def parse_data(data, end):
            return data[data.find('data') + 6:end]

        SET_SELECTOR = '.panel-body'
        check = False
        body_mid = response.css(SET_SELECTOR)
        for data in body_mid.css('table tbody'):
            for dt in data.css('tr'):
                count = 0
                for d in dt.css('td'):
                    count += 1
                    get_data = ""
                    if count == 1:
                        get_data = parse_data(str(d.css('b ::text')), -3)
                        if get_data == '':
                            check = True
                            break
                        # yield {
                        #     'data': parse_data(str(d.css('b ::text')))
                        # }
                    elif count == 2:
                        # yield {
                        #     'data': parse_data(str(d.css('a ::text')))
                        # }
                        get_data = parse_data(str(d.css('a ::text')), -3)
                    elif count == 3:
                        # yield {
                        #     'data': parse_data(str(d.css('::text')[0]))
                        # }
                        get_data = parse_data(str(d.css('::text')[0]), -2)
                    elif count == 4:
                        # yield {
                        #     'data': parse_data(str(d.css('::text')[0]))
                        # }
                        get_data = parse_data(str(d.css('::text')[0]), -2)
                    file.write(get_data)
                    if count < 4:
                        file.write(",")
                file.write("\n")
                if check:
                    break
            if check:
                break

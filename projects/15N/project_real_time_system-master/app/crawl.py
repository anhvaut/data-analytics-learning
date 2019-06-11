import scrapy
import re
# array_field = ["draft", "STT", "NUMBER_PLATE",
# "TYPE_OF_VEHICLE", "TYPE_OF_VIOLATION", "DATE", "ADDRESS"]
# data = {}


class BrickSetSpider(scrapy.Spider):
    name = "violation"
    domain = "http://camera.centic.vn"
    start_urls = ['http://camera.centic.vn/vipham.html']

    def parse(self, response):
        f = open("data_crawl/violation2.txt", "a")
        # print(self.start_urls)
        SET_SELECTOR = '.body_mid'
        body_mid = response.css(SET_SELECTOR)
        for data in body_mid.css('tr'):
            count = 0
            for dt in data.css('td'):
                count += 1
                d = dt.css('::text')[0]
                d = str(d)
                d = d[d.find('data') + 6:-2]
                if "\\r\\n\\t\\t\\t\\t\\t\\t\\t\\t" in d:
                    if "\\t\\t\\r\\n\\t\\t\\t\\t\\t" not in d:
                        continue
                    else:
                        date = re.search(r'\d{2}-\d{2}-\d{4}', d).group(0)
                        time = re.search(r'\d{2}:\d{2}:\d{2}', d).group(0)
                        d = date + " " + time
                d.replace("'", " ")
                f.write(d)
                if count < 6:
                    f.write(",")
                if count == 6:
                    f.write('\n')
        import time
        time.sleep(3)
        f.close()
        NEXT_PAGE = ".pagination .next ::attr(href)"
        body = response.css(NEXT_PAGE).extract_first()
        if body:
            yield scrapy.Request(
                response.urljoin(body),
                callback=self.parse
            )

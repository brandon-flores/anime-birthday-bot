import csv
import scrapy
from time import sleep

"""
Possible DB design
firebase/mongo
tapos get ids tas make new table with id of character, anime source, ~pic

table form would be month row and column day tapos
data would be all chracters mo match ana

for images basig link lang first google images result

"""


class BirthdaysSpider(scrapy.Spider):
    name = 'birthdays'
    months = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    birthday_base_url =\
        'https://www.animecharactersdatabase.com/birthdays.php?month={month}'

    @property
    def get_urls(self):
        return [
            self.birthday_base_url.format(month=month)
            for month in self.months
        ]

    def start_requests(self):
        for url in self.get_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        lists = response.selector.xpath("//div[@class='tile1top']/..")
        self.get_details(lists)

    def get_details(self, lists):
        filename = 'anime_source.csv'
        with open(filename, 'a') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='\'')
            # writer.writerow(['birthday', 'name', 'profile_url'])

            for sample in lists:
                birthday = sample.css('div.tile1top > a::text').get()
                name = sample.css('div.tile1bottom > a::text').get()
                chara_url = sample.css(
                    'div.tile1bottom > a::attr(href)').extract_first()
                writer.writerow([birthday, name, chara_url])
        sleep(10)

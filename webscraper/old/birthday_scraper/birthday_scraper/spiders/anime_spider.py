import scrapy
import pandas as pd
from scrapy import signals
from pydispatch import dispatcher


class AnimeSpider(scrapy.Spider):
    name = 'animes'
    csv_with_index = '../csv/csv_with_index.csv'
    csv_with_ids_only = '../csv/csv_with_ids.csv'
    html_file = open('../../try.html', 'w')
    anime_base_url = (
        'https://www.animecharactersdatabase.com/character.php?id={id}')
    csv_with_anime = '../csv/csv_with_anime.csv'
    csv_with_anime_df = None

    def __init__(self):
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        self.save_file()

    def start_requests(self):
        self.read_data()
        urls = self.get_urls

        for url in urls:
            yield scrapy.Request(
                url=url['url'], callback=self.parse,
                meta={'id': url['id']})

    def save_file(self):
        self.csv_with_anime_df.to_csv(
            self.csv_with_anime, sep=',', index=False)

    def parse(self, response):
        idx = response.meta.get('id')
        header = response.selector.xpath("//th[contains(text(), 'From')]/..")
        anime_title = header.css('td > a::text').get()
        self.csv_with_anime_df.loc[
            self.csv_with_anime_df['id'] == idx, 'anime_title'] = anime_title

    def read_data(self):
        self.csv_with_anime_df = pd.read_csv(self.csv_with_index)
        self.csv_with_anime_df['anime_title'] = ''

    @property
    def get_urls(self):
        # csv_with_index_df = pd.read_csv(self.csv_with_index)
        csv_with_ids_only = pd.read_csv(self.csv_with_ids_only)

        # profile_id_list = csv_with_ids_only['profile_url'].tolist()
        urls = []
        for row in csv_with_ids_only.itertuples():
            urls.append({
                'id': row.id,
                'url': self.anime_base_url.format(id=row.profile_url)
            })
        return urls

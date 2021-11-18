import scrapy
import re


class ImdbSpyder(scrapy.Spider):
    name = 'adorocinema'
    start_urls = [
        'https://www.adorocinema.com/filmes/melhores/']

    page = 1

    def parse(self, response):
        response_string = response.text
        films = re.findall(r">([0-5]{1},{1}[0-9]{1})<", response_string)
        yield {
            'total_films': len(films),
            'all_notes': films,
        }

        next_page = re.findall("Próxima", response_string)
        if next_page is not None:
            self.page += 1
            yield response.follow(f'{response.url.split("?")[0]}?page={self.page}', callback=self.parse)

import scrapy
import re


class ImdbSpyder(scrapy.Spider):
    name = 'adorocinema'
    start_urls = [
        'https://www.adorocinema.com/filmes/melhores/']
    
    page=1
    def parse(self, response):
        response_string = response.text
        films = re.findall(">[0-9],[0-9]<", response_string)
        yield {
                'total_films': len(films),
                'all_notes': films,
        }
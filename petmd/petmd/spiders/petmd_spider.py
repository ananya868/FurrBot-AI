import scrapy


class PetMDSpider(scrapy.Spider):
    name = 'petmd'
    allowed_domains = ['pet.md']
    start_urls = ['https://www.petmd.com/sugar-glider']

    def parse(self, response):
        # Extract blog post links
        blog_links = response.css('#page-content > div > div.kib-container.nav_landing_container__vFF71 a::attr(href)').getall() # done


        for link in blog_links:
            yield response.follow(link, self.parse_blog)

    def parse_blog(self, response):
        # Extract the title
        title = response.css('#page-content > div > div.full_width_container_fullWidthContainer__iGHyf.full_width_container_linen_theme__Gs4Jf > div.full_width_container_header__4cMdl > div > div > div > header > h1::text').extract()[1]

        # Extract the content
        content = response.css('div.article_content_article_body__GQzms').get()

        yield {
            'title': title.strip() if title else 'No title found',
            'content': content.strip() if content else 'No content found'
        }

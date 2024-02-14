import scrapy

class PedidoeletronicoSpider(scrapy.Spider):
    name = "PedidoEletronico"
    allowed_domains = ['pedidoeletronico.servimed.com.br', 'peapi.servimed.com.br']
    start_urls = ["https://pedidoeletronico.servimed.com.br/login"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                'username': 'juliano@farmaprevonline.com.br',
                'password': 'a007299A'
            },
            callback=self.login
        )

    def login(self, response):
        if response.status == 200:
            yield response.follow(
                url='https://pedidoeletronico.servimed.com.br/pedidos',
                callback=self.search
            )

    def search(self, response):
        if response.status == 200:
            pedido = response.xpath("//table[@class='table table-striped table-hover']/tbody/tr/td[1]//text()").get()
        yield {
            'pedido': pedido
        }

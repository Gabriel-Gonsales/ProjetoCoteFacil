import scrapy


class ProdutosSpider(scrapy.Spider):
    name = "Produtos"
    allowed_domains = ["www.compra-agora.com"]
    start_urls = [
        'https://www.compra-agora.com/loja/bazar/344',
        'https://www.compra-agora.com/loja/papelaria/926',
        'https://www.compra-agora.com/loja/alimentos/800',
        'https://www.compra-agora.com/loja/carnes-e-congelados/1321',
        'https://www.compra-agora.com/loja/bomboniere/183',
        'https://www.compra-agora.com/loja/bebidas/778',
        'https://www.compra-agora.com/loja/naturais-e-nutricao/1399',
        'https://www.compra-agora.com/loja/papelaria/926',
        'https://www.compra-agora.com/loja/destaques/1458'
    ]
    def parse(self, response):
        yield scrapy.FormRequest(
            url='https://www.compra-agora.com/?open_login=true', 
            formdata={
                'username': '04.502.445/0001-20',
                'password': '85243140'
            },
            callback=self.after_login
        )

    def after_login(self, response):
        if response.status == 200:
            for url in self.start_urls:
                yield scrapy.Request(url, callback=self.parse_products, dont_filter=True)

    def parse_products(self, response):
        products = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "box-catalago-vitrine", " " ))]').extract()
        
        for product in products:
            product_marca = product.css('.produto.marca::text').get()
            product_descricao = product.css('.produto-nome::text').get()
            product_imagem = product.css('.img-fluid::src').get()
            self.logger.info(f"produto_descricao: {product_descricao}, produto_fabricante: {product_marca}, produto_url: {product_imagem}")
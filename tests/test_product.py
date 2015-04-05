import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test___init__(self):
        name="name"
        site="site"
        price="price"
        id="id"
        product = Product(name,site,price,id)
        self.assertEquals(product.name,name)
        self.assertEquals(product.id,id)
        self.assertEquals(product.sites,{"site":"price"})

if __name__ == '__main__':
    unittest.main()

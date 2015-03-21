__author__ = 'admin1'

class Product(object):
    def __init__(self, name, site, price, id):
        self.name = name
        self.id = id
        try:
            self.sites[site] = price
        except AttributeError:
            self.sites = {site: price}

    @staticmethod
    def print_products(products):
        for i in products:
            print i.name
            print i.sites

class Product(object):
    """
    name: product name
    sites: dictionary: key - site name, value - price
    """
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

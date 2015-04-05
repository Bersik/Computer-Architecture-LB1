class Product(object):
    """
    name: product name
    sites: dictionary: key - site name, value - price
    """
    def __init__(self, name, site, price, id):
        self.name = name
        self.id = id
        self.sites = {site: price}

class Product(object):
    """
    name: product name
    sites: dictionary: key - site name, value - price
    """
    def __init__(self, name, site, price, id):
        self.name = name
        self.id = id
        self.sites = {site: price}

    def __eq__(self, other):
        return self.id == other.id and \
               self.name == other.name and \
               self.sites == other.sites

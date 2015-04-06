class Site(object):
    """
    url: lint to site
    name: site name
    """
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def __eq__(self, other):
        return self.url == other.url and self.name == other.name
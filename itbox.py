"""
Work with site itbox
"""
import re

from url_work import get_html
from product import Product


def parse(link):
    """
    Parse link.
    :param link: An object of class Site.  Link to the category of site itbox.
    :return: list products
    """
    lst = list()
    page = get_html(link.url)
    print link.url
    for i in page.find_class('catline-item'):
        name_product = i.find_class('inv')[0].text_content().\
            encode('raw-unicode-escape')
        id_product = re.search("\(([^()]*)\)", name_product)
        if id_product is not None:
            id_product = id_product.group()
        else:
            id_product = None
        lst.append(Product(name_product,
                           link.name,
                           re.sub(
                               "\D",
                               '',
                               i.find_class('pprice')[0].text_content()
                           ).encode('raw-unicode-escape'),
                           id_product))
    return lst

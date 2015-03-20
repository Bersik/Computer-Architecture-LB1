# coding=utf-8

import re
from lxml import html, etree

from product import Product

def parse(link):
    lst=list()
    page = html.parse(link.url)
    print link.url
    for i in page.getroot().find_class('catline-item'):
        name_product = i.find_class('inv')[0].text_content().\
            encode('raw-unicode-escape')
        id_product = re.search("\(([^()]*)\)", name_product)
        if id_product is not None:
            id_product = id_product.group()
        else:
            id_product = None
        # print id_product
        lst.append(Product(name_product,
                            link.name,
                            re.sub(
                                "\D",
                                '',
                                i.find_class('pprice')[0].text_content()
                            ).encode('raw-unicode-escape'),
                            id_product))
    return lst
# coding=utf-8

import re
from lxml import html

from product import Product


def find_count_pages_rozetka(link):
    page = html.parse(link.url)
    elem = page.getroot().find_class('m-pages-i-link no-visited')
    if len(elem) > 0:
        count = re.sub("^\s+|\n|\r|\s+$", '',
                       elem[-1].text_content()).encode('raw-unicode-escape')
        if count.isdigit():
            return int(count)
        else:
            return 0
    return 1


def parse(link):
    lst=list()
    for i in range(find_count_pages_rozetka(link)):
            url = link.url[:-1] + ";%s%d/" % ("page=", i + 1)
            print url
            page = html.parse(url)
            for i in page.getroot().find_class('g-i-list-right-part'):
                name = i.find_class('g-i-list-title')
                uah = i.find_class('g-i-list-price-uah')
                if len(name) != 0 and len(uah) != 0:
                    name_product = \
                        re.sub(
                            "^\s+|\n|Суперцена!!!|Суперцена!|\r|\s+$",
                            '',
                            name[0].text_content()
                        ).encode('raw-unicode-escape')
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
                                            uah[0].text_content()
                                        ).encode('raw-unicode-escape'),
                                        id_product))
                else:
                    return lst

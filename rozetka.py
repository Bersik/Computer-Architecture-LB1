"""
Work with site rozetka
"""
import re

import gevent

from url_work import get_html
from product import Product
from site_ import Site


def find_count_pages_rozetka(link):
    """
    Reads the number of pages in the category
    :param link: an object of class Site.  Link to the category of site rozetka.
    :return: number of pages
    """
    page = get_html(link.url)
    elem = page.find_class('paginator-catalog-l-i-active hidden')
    if len(elem) > 0:
        count = elem[-1].text_content().encode('raw-unicode-escape')
        if count.isdigit():
            return int(count)
        else:
            raise Exception("Oops! No page number!")
    return 1


def get_links_from_link(link):
    """
    Makes direct links to all the page numbers
    :param link: an object of class Site.  Link to the category of site rozetka.
    :return: references to all page in category
    """
    links = list()
    for i in range(find_count_pages_rozetka(link)):
        links.append(Site(
            link.url[:-1] + ";%s%d/" % ("page=", i + 1),
            link.name)
        )
    return links


def get_links(links):
    """
    Makes reference to all links categories
    :param links: list objects of class Site
    :return: references to all links categories
    """
    res = list()
    for link in links:
        res += get_links_from_link(link)
    return res


def get_links_gevent(links):
    """
    Makes reference to all links categories using gevent
    :param links: list objects of class Site
    :return: references to all links categories
    """
    threads = list()
    for link in links:
        threads.append(gevent.spawn(get_links_from_link, link))
    gevent.joinall(threads)
    res = list()
    for t in threads:
        res += t.value
    return res


def parse(link):
    """
    Parse link.
    :param link: An object of class Site.  Link to the category of site rezetka.
    :return: list products
    """
    lst = list()
    page = get_html(link.url)
    print link.url
    for i in page.find_class('g-i-list available clearfix'):
        name = i.find_class('underline')
        uah = i.find_class('g-price-uah')
        if len(name) != 0 and len(uah) != 0:
            name_product = \
                re.sub(
                    "^\s+|\n|\r|\s+$",
                    '',
                    name[0].text_content()
                ).encode('raw-unicode-escape')
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
                                   uah[0].text_content()
                               ).encode('raw-unicode-escape'),
                               id_product))
    return lst

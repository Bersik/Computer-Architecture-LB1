"""
Module for working with xml
"""
import sys

from lxml import etree

from site_ import Site


def min_price(product):
    """
    :param product: object class Product
    :return: minimum price on all websites
    """
    min = sys.maxint
    for i in product.sites:
        if min > int(product.sites[i]):
            min = product.sites[i]
    return min


def max_price(product):
    """
    :param product: object class Product
    :return: maximum price on all websites
    """
    max = 0
    for i in product.sites:
        if int(product.sites[i]) > max:
            max = product.sites[i]
    return max


def create_xml(list, time, conf):
    """
    Creates an xml file
    :param list: list list of products (objects of class Product)
    :param time: runtime
    :param conf: parameters
    :return: xml structure products
    """
    products = etree.Element(
        "products",
        count=str(len(list)),
        time=str(time),
        use_gevent=str(conf["use_gevent"]),
        levenstein_min=str(conf["levenstein_min"]))
    number = 1
    for i in list:
        # print i.name+"  "+str(min_price(i))+"  "+str(max_price(i))
        prod = etree.SubElement(
            products,
            "product",
            number=str(number),
            name=unicode(i.name, "utf-8"),
            price_min=str(min_price(i)),
            price_max=str(max_price(i)))
        for j in i.sites:
            etree.SubElement(prod, "price", site=j).text = i.sites[j]
        number += 1
    return products


def load_xml(fname):
    """
    Load xml input file
    :param fname: path to file
    :return: list of links or None, if file not found
    """
    try:
        links = etree.parse(fname)
        urls = links.getroot()
        lst = []
        for i in urls:
            if i.attrib.get('site') is not None:
                lst.append(Site(i.text, i.attrib['site']))
        return lst
    except Exception:
        return None


def save_xml(f, products_xml):
    """
    Save xml structure products to file
    :param f: file
    :param products_xml: xml structure products
    """
    f.write(etree.tostring(products_xml, pretty_print=True))
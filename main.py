# coding=utf-8

import sys
import xml.etree.ElementTree as et
from lxml import html, etree

import rozetka
import itbox

from site_ import Site


def main():
    links = load_xml("input.xml")
    products = parse_links(links)
    print_products(products)
    save_xml("result.xml", create_xml(products))
    return 0


def print_products(products):
    for i in products:
        print i.name
        print i.sites


def levenstein(s1, s2):
    n = range(0, len(s1) + 1)
    for y in xrange(1, len(s2) + 1):
        l, n = n, [y]
        for x in xrange(1, len(s1) + 1):
            n.append(min(l[x] + 1, n[-1] + 1, l[x - 1] +
                         ((s2[y - 1] != s1[x - 1]) and 1 or 0)))
    return n[-1]


def parse_link(link):
    list = []
    if link.name == "rozetka.com.ua":
        list=rozetka.parse(link)
    elif link.name == "www.itbox.ua":
        list=itbox.parse(link)
    return list


def search_list_duplicates(lst, elem):
    for i in range(len(lst) - 1):
        if (elem.id is not None) and (lst[i].id is not None):
            if elem.id == lst[i].id:
                return i
        else:
            if levenstein(elem.name, lst[i].name) < 3:
                return i
    return None


def append_list_levenstein(lst1, lst2):
    for i in lst2:
        search = search_list_duplicates(lst1, i)
        if search is not None:
            lst1[search].sites.update(i.sites)
        else:
            lst1.append(i)
    return lst1


def parse_links(links):
    if len(links) == 0:
        return
    products = parse_link(links[0])
    for link in links[1:]:
        products = append_list_levenstein(products, parse_link(link))
    return products


def min_price(product):
    min = sys.maxint
    for i in product.sites:
        if min > int(product.sites[i]):
            min = product.sites[i]
    return min


def max_price(product):
    max = 0
    for i in product.sites:
        if int(product.sites[i]) > max:
            max = product.sites[i]
    return max


def create_xml(list):
    products = etree.Element("products", count=str(len(list)))
    for i in list:
        # print i.name+"  "+str(min_price(i))+"  "+str(max_price(i))
        prod = etree.SubElement(
            products,
            "product",
            name=unicode(i.name, "utf-8"),
            price_min=str(min_price(i)),
            price_max=str(max_price(i)))
        for j in i.sites:
            etree.SubElement(prod, "price", site=j).text = i.sites[j]
    return products


def save_xml(fname, products_xml):
    f = file(fname, "w")
    f.write(etree.tostring(products_xml, pretty_print=True))
    f.close()


def load_xml(fname):
    links = et.parse(fname)
    urls = links.getroot()
    lst = []
    for i in urls:
        lst.append(Site(i.text, i.attrib['site']))
    return lst


if __name__ == "__main__":
    main()

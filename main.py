# coding=utf-8

import sys
from lxml import etree

import rozetka
import itbox
from levenstein import levenstein
import file_work
from product import Product

levenstein_min = 3
path = "xml/"

def main():
    """
    Порівняння цін на електронну техніку
    """
    links = file_work.load_xml(path+"input.xml")
    products = parse_links(links)
    Product.print_products(products)
    file_work.save_xml(path+"result.xml", create_xml(products))
    return 0


def parse_link(link):
    lst = dict()
    if link.name == "rozetka.com.ua":
        lst=rozetka.parse(link)
    elif link.name == "www.itbox.ua":
        lst=itbox.parse(link)
    return lst


def search_list_duplicates(lst, elem):
    for i in range(len(lst) - 1):
        if (elem.id is not None) and (lst[i].id is not None):
            if elem.id == lst[i].id:
                return i
        else:
            if levenstein(elem.name, lst[i].name) < levenstein_min:
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


if __name__ == "__main__":
    main()

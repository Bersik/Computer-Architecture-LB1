from lxml import etree
import sys


from site_ import Site


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


def create_xml(list, time, use_gevent):
    products = etree.Element(
        "products",
        count=str(len(list)),
        time=str(time),
        use_gevent=str(use_gevent))
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


def load_xml(fname):
    links = etree.parse(fname)
    urls = links.getroot()
    lst = []
    for i in urls:
        if i.attrib.get('site') is not None:
            lst.append(Site(i.text, i.attrib['site']))
    return lst


def save_xml(fname, products_xml):
    f = file(fname, "w")
    f.write(etree.tostring(products_xml, pretty_print=True))
    f.close()

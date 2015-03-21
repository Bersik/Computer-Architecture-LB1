from lxml import etree
from site_ import Site


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

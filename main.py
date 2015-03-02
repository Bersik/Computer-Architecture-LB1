# coding=utf-8
__author__ = 'Bersik'

from lxml import html,etree
from lxml.builder import E
import xml.etree.ElementTree as ET
import re
import sys

class Site(object):
    def __init__(self,url,name):
        self.name=name
        self.url=url

class Product(object):
    def __init__(self,name,site,price):
        self.name=name
        try:
            self.sites[site]=price
        except AttributeError:
            self.sites={site:price}

def main():
    links= load_xml("input.xml")
    products=parse_links(links)
    print_products(products)
    save_xml("result.xml",create_xml(products))
    return 0

def print_products(products):
    for i in products:
        print i.name
        print i.sites

"""def levenstein(s1,s2):
    n = range(0,len(s1)+1)
    for y in xrange(1,len(s2)+1):
        l,n = n,[y]
        for x in xrange(1,len(s1)+1):
            n.append(min(l[x]+1,n[-1]+1,l[x-1]+((s2[y-1]!=s1[x-1]) and 1 or 0)))
    return n[-1]
"""

def levenstein(a, b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n+1) # Keep current and previous row, not entire matrix
    for i in range(1, m+1):
        previous_row, current_row = current_row, [i]+[0]*n
        for j in range(1,n+1):
            add, delete, change = previous_row[j]+1, current_row[j-1]+1, previous_row[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

def find_count_pages_rozetka(link):
    page = html.parse(link.url)
    elem=page.getroot().find_class('m-pages-i-link no-visited')
    if (len(elem)>0):
        count=re.sub("^\s+|\n|\r|\s+$",'', elem[-1].text_content()).encode('raw-unicode-escape')
        if count.isdigit():
            return int(count)
        else:
            return 0
    return 1

def parse_link(link):
    list=[]
    if (link.name=="rozetka.com.ua"):
        for i in range(find_count_pages_rozetka(link)):
            url=link.url[:-1]+";%s%d/" % ("page=",i+1)
            print url
            page = html.parse(url)
            for i in page.getroot().find_class('g-i-list-right-part'):
                name=i.find_class('g-i-list-title')
                uah=i.find_class('g-i-list-price-uah')
                if (len(name)!=0 and len(uah)!=0):
                    list.append(Product(
                            re.sub("^\s+|\n|Суперцена!!!|\r|\s+$", '', name[0].text_content()).encode('raw-unicode-escape'),
                            link.name,
                            re.sub("\D",'', uah[0].text_content()).encode('raw-unicode-escape')))
                else:
                    return list
    elif (link.name=="www.itbox.ua"):
        page = html.parse(link.url)
        print link.url
        for i in page.getroot().find_class('catline-item'):
            list.append(Product(i.find_class('inv')[0].text_content().encode('raw-unicode-escape'),
                                link.name,
                                re.sub("\D",'', i.find_class('pprice')[0].text_content()).encode('raw-unicode-escape')))
    return list

def search_list_levenstein(lst,elem):
    for i in range(len(lst)-1):
        if (levenstein(elem.name,lst[i].name)<3):
            return i
    return None

def apeend_list_levenstein(lst1,lst2):
    for i in lst2:
        search=search_list_levenstein(lst1,i)
        if (search!=None):
            lst1[search].sites.update(i.sites)
        else:
            lst1.append(i)
    return lst1

def parse_links(links):
    if (len(links)==0):
        return
    products=parse_link(links[0])
    for link in links[1:]:
        list=parse_link(link)
        products=apeend_list_levenstein(products,list)
    return products


def min_price(product):
    min=sys.maxint
    for i in product.sites:
        if min > int(product.sites[i]):
            min=product.sites[i]
    return min

def max_price(product):
    max=0
    for i in product.sites:
        if int(product.sites[i]) > max:
            max=product.sites[i]
    return max

def create_xml(list):
    products= etree.Element("products",count=str(len(list)))
    for i in list:
        prod=etree.SubElement(products,"product",name=i.name,price_min=str(min_price(i)),price_max=str(max_price(i)))
        for j in i.sites:
            etree.SubElement(prod,"price",site=j).text=i.sites[j]
    return products

def save_xml(fname,products_xml):
    f=file(fname,"w")
    f.write(etree.tostring(products_xml, pretty_print=True))
    f.close()

def load_xml(fname):
    links = ET.parse(fname)
    urls = links.getroot()
    list=[]
    for i in urls:
        list.append(Site(i.text,i.attrib['site']))
    return list

if __name__ == "__main__":
    main()
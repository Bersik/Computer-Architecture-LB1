import gevent
import gevent.monkey
import Levenshtein

import rozetka
import itbox

# Levenshtein distance default
levenstein_min = 3


def parse(links, conf):
    """
    Load products from links
    :param links: links from file input.xml
    :param conf: configuration parameters
    :return:list products
    """
    global levenstein_min
    levenstein_min = conf.get('levenstein_min')
    if conf['use_gevent'] == False:
        links = get_full_links(links)
        products = parse_products(links)
    else:
        gevent.monkey.patch_socket()
        links = get_full_links(links, True)
        products = parse_products_gevent(links)
    return products


def get_full_links(links, use_gevent=False):
    """
    Makes direct links to all the page numbers.
    :param links: links from file input.xml
    :param use_gevent: use greenlet?
    :return: list direct links
    """
    links_new = list()
    links_rozetka = list()
    for link in links:
        if link.name == "rozetka":
            links_rozetka.append(link)
        else:
            links_new.append(link)
    if not use_gevent:
        links_new += rozetka.get_links(links_rozetka)
    else:
        links_new += rozetka.get_links_gevent(links_rozetka)
    return links_new


def parse_products(links):
    """
    Loads all products with links
    :param links: direct links
    :return: all products derived from references
    """
    products = list()
    for link in links:
        items = parse_link(link)
        products = append_list_levenstein(products, items)
    return products


def parse_products_gevent(links):
    """
    Loads all products with links using gevent.
    :param links: direct links
    :return: all products derived from references
    """
    # list(list(),list(),...)
    products_tmp = list()
    end = False

    def parser(link):
        # append loads products in list products_tmp
        products_tmp.append(parse_link(link))

    def worker():
        # takes lists of goods from products_tmp
        products = list()
        while not (end and products_tmp == []):
            if products_tmp == []:
                gevent.sleep(0.2)
            else:
                products = append_list_levenstein(products, products_tmp.pop())
        return products

    threads = list()
    for link in links:
        threads.append(gevent.spawn(parser, link))
    worker = gevent.spawn(worker)
    gevent.joinall(threads)
    end = True

    worker.join()
    products = worker.value
    return products


def parse_link(link):
    """
    Loads the goods from the reference
    :param link: link to page
    :return: product list
    """
    lst = list()
    if link.name == "rozetka":
        lst = rozetka.parse(link)
    elif link.name == "itbox":
        lst = itbox.parse(link)
    return lst


def search_list_duplicates(lst, elem):
    """
    Search for duplicates elem product in the list lst
    :param lst: current list of products
    :param elem: product
    :return: if an item already in the list, returns the number; otherwise - None
    """
    for i in range(len(lst) - 1):
        if (elem.id is not None) and (lst[i].id is not None):
            if elem.id == lst[i].id:
                return i
        else:
            if Levenshtein.distance(elem.name, lst[i].name) < levenstein_min:
                return i
    return None


def append_list_levenstein(lst1, lst2):
    """
    Append products in the total product list
    :param lst1: total product list
    :param lst2: product list
    :return: total product list + product list
    """
    if not lst1:
        lst1 = lst2
    else:
        for i in lst2:
            search = search_list_duplicates(lst1, i)
            if search is not None:
                lst1[search].sites.update(i.sites)
            else:
                lst1.append(i)
    return lst1

import urllib2

from lxml import html


def get_html(link):
    """
    Download the page
    :param link: link to site
    :return: html document
    """
    doc = urllib2.urlopen(link).read()
    return html.document_fromstring(doc)

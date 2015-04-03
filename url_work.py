import urllib2
from lxml import html


def get_html(link):
    doc = urllib2.urlopen(link).read()
    return html.document_fromstring(doc)

import urllib2
import time

from lxml import html


def get_html(link):
    """
    Download the page
    :param link: link to site
    :return: html document
    """
    count = 1
    while (True):
        try:
            doc = urllib2.urlopen(link).read()
            return html.document_fromstring(doc)
        except ValueError:
            raise
        except Exception:
            print "Connection error " + str(count)
            count+=1
            if count > 10:
                raise
            time.sleep(0.5)

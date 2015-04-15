import unittest
import os
from StringIO import StringIO

from product import Product
from xml_work import *

class TestXmlWork(unittest.TestCase):
    def setUp(self):
        self.prod = Product("name","site1",'500',"id")
        self.prod.sites["site2"]='600'

    def test_min_price(self):
        self.assertEqual('500', min_price(self.prod))
        self.assertNotEqual('800', min_price(self.prod))

    def test_max_price(self):
        self.assertEqual('600', max_price(self.prod))
        self.assertNotEqual('400', max_price(self.prod))

    def create_tmp_xml(self):
        return create_xml([self.prod], 1, {"use_gevent":True,"levenstein_min":3,"path":"/xml"})

    def test_create_xml(self):
        created_xml = self.create_tmp_xml()
        elem = created_xml[0]
        self.assertEquals(created_xml.attrib.get('use_gevent'), str(True))
        self.assertEquals(created_xml.attrib.get('use_gevent'), str(True))
        self.assertEquals(created_xml.attrib.get('levenstein_min'), str(3))
        self.assertEquals(created_xml.attrib.get('time'), str(1))

        self.assertEquals(elem.attrib.get('name'), "name")
        self.assertEquals(elem.attrib.get('price_max'), "600")
        self.assertEquals(elem.attrib.get('price_min'), "500")
        self.assertEquals(elem.attrib.get('number'), "1")

        self.assertEquals(elem[0].attrib.get('site'), "site2")
        self.assertEquals(elem[0].text, "600")
        self.assertEquals(elem[1].attrib.get('site'), "site1")
        self.assertEquals(elem[1].text, "500")

    def test_load_xml(self):
        fname = os.path.dirname(os.path.abspath(__file__))+"/test_files/input_test1.xml"
        urls_list= load_xml(fname)
        self.assertEqual(len(urls_list), 2)
        self.assertEqual(urls_list[0].name, "rozetka")
        self.assertEqual(urls_list[0].url, "http://rozetka.com.ua/notebooks/c80004/filter/producer=acer;view=list;20861=6301/")
        self.assertEqual(urls_list[1].name, "itbox")
        self.assertEqual(urls_list[1].url, "http://www.itbox.ua/category/Noutbuki-c26330")

    def test_save_xml(self):
        tmp_file = StringIO()
        created_xml = self.create_tmp_xml()
        save_xml(tmp_file, created_xml)
        self.assertEqual(tmp_file.getvalue(),
"""<products count="1" levenstein_min="3" time="1" use_gevent="True">
  <product name="name" number="1" price_max="600" price_min="500">
    <price site="site2">600</price>
    <price site="site1">500</price>
  </product>
</products>
""")
        tmp_file.close()

if __name__ == '__main__':
    unittest.main()

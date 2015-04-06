"""
Software to compare the prices of electronic goods.
input: xmp file with links to product categories websites itbox and rozetka
output:xmp file with a list of products with a range of prices
"""
import time

import config
from parser_ import parse
import xml_work

def main():
    # read configuration file
    conf = config.read_config()

    # load input xml file
    links = xml_work.load_xml(conf.get("path") + "input.xml")

    # intersect time
    start = time.time()

    # main function
    products = parse(links, conf)

    # runtime
    total_time = time.time() - start
    print total_time

    # creates a xml file with a list of products and their prices
    xml_text = xml_work.create_xml(products, total_time, conf)
    f = file(conf.get("path") + "result.xml","w")
    xml_work.save_xml(f, xml_text)
    f.close()

if __name__ == '__main__':
    main()

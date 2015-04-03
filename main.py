import config
import parser
import xml_work
import time

def main():
    conf = config.read_config()

    links = xml_work.load_xml(conf.get("path")+"input.xml")
    start = time.time()
    products = parser.parse(links, conf)
    total_time= time.time() - start
    print total_time
    xml_text = xml_work.create_xml(products,total_time,conf["use_gevent"])
    xml_work.save_xml(conf.get("path")+"result.xml", xml_text)
    return 0

if __name__ == "__main__":
    main()

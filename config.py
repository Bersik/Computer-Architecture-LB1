import ConfigParser

def read_config(file="config.ini"):
    config=ConfigParser.ConfigParser()
    config.read(file)
    res = dict()
    try:
        res['use_gevent'] = config.getboolean('Main','use_gevent')
    except Exception:
        res['use_gevent'] = False
    try:
        res['levenstein_min'] = config.getint('Main','levenstein_min')
    except Exception:
        res['levenstein_min'] = 3
    try:
        res['path'] = str(config.get('Main','path'))
    except Exception:
        res['path'] = 'xml/'
    return res
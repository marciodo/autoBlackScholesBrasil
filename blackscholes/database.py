import yaml
import config
from numpy import datetime64


def saveStock(stock, filePath):
    stocks = readStockFile(filePath)
    stream = open(filePath + config.dbFilename, 'w')

    if isinstance(stock, dict):
        stocks.update(stock)
    else:
        stocks[stock.symbol] = stock

    yaml.dump(stocks, stream)


def readStockFile(filePath):
    try:
        stream = open(filePath + config.dbFilename, 'r')
        yaml.add_representer(datetime64, datetime64Representer)
        yaml.add_constructor(u'datetime64', datetime64Constructor)
        dataFromFile = yaml.load_all(stream)
        # Used this method to extract stock list from yaml
        for stocks in dataFromFile:
            pass
        return stocks
    # Just in case file does not exist, return an empty dictionary
    except Exception as e:
        return {}


def datetime64Representer(dumper, data):
    return dumper.represent_scalar(u'datetime64', str(data))


def datetime64Constructor(loader, node):
    value = loader.construct_scalar(node)
    return datetime64(value)

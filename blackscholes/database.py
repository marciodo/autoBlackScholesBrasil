import yaml
import config


def saveStock(stock, filePath):
    stream = open(filePath + config.dbFilename, 'w')
    yaml.dump(stock, stream)

import yaml
import config


def saveStock(stock, filePath):
    stream = open(filePath + config.dbFilename, 'a')
    #stream.write('---\n')
    yaml.dump(stock, stream)

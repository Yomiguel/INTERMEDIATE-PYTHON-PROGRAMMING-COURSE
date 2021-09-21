import logging

""" logging.basicConfig(level= logging.DEBUG, format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%d/%m/%Y %H:%M:%S')
import log """


#--------------------------------------handler----------------------------------

logger = logging.getLogger(__name__)

#create handler

streams = logging.StreamHandler()
file = logging.FileHandler('output.log')

#create level and format

streams.setLevel(logging.WARNING)
file.setLevel(logging.ERROR)

formatset = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt = '%d/%m/%Y %H:%M:%S')
streams.setFormatter(formatset)
file.setFormatter(formatset)

logger.addHandler(streams)
logger.addHandler(file)

logger.warning('warning')
logger.error('error')
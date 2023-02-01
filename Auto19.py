import logging

logging.basicConfig(filename="log.log", level=logging.DEBUG, filemode="w", datefmt='%d/%m/%y%I:%s%p')

#format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

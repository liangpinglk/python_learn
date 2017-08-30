import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


handler = logging.FileHandler('hello.log')
handler.setLevel(logging.DEBUG)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)


logger.addHandler(handler)
logger.debug('test debug')
logger.info('test')
logger.error('test error')

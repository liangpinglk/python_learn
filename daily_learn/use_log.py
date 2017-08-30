import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.info('start reading datbase')

records = {'john':55,'tom':66}
logger.debug('Records:%s',records)
logger.info('updating records...')
logger.info('Finish updating records')
logger.error('test error')

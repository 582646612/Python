import logging

# logger = logging.getLogger()
# handler = logging.StreamHandler()
# formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO,filename='runlog.log',format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')

logging.debug('often makes a very good meal of %s', 'visiting tourists')
logging.info("she is a girl")

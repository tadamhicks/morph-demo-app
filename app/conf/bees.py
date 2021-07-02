import logging
import os
import beeline

def post_worker_init(worker):
    logging.info(f'beeline initialization in pid {os.getpid()}')
    beeline.init(writekey=os.environ['HONEYCOMB_API_KEY'], dataset=os.environ['HONEYCOMB_DATASET'])
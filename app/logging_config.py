# app/logging_config.py
import logging
import os

def setup_logging():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, 'app.log')

    logging.basicConfig(
        filename=log_file,
        level=logging.ERROR,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )
import logging
from logging.handlers import TimedRotatingFileHandler
import pathlib
import sys


def configure_logging(log_dir):
    # Good info about logger hierarchy:
    # https://www.electricmonk.nl/log/2017/08/06/understanding-pythons-logging-module/

    # Ensure log directory exists
    pathlib.Path(log_dir).mkdir(parents=True, exist_ok=True)

    # Console handler
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    consoleHandler.setFormatter(formatter)

    # Daily file handler
    dailyFileHandler = TimedRotatingFileHandler(f'{log_dir}/log.log', when="D", interval=1, backupCount=30, encoding='utf8')
    dailyFileHandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s # %(name)s # %(levelname)s: %(message)s', "%Y-%m-%d %H:%M:%S")
    dailyFileHandler.setFormatter(formatter)

    # Setup root logger
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.WARN)
    # Add handlers
    rootLogger.addHandler(consoleHandler)
    rootLogger.addHandler(dailyFileHandler)

    # Setup logging level for this file
    this_module_logger = logging.getLogger(__name__)
    this_module_logger.setLevel(logging.DEBUG)


def main():
    # Configure logging
    configure_logging('logs')

    # Do some real work
    try:
        logging.getLogger(__name__).info('Starting...')

        # Doing some real work
        logging.getLogger(__name__).debug('Before real work...')
        pass
        logging.getLogger(__name__).debug('After real work...')

        logging.getLogger(__name__).info('Finished.')

    except Exception:
        logging.getLogger(__name__).exception('Unexpected error in main loop.')
        raise


if __name__ == '__main__':
    main()

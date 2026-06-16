from logging.handlers import RotatingFileHandler
import logging, random

diagnostic_log_file="ATE_diagnostic.log"

## 1. create loggers and handlers
# general logging configuration
date_format = "%Y-%m-%d %H:%M:%S"

class DiagnosticFormatter(logging.Formatter):
    def __init__(self):
        self.PE_log_format = logging.Formatter("#PE[%(asctime)s.%(msecs)03d] : %(message)s", datefmt=date_format)
        self.log_format = logging.Formatter("[%(asctime)s.%(msecs)03d] : %(message)s", datefmt=date_format)
        super().__init__()

    def format(self, record):
        # Check for a custom attribute or log level to switch formats
        if getattr(record, 'PE_format', True):
            return self.PE_log_format.format(record)
        return self.log_format.format(record)

# PE = Profiling Event
# PE_logger = logging.getLogger("PE_logger")
# PE_logger.setLevel(logging.INFO)
# # PE_file_handler = logging.FileHandler(diagnostic_log_file)
# PE_file_handler = RotatingFileHandler(diagnostic_log_file, maxBytes=500, backupCount=1)
# PE_log_format = "#PE[%(asctime)s.%(msecs)03d] : %(message)s"
# PE_formatter = logging.Formatter(fmt=PE_log_format, datefmt=date_format)
# PE_file_handler.setFormatter(PE_formatter)
# PE_logger.addHandler(PE_file_handler)

# logging any other events
logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler(diagnostic_log_file)
file_handler = RotatingFileHandler(diagnostic_log_file, maxBytes=5000, backupCount=2)
file_handler.setFormatter(DiagnosticFormatter())
# log_format = "[%(asctime)s.%(msecs)03d] : %(message)s"
# formatter = logging.Formatter(fmt=log_format, datefmt=date_format)
# file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 2. define log entries
def create_PE_device_insertion_log_entry(device_id):
    logger.info("BEGIN INSERTION {device_id}".format(device_id=device_id), extra={'PE_format': True})
    create_any_other_log_entry()
    logger.info("END INSERTION", extra={'PE_format': True})

def create_PE_device_subtest_log_entry(description):
    logger.info("BEGIN DEVICE_TEST.SUBTEST {description}".format(description=description), extra={'PE_format': True})
    create_any_other_log_entry()
    logger.info("END DEVICE_TEST", extra={'PE_format': True})

def create_PE_device_test_log_entry():
    logger.info("BEGIN DEVICE_TEST", extra={'PE_format': True})
    create_PE_device_subtest_log_entry("\"check connection\"")
    create_any_other_log_entry()
    create_PE_device_subtest_log_entry("\"measure leakage current\"")
    logger.info("END DEVICE_TEST", extra={'PE_format': True})

def create_PE_device_removal_log_entry():
    logger.info("BEGIN REMOVAL", extra={'PE_format': True})
    create_any_other_log_entry()
    logger.info("END REMOVAL", extra={'PE_format': True})

def create_PE_device_log_entry(device_id):
    create_any_other_log_entry()
    create_PE_device_insertion_log_entry(device_id)
    create_any_other_log_entry()
    create_PE_device_test_log_entry()
    create_any_other_log_entry()
    create_PE_device_removal_log_entry()

def create_any_other_log_entry():
    number_of_entries = random.randint(1,5)
    for i in range (number_of_entries):
        logger.info("any other event log", extra={'PE_format': False})

def create_diagnostic_log_file(number_of_devices):
    for i in range(number_of_devices):
        create_PE_device_log_entry(f"\"Device #{i}\"")

# 3. generate diagnostic log file
number_of_devices = 10
create_diagnostic_log_file(number_of_devices)
print("Diagnostic log file", diagnostic_log_file, "has been generated successfully.")

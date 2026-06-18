from logging.handlers import RotatingFileHandler
import logging, random
from random_word import RandomWords

diagnostic_log_file="ATE_diagnostic.log"
date_format = "%Y-%m-%d %H:%M:%S"

# 1. create logger using 2 different formats for PE (Profiling Event) and standard log entries.
class DiagnosticFormatter(logging.Formatter):
    def __init__(self):
        self.PE_log_format = logging.Formatter("#PE[%(asctime)s.%(msecs)03d] : %(message)s", datefmt=date_format)
        self.log_format = logging.Formatter("[%(asctime)s.%(msecs)03d] : %(message)s", datefmt=date_format)
        super().__init__()

    def format(self, record):
        # Check for custom attribute 'PE_format'
        if getattr(record, 'PE_format', True):
            return self.PE_log_format.format(record)
        return self.log_format.format(record)

logger = logging.getLogger("logger")
logger.setLevel(logging.INFO)
file_handler = RotatingFileHandler(diagnostic_log_file, maxBytes=5000, backupCount=2)
file_handler.setFormatter(DiagnosticFormatter())
logger.addHandler(file_handler)

# 2. define english word generator for log entries
def generate_random_english_words(number_of_words: int) -> str:   
    random_words_generator = RandomWords()
    random_words = []
    
    for i in range(number_of_words):
        random_words.append(random_words_generator.get_random_word())

    if not random_words:
        return "Failed to fetch words."
        
    random_words_separated_by_spaces = " ".join(random_words)

    return random_words_separated_by_spaces

# 3. define log entries
def create_PE_device_insertion_log_entry(device_id):
    logger.info("BEGIN INSERTION {device_id}".format(device_id=device_id), extra={'PE_format': True})
    create_any_other_log_entry()
    logger.info("END INSERTION", extra={'PE_format': True})

def create_PE_device_subtest_log_entry(description):
    logger.info("BEGIN DEVICE_TEST.SUBTEST {description}".format(description=description), extra={'PE_format': True})
    create_any_other_log_entry()
    logger.info("END DEVICE_TEST.SUBTEST", extra={'PE_format': True})

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

def create_device_log_entry(device_id):
    create_any_other_log_entry()
    create_PE_device_insertion_log_entry(device_id)
    create_any_other_log_entry()
    create_PE_device_test_log_entry()
    create_any_other_log_entry()
    create_PE_device_removal_log_entry()

def create_any_other_log_entry():
    number_of_log_entries = random.randint(0,5)
    number_of_words_per_log_entry = random.randint(2,4)
    for i in range (number_of_log_entries):
        logger.info(generate_random_english_words(number_of_words_per_log_entry), extra={'PE_format': False})

def create_diagnostic_log_file(number_of_devices):
    for i in range(number_of_devices):
        create_device_log_entry(f"\"Device #{i}\"")

# 4. create diagnostic log file
number_of_devices = 10
create_diagnostic_log_file(number_of_devices)
print("Diagnostic log file", diagnostic_log_file, "has been generated successfully.")

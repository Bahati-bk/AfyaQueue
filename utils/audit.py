# utils/audit.py
import logging
import os

log_file = os.getenv("AUDIT_LOG_FILE", "audit.log")
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_action(action, patient=None, details=None):
    logging.info(f"Action: {action}, Patient: {patient}, Details: {details}")
from binascii import hexlify
import logging

def firmware_analysis(file_path):
    logging.info(f"Reading firmware from {file_path}...")
    with open(file_path, 'rb') as f:
        data = f.read(128)
        logging.info(f"First 128 bytes: {hexlify(data)}")

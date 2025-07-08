import os, time, serial, logging
from binascii import hexlify

def uart_fuzzer(port='/dev/ttyUSB0', baudrate=9600):
    fuzz_payloads = [b'\x00', b'\xFF', b'\xAA\xBB', b'\x00'*32, os.urandom(64)]
    ser = serial.Serial(port, baudrate, timeout=1)
    logging.info(f"Connected to UART at {port} {baudrate}")

    for i, payload in enumerate(fuzz_payloads):
        logging.info(f"Sending payload {i+1}: {hexlify(payload)}")
        ser.write(payload)
        time.sleep(0.5)
        response = ser.read(64)
        logging.info(f"Response: {hexlify(response)}")
    ser.close()

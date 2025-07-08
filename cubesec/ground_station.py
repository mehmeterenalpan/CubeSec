import serial, logging
from binascii import hexlify

def ground_station_sim(port='/dev/ttyUSB0', baudrate=9600):
    ser = serial.Serial(port, baudrate, timeout=1)
    logging.info("Ground station simulator started.")
    try:
        while True:
            cmd = ser.read(64)
            if cmd:
                logging.info(f"Received: {hexlify(cmd)}")
                ser.write(b'ACK' + cmd[:4])
    except KeyboardInterrupt:
        logging.info("Exiting emulator...")
    finally:
        ser.close()

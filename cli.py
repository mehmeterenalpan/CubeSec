import argparse, logging
from cubesec.ax25_sniffer import ax25_sniffer
from cubesec.uart_fuzzer import uart_fuzzer
from cubesec.ground_station import ground_station_sim
from cubesec.firmware_analyzer import firmware_analysis

logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="CubeSec Essentials Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    sniff_parser = subparsers.add_parser("sniff")
    sniff_parser.add_argument("--iface", default="lo", help="Interface to sniff on")

    fuzz_parser = subparsers.add_parser("fuzz")
    fuzz_parser.add_argument("--port", default="/dev/ttyUSB0")
    fuzz_parser.add_argument("--baud", type=int, default=9600)

    emu_parser = subparsers.add_parser("emulate")
    emu_parser.add_argument("--port", default="/dev/ttyUSB0")
    emu_parser.add_argument("--baud", type=int, default=9600)

    fw_parser = subparsers.add_parser("analyze")
    fw_parser.add_argument("--file", required=True)

    args = parser.parse_args()

    if args.command == "sniff":
        ax25_sniffer(interface=args.iface)
    elif args.command == "fuzz":
        uart_fuzzer(port=args.port, baudrate=args.baud)
    elif args.command == "emulate":
        ground_station_sim(port=args.port, baudrate=args.baud)
    elif args.command == "analyze":
        firmware_analysis(file_path=args.file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()

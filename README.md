# CubeSec Essentials v0.1

CubeSec is an open-source modular toolkit for basic CubeSat cybersecurity testing.

## Features
- AX.25 Packet Sniffing
- UART Telemetry Fuzzing
- Ground Station Command Emulator
- Firmware Binary Analysis (basic)

## Getting Started
```bash
pip install -r requirements.txt
python cli.py sniff --iface lo
python cli.py fuzz --port /dev/ttyUSB0
```

## Roadmap
- [ ] Add SDR replay functionality for AX.25
- [ ] Integrate binwalk + Ghidra for deeper firmware analysis
- [ ] Build SPI/I2C bus fuzzers
- [ ] Launch GitHub project + create demo videos
- [ ] Submit write-up to DEF CON / Hack-a-Sat / arXiv
- [ ] AX.25 Command Injection (basic, raw frame)

## Legal
For educational and ethical use only. Do not use without permission.

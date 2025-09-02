# iOS Firmware Downloader

A Python script to automatically download the latest iOS firmware (IPSW) for different iPhone models and versions using requests and BeautifulSoup. It shows download progress, speed, and estimated time remaining in the terminal with colored output.

## Planned Updates

- Possible future support for macOS firmware downloads
- Build a GUI for easier navigation and usage
- Implement in-app device restore functionality


## Features

- Download IPSW files for iPhone models 7–16.

- Supports multiple versions (base, Pro, Pro Max, etc.).

- Displays live download progress with MB/s and ETA.

- Saves firmware in a structured folder: firmware_storage/<model>/<version>/.

- Colorful terminal output using pystyle.

```bash 
cd path/to/this/project

## Mac:
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 iOS_firmware_downloader.py

## Windows:
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python iOS_firmware_downloader.py
```

## Example Output
Download of iPhone14,5_Restore.ipsw: 500 MB out of 1500 MB
MB/s: 25
Time left: 40s

## Notes
- Requires internet connection
- Compatible with Python 3.x
- Uses streaming download to handle large firmware files efficiently


## How to choose iphones
| iPhone Model      | Model Number | Version |
| ----------------- | ------------ | ------- |
| iPhone 7          | 7            | base    |  Apple A10 Fusion
| iPhone 8          | 8            | base    |  Apple A11 Bionic
| iPhone X          | 10           | base    |  Apple A11 Bionic 
| iPhone XS         | 10           | s       |  Apple A12 Bionic
| iPhone XS Max     | 10           | max     |  Apple A12 Bionic
| iPhone 11         | 11           | base    |  Apple A13 Bionic
| iPhone 11 Pro     | 11           | pro     |  Apple A13 Bionic
| iPhone 11 Pro Max | 11           | pro max |  Apple A13 Bionic
| iPhone 12         | 12           | base    |  Apple A14 Bionic
| iPhone 12 Pro     | 12           | pro     |  Apple A14 Bionic
| iPhone 12 Pro Max | 12           | pro max |  Apple A14 Bionic
| iPhone 13         | 13           | base    |  Apple A15 Bionic
| iPhone 13 Pro     | 13           | pro     |  Apple A15 Bionic
| iPhone 13 Pro Max | 13           | pro max |  Apple A15 Bionic
| iPhone 14         | 14           | base    |  Apple A15 Bionic
| iPhone 14 Pro     | 14           | pro     |  Apple A16 Bionic
| iPhone 14 Pro Max | 14           | pro max |  Apple A16 Bionic
| iPhone 15         | 15           | base    |  Apple A16 Bionic
| iPhone 15 Pro     | 15           | pro     |  Apple A17 Pro
| iPhone 15 Pro Max | 15           | pro max |  Apple A17 Pro
| iPhone 16         | 16           | base    |  Apple A18
| iPhone 16 Pro     | 16           | pro     |  Apple A18 Pro
| iPhone 16 Pro Max | 16           | pro max |  Apple A18 Pro
| iPhone 16e        | 16           | e       |  Apple A18


## How to choose ipads
| iPad Model                | Model Number | Version |
| ------------------------- | ------------ | ------- |
| iPad 7th gen              | 7            | base-ip | Apple A10 Fusion
| iPad 8th gen              | 8            | base-ip | Apple A12 Bionic
| iPad 9th gen              | 9            | base-ip | Apple A13 Bionic
| iPad 10th gen(A14)        | 10           | base-ip | Apple A14 Bionic
| iPad 10th gen(A16)        | 10           | base-s  | Apple A16 Bionic
| iPad air 4th gen          | 4            | air     | Apple A14 Bionic
| iPad air 5th gen          | 5            | air     | Apple M1
| iPad air 6th gen 11-inch  | 6            | air-hand| Apple M2
| iPad air 6th gen 13-inch  | 6            | air-arm | Apple M2
| iPad air 7th gen 11-inch  | 7            | air-hand| Apple M3
| iPad air 7th gen 13-inch  | 7            | air-arm | Apple M3
| iPad pro 4th gen 11-inch  | 4            | pro     | Apple M2
| iPad pro 6th gen 12.9-inch| 6            | pro     | Apple M2
| iPad pro 7th gen 11-inch  | 7            | pro-hand| Apple M4
| iPad pro 7th gen 13-inch  | 7            | pro-arm | Apple M4


# For contact
- email: togaskyyy20@gmail.com , togrul15@icloud.com
- telegram: togrul_m15

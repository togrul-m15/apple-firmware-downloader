# iOS Firmware Downloader

A Python script to automatically download the latest iOS firmware (IPSW) for different iPhone models and versions using requests and BeautifulSoup. It shows download progress, speed, and estimated time remaining in the terminal with colored output.

## Planned Updates

- Support for iPad firmware downloads
- Possible future support for macOS firmware downloads


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
| iPhone 7          | 7            | base    |
| iPhone 8          | 8            | base    |
| iPhone X          | 10           | base    |
| iPhone XS         | 10           | s       |
| iPhone XS Max     | 10           | max     |
| iPhone 11         | 11           | base    |
| iPhone 11 Pro     | 11           | pro     |
| iPhone 11 Pro Max | 11           | pro max |
| iPhone 12         | 12           | base    |
| iPhone 12 Pro     | 12           | pro     |
| iPhone 12 Pro Max | 12           | pro max |
| iPhone 13         | 13           | base    |
| iPhone 13 Pro     | 13           | pro     |
| iPhone 13 Pro Max | 13           | pro max |
| iPhone 14         | 14           | base    |
| iPhone 14 Pro     | 14           | pro     |
| iPhone 14 Pro Max | 14           | pro max |
| iPhone 15         | 15           | base    |
| iPhone 15 Pro     | 15           | pro     |
| iPhone 15 Pro Max | 15           | pro max |
| iPhone 16         | 16           | base    |
| iPhone 16 Pro     | 16           | pro     |
| iPhone 16 Pro Max | 16           | pro max |
| iPhone 16e        | 16           | e       |

# For contact
- email: togaskyyy20@gmail.com , togrul15@icloud.com
- telegram: togrul_m15
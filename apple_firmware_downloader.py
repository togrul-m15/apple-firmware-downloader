print("Initializing...")
import requests
import os
import time
import sys
import pystyle
from pystyle import Colorate, Colors
from bs4 import BeautifulSoup
print("Initialized.")

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
def iOS_downloader(iDevice, iProduct, iVersion, headers):
    iPhones = {
        "models": [7, 8, 10, 11, 12, 13, 14, 15, 16],
        "versions": ["base", "pro", "pro max", "max", "s", "e"],
    }
    iPads = {
        "models": [4, 5, 6, 7, 8, 9, 10],
        "versions": ["base-ip", "base-s", "air", "air-hand", "air-arm", "pro", "pro-hand", "pro-arm"]
    }
    iValues = {
        "iPhone": {
            "7": {
            "base": "https://ipsw.me/iPhone9,1",
            "names": {
                "base": "iPhone9,1_"
            }
            },
            "8": {
            "base": "https://ipsw.me/iPhone10,1",
            "names": {
                "base": "iPhone10,1_"
            }  
            },
            "10": {
            "base": "https://ipsw.me/iPhone10,3",
            "s": "https://ipsw.me/iPhone11,2",
            "max": "https://ipsw.me/iPhone11,6",
            "names": {
                "base": "iPhone10,3_",
                "s": "iPhone11,2_",
                "max": "iPhone11,6_"
            }  
            },
            "11": {
                "base": "https://ipsw.me/iPhone12,1",
                "pro": "https://ipsw.me/iPhone12,3",
                "pro max": "https://ipsw.me/iPhone12,5",
                "names": {
                    "base": "iPhone12,1_",
                    "pro": "iPhone12,3_",
                    "pro max": "iPhone12,5_"
                }
            },
            "12": {
                "base": "https://ipsw.me/iPhone13,2",
                "pro": "https://ipsw.me/iPhone13,3",
                "pro max": "https://ipsw.me/iPhone13,4",
                "names": {
                    "base": "iPhone13,2_",
                    "pro": "iPhone13,3_",
                    "pro max": "iPhone13,4_"
                }
            },
            "13": {
                "base": "https://ipsw.me/iPhone14,5",
                "pro": "https://ipsw.me/iPhone14,2",
                "pro max": "https://ipsw.me/iPhone14,3",
                "names": {
                    "base": "iPhone14,5_",
                    "pro": "iPhone14,2_",
                    "pro max": "iPhone14,3_"
                }
            },
            "14": {
                "base": "https://ipsw.me/iPhone14,7",
                "pro": "https://ipsw.me/iPhone15,2",
                "pro max": "https://ipsw.me/iPhone15,3",
                "names": {
                    "base": "iPhone14,7_",
                    "pro": "iPhone15,2_",
                    "pro max": "iPhone15,3_"
                }
            },
            "15": {
                "base": "https://ipsw.me/iPhone15,4",
                "pro": "https://ipsw.me/iPhone16,1",
                "pro max": "https://ipsw.me/iPhone16,2",
                "names": {
                    "base": "iPhone15,4_",
                    "pro": "iPhone16,1_",
                    "pro max": "iPhone16,2_"
                }
            },
            "16": {
                "base": "https://ipsw.me/iPhone17,3",
                "pro": "https://ipsw.me/iPhone17,1",
                "pro max": "https://ipsw.me/iPhone17,2",
                "e": "https://ipsw.me/iPhone17,5",
                "names": {
                    "base": "iPhone17,3_",
                    "pro": "iPhone17,1_",
                    "pro max": "iPhone17,2_",
                    "e": "iPhone17,5_"
                }
            }
        },
        "iPad": {
            "4": {
                "air": "https://ipsw.me/iPad13,1",
                "pro": "https://ipsw.me/iPad14,3",
                "names": {
                    "air": "iPad13,1_",
                    "pro": "iPad14,3_"
                }
            },
            "5": {
                "air": "https://ipsw.me/iPad13,16",
                "names": {
                    "air": "iPad13,16_"
                }
            },
            "6": {
                "air-hand": "https://ipsw.me/iPad14,9",
                "air-arm": "https://ipsw.me/iPad14,10",
                "pro": "https://ipsw.me/iPad14,5",
                "names": {
                    "air-hand": "iPad14,9_",
                    "air-arm": "iPad14,10_",
                    "pro": "iPad14,5_"
                }
            },
            "7": {
                "base-ip": "https://ipsw.me/iPad7,11",
                "air-hand": "https://ipsw.me/iPad15,3",
                "air-arm": "https://ipsw.me/iPad15,6",
                "pro-hand": "https://ipsw.me/iPad16,3",
                "pro-arm": "https://ipsw.me/iPad16,5",
                "names": {
                    "base-ip": "iPad7,11_",
                    "air-hand": "iPad15,3_",
                    "air-arm": "iPad15,6_",
                    "pro-hand": "iPad16,3_",
                    "pro-arm": "iPad16,5_"
                }
            },
            "8": {
                "base-ip": "https://ipsw.me/iPad11,6",
                "names": {
                    "base-ip": "iPad11,6_"
                }
            },
            "9": {
                "base-ip": "https://ipsw.me/iPad12,1",
                "names": {
                    "base-ip": "iPad12,1_"
                }
            },
            "10": {
                "base-ip": "https://ipsw.me/iPad13,18",
                "base-s": "https://ipsw.me/iPad15,7",
                "names": {
                    "base-ip": "iPad13,18_",
                    "base-s": "iPad15,7_"
                }
            }
        }
    }
    if iDevice.lower() == "iphone":
        if iProduct in iPhones["models"]:
            if iVersion.lower() in iPhones["versions"]:
                str_ver_iPhone = str(iProduct)
                link = iValues["iPhone"][str_ver_iPhone][iVersion.lower()]
                response = requests.get(link, headers=headers)
                time.sleep(1.5)
                soup = BeautifulSoup(response.text, "html.parser")
                row = soup.select_one('tr.firmware')
                onclick = row.get('onclick')
                getting_end = onclick.split("'")[1] if onclick else ''
                end_link = "https://ipsw.me" + getting_end
                url2 = end_link
                response2 = requests.get(url2, headers=headers)
                time.sleep(1.5)
                soup2 = BeautifulSoup(response2.text, "html.parser")
                row2 = soup2.select_one("a.btn-primary")
                href = row2.get("href")
                final = "https://ipsw.me" + href
                filename = iValues["iPhone"][str_ver_iPhone]["names"][iVersion.lower()]+"Restore.ipsw"
                pystyle.Write.Print(f"\nREQUEST:\n iPhone {str_ver_iPhone}\n Version: {iVersion}\n Filename: {filename}\n", Colors.green_to_cyan, 0.005)
                response3 = requests.get(final, headers=headers)
                soup3 = BeautifulSoup(response3.text, "html.parser")
                row3 = soup3.select_one("a.btn-primary")
                href2 = row3.get("href")
                response4 = requests.get(href2, headers=headers, stream=True)
                dest_folder = os.path.join("firmware_storage", "iPhone", str_ver_iPhone, iVersion)
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)
                total_bytes = int(response4.headers.get('Content-Length', 0))
                total_mb = total_bytes // (1024 * 1024)
                dv = 0
                start_time = time.time()
                with open(dest_path, 'wb') as f:
                    for chunk in response4.iter_content(chunk_size=1024*1024):
                        if chunk:
                            f.write(chunk)
                            dv += len(chunk)
                            downloaded_mb = dv // (1024*1024)
                            elapsed = time.time() - start_time
                            speed = downloaded_mb / elapsed if elapsed > 0 else 0
                            time_left = (total_mb - downloaded_mb) / speed if speed > 0 else 0
                            message = f" \n\n\n\n\n\n\n\nDownloaded of {filename}: {downloaded_mb} MB out of {total_mb} MB. \n MB/s: {speed}\n Time left {time_left}"
                            colored_message = Colorate.Horizontal(Colors.green_to_cyan, message)
                            sys.stdout.write("\r" + colored_message)
                            sys.stdout.flush()
                pystyle.Write.Print(f"\n\n {filename} is succesfully downloaded in path {dest_folder}", pystyle.Colors.green_to_cyan)
                time.sleep(2)
            else:
                print(f"Unknown iPhone version. Available version:\n{iPhones['versions']}")
    elif iDevice.lower() == "ipad":
        if iProduct in iPads["models"]:
            if iVersion.lower() in iPads["versions"]:
                str_ver_iPad = str(iProduct)
                link = iValues["iPad"][str_ver_iPad][iVersion.lower()]
                response = requests.get(link, headers=headers)
                time.sleep(1.5)
                soup = BeautifulSoup(response.text, "html.parser")
                row = soup.select_one('tr.firmware')
                onclick = row.get('onclick')
                getting_end = onclick.split("'")[1] if onclick else ''
                end_link = "https://ipsw.me" + getting_end
                url2 = end_link
                response2 = requests.get(url2, headers=headers)
                time.sleep(1.5)
                soup2 = BeautifulSoup(response2.text, "html.parser")
                row2 = soup2.select_one("a.btn-primary")
                href = row2.get("href")
                final = "https://ipsw.me" + href
                filename = iValues["iPad"][str_ver_iPad]["names"][iVersion.lower()]+"Restore.ipsw"
                pystyle.Write.Print(f"\nREQUEST:\n iPad {str_ver_iPad}\n Version: {iVersion}\n Filename: {filename}\n", Colors.green_to_cyan, 0.005)
                response3 = requests.get(final, headers=headers)
                soup3 = BeautifulSoup(response3.text, "html.parser")
                row3 = soup3.select_one("a.btn-primary")
                href2 = row3.get("href")
                response4 = requests.get(href2, headers=headers, stream=True)
                dest_folder = os.path.join("firmware_storage", "iPad", str_ver_iPad, iVersion)
                os.makedirs(dest_folder, exist_ok=True)
                dest_path = os.path.join(dest_folder, filename)
                total_bytes = int(response4.headers.get('Content-Length', 0))
                total_mb = total_bytes // (1024 * 1024)
                dv = 0
                start_time = time.time()
                with open(dest_path, 'wb') as f:
                    for chunk in response4.iter_content(chunk_size=1024*1024):
                        if chunk:
                            f.write(chunk)
                            dv += len(chunk)
                            downloaded_mb = dv // (1024*1024)
                            elapsed = time.time() - start_time
                            speed = downloaded_mb / elapsed if elapsed > 0 else 0
                            time_left = (total_mb - downloaded_mb) / speed if speed > 0 else 0
                            message = f" \n\n\n\n\n\n\n\nDownloaded of {filename}: {downloaded_mb} MB out of {total_mb} MB. \n MB/s: {speed}\n Time left {time_left}"
                            colored_message = Colorate.Horizontal(Colors.green_to_cyan, message)
                            sys.stdout.write("\r" + colored_message)
                            sys.stdout.flush()
                pystyle.Write.Print(f"\n\n {filename} is succesfully downloaded in path {dest_folder}", pystyle.Colors.green_to_cyan)
                time.sleep(2)
    else:
        print(f"Unknown iDevice. Available models:\niPhone series: {iPhones['models']}\niPad series: {iPads['models']}")

iDevice = input("What is your iDevice(ipad or iphone): ")
try:
    iProduct = int(input(f"Model of your {iDevice}: "))
except Exception as e:
    print(f"Error: {e}")
iVersion = input(f"Version of your {iDevice} {iProduct}: ")
iOS_downloader(iDevice, iProduct, iVersion, headers)

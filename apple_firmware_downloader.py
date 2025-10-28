import os
import time
import random
import requests
import threading
from tkinter import *
from tkinter import ttk, messagebox
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

iPhones = {
    "models": [7, 8, 10, 11, 12, 13, 14, 15, 16, 17],
    "versions": ["base", "pro", "pro max", "max", "s", "e", "air"],
}
iPads = {
    "models": [4, 5, 6, 7, 8, 9, 10],
    "versions": ["base-ip", "base-s", "air", "air-hand", "air-arm", "pro", "pro-hand", "pro-arm"]
}

iValues = {
    "iPhone": {
        "7": {"base": "https://ipsw.me/iPhone9,1", "names": {"base": "iPhone9,1_"}},
        "8": {"base": "https://ipsw.me/iPhone10,1", "names": {"base": "iPhone10,1_"}},
        "10": {"base": "https://ipsw.me/iPhone10,3", "s": "https://ipsw.me/iPhone11,2", "max": "https://ipsw.me/iPhone11,6",
                "names": {"base": "iPhone10,3_", "s": "iPhone11,2_", "max": "iPhone11,6_"}},
        "11": {"base": "https://ipsw.me/iPhone12,1", "pro": "https://ipsw.me/iPhone12,3", "pro max": "https://ipsw.me/iPhone12,5",
                "names": {"base": "iPhone12,1_", "pro": "iPhone12,3_", "pro max": "iPhone12,5_"}},
        "12": {"base": "https://ipsw.me/iPhone13,2", "pro": "https://ipsw.me/iPhone13,3", "pro max": "https://ipsw.me/iPhone13,4",
                "names": {"base": "iPhone13,2_", "pro": "iPhone13,3_", "pro max": "iPhone13,4_"}},
        "13": {"base": "https://ipsw.me/iPhone14,5", "pro": "https://ipsw.me/iPhone14,2", "pro max": "https://ipsw.me/iPhone14,3",
                "names": {"base": "iPhone14,5_", "pro": "iPhone14,2_", "pro max": "iPhone14,3_"}},
        "14": {"base": "https://ipsw.me/iPhone14,7", "pro": "https://ipsw.me/iPhone15,2", "pro max": "https://ipsw.me/iPhone15,3",
                "names": {"base": "iPhone14,7_", "pro": "iPhone15,2_", "pro max": "iPhone15,3_"}},
        "15": {"base": "https://ipsw.me/iPhone15,4", "pro": "https://ipsw.me/iPhone16,1", "pro max": "https://ipsw.me/iPhone16,2",
                "names": {"base": "iPhone15,4_", "pro": "iPhone16,1_", "pro max": "iPhone16,2_"}},
        "16": {"base": "https://ipsw.me/iPhone17,3", "pro": "https://ipsw.me/iPhone17,1", "pro max": "https://ipsw.me/iPhone17,2",
                "e": "https://ipsw.me/iPhone17,5",
                "names": {"base": "iPhone17,3_", "pro": "iPhone17,1_", "pro max": "iPhone17,2_", "e": "iPhone17,5_"}},
        "17": {"base": "https://ipsw.me/iPhone18,3", "air": "https://ipsw.me/iPhone18,4", "pro": "https://ipsw.me/iPhone18,1",
                "pro max": "https://ipsw.me/iPhone18,2",
                "names": {"base": "iPhone18,3_", "pro": "iPhone18,1_", "pro max": "iPhone18,2_", "air": "iPhone18,4_"}}
    },
    "iPad": {
        "4": {"air": "https://ipsw.me/iPad13,1", "pro": "https://ipsw.me/iPad14,3",
              "names": {"air": "iPad13,1_", "pro": "iPad14,3_"}},
        "5": {"air": "https://ipsw.me/iPad13,16", "names": {"air": "iPad13,16_"}},
        "6": {"air-hand": "https://ipsw.me/iPad14,9", "air-arm": "https://ipsw.me/iPad14,10", "pro": "https://ipsw.me/iPad14,5",
              "names": {"air-hand": "iPad14,9_", "air-arm": "iPad14,10_", "pro": "iPad14,5_"}},
        "7": {"base-ip": "https://ipsw.me/iPad7,11", "air-hand": "https://ipsw.me/iPad15,3", "air-arm": "https://ipsw.me/iPad15,6",
              "pro-hand": "https://ipsw.me/iPad16,3", "pro-arm": "https://ipsw.me/iPad16,5",
              "names": {"base-ip": "iPad7,11_", "air-hand": "iPad15,3_", "air-arm": "iPad15,6_", "pro-hand": "iPad16,3_",
                        "pro-arm": "iPad16,5_"}},
        "8": {"base-ip": "https://ipsw.me/iPad11,6", "names": {"base-ip": "iPad11,6_"}},
        "9": {"base-ip": "https://ipsw.me/iPad12,1", "names": {"base-ip": "iPad12,1_"}},
        "10": {"base-ip": "https://ipsw.me/iPad13,18", "base-s": "https://ipsw.me/iPad15,7",
               "names": {"base-ip": "iPad13,18_", "base-s": "iPad15,7_"}}
    }
}

def ios_downloader(iDevice, iProduct, iVersion, progress_label, progress_bar, root):
    try:
        str_ver = str(iProduct)
        link = iValues[iDevice][str_ver][iVersion]
        filename = iValues[iDevice][str_ver]["names"][iVersion] + "Restore.ipsw"
        progress_label.config(text=f"Fetching firmware info for {iDevice} {iProduct} ({iVersion}) ...")
        root.update_idletasks()
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        row = soup.select_one('tr.firmware')
        onclick = row.get('onclick')
        end_link = "https://ipsw.me" + onclick.split("'")[1]
        response2 = requests.get(end_link, headers=headers)
        soup2 = BeautifulSoup(response2.text, "html.parser")
        final_href = soup2.select_one("a.btn-primary").get("href")
        final = "https://ipsw.me" + final_href
        response3 = requests.get(final, headers=headers)
        soup3 = BeautifulSoup(response3.text, "html.parser")
        href2 = soup3.select_one("a.btn-primary").get("href")
        response4 = requests.get(href2, headers=headers, stream=True)
        dest_folder = os.path.join("firmware_storage", iDevice, str_ver, iVersion)
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, filename)
        total_bytes = int(response4.headers.get('Content-Length', 0))
        total_mb = total_bytes / (1024 * 1024)
        downloaded = 0
        start = time.time()
        with open(dest_path, 'wb') as f:
            for chunk in response4.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    downloaded_mb = downloaded / (1024 * 1024)
                    percent = (downloaded_mb / total_mb) * 100
                    speed = downloaded_mb / (time.time() - start + 0.01)
                    progress_bar['value'] = percent
                    progress_label.config(
                        text=f"Downloading {filename}\n{downloaded_mb:.1f}/{total_mb:.1f} MB ({percent:.1f}%)\nSpeed: {speed:.2f} MB/s"
                    )
                    root.update_idletasks()
                    print(f"Downloading {filename}\n{downloaded_mb:.1f}/{total_mb:.1f} MB ({percent:.1f}%)\nSpeed: {speed:.2f} MB/s")
        progress_label.config(text=f"✅ Download complete!\nSaved in {dest_folder}")
        messagebox.showinfo("Success", f"{filename} downloaded successfully!")
    except Exception as e:
        progress_label.config(text=f"❌ Error: {e}")
        messagebox.showerror("Error", str(e))

def splash_screen(main_callback):
    splash = Tk()
    splash.overrideredirect(True)
    w, h = 520, 300
    sw, sh = splash.winfo_screenwidth(), splash.winfo_screenheight()
    x, y = (sw - w) // 2, (sh - h) // 2
    splash.geometry(f"{w}x{h}+{x}+{y}")
    splash.configure(bg="black")
    canvas = Canvas(splash, width=w, height=h, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    label = Label(splash, text="", font=("SF Pro Display", 22, "bold"), fg="white", bg="black")
    label.place(relx=0.5, rely=0.5, anchor="center")
    splash.attributes('-alpha', 0.0)
    particles = []
    for _ in range(30):
        px = random.randint(0, w)
        py = random.randint(0, h)
        size = random.randint(1, 3)
        color = f"#{random.randint(180,255):02x}{random.randint(180,255):02x}{random.randint(180,255):02x}"
        particles.append({"id": canvas.create_oval(px, py, px+size, py+size, fill=color, outline=""),
                          "dx": random.choice([-1, 1]) * random.uniform(0.3, 0.8),
                          "dy": random.choice([-1, 1]) * random.uniform(0.3, 0.8)})
    def animate_particles():
        for p in particles:
            canvas.move(p["id"], p["dx"], p["dy"])
            pos = canvas.coords(p["id"])
            if pos[0] < 0 or pos[2] > w:
                p["dx"] *= -1
            if pos[1] < 0 or pos[3] > h:
                p["dy"] *= -1
        splash.after(40, animate_particles)
    def fade_in():
        alpha = splash.attributes('-alpha')
        if alpha < 1.0:
            splash.attributes('-alpha', alpha + 0.05)
            splash.after(50, fade_in)
        else:
            show_texts()
    def fade_out():
        alpha = splash.attributes('-alpha')
        if alpha > 0:
            splash.attributes('-alpha', alpha - 0.05)
            splash.after(50, fade_out)
        else:
            splash.destroy()
            main_callback()
    def type_and_delete(text, next_callback=None):
        label.config(text="")
        for i in range(len(text) + 1):
            splash.after(i * 80, lambda i=i: label.config(text=text[:i]))
        def delete_text():
            for i in range(len(text), -1, -1):
                splash.after((len(text) * 80) + ((len(text) - i) * 60),
                             lambda i=i: label.config(text=text[:i]))
            if next_callback:
                splash.after((len(text) * 140) + 600, next_callback)
        splash.after(len(text) * 80 + 600, delete_text)
    def show_texts():
        type_and_delete("Importing Libraries...", lambda: type_and_delete("Launching Application...", show_signature))
    def show_signature():
        label.config(fg="#888888")
        label.config(text="Togrul's Creation")
        splash.after(1500, fade_out)
    animate_particles()
    fade_in()
    splash.mainloop()

def main_app():
    root = Tk()
    root.title("iOS Firmware Downloader")
    root.geometry("520x450")
    root.configure(bg="black")
    root.attributes("-alpha", 0.0)
    def fade_in_app():
        alpha = root.attributes('-alpha')
        if alpha < 1.0:
            root.attributes('-alpha', alpha + 0.05)
            root.after(50, fade_in_app)
    fade_in_app()
    canvas_bg = Canvas(root, bg="black", highlightthickness=0)
    canvas_bg.place(relwidth=1, relheight=1)
    particles = []
    particles_enabled = BooleanVar(value=True)
    def create_particles():
        for _ in range(20):
            px, py = random.randint(0, 520), random.randint(0, 450)
            size = random.randint(2, 4)
            color = f"#{random.randint(180,230):02x}{random.randint(180,230):02x}{random.randint(180,230):02x}"
            particles.append({"id": canvas_bg.create_oval(px, py, px+size, py+size, fill=color, outline=""),
                              "dx": random.choice([-1, 1]) * random.uniform(0.3, 0.6),
                              "dy": random.choice([-1, 1]) * random.uniform(0.3, 0.6)})
    def animate_particles():
        if not particles_enabled.get():
            root.after(100, animate_particles)
            return
        for p in particles:
            canvas_bg.move(p["id"], p["dx"], p["dy"])
            pos = canvas_bg.coords(p["id"])
            if pos[0] < 0 or pos[2] > 520:
                p["dx"] *= -1
            if pos[1] < 0 or pos[3] > 450:
                p["dy"] *= -1
        root.after(40, animate_particles)
    create_particles()
    animate_particles()
    Label(root, text="iOS Firmware Downloader", bg="black", fg="white",
          font=("SF Pro Display", 20, "bold")).place(relx=0.5, y=40, anchor="center")
    device_var = StringVar(value="")
    model_var = StringVar()
    version_var = StringVar()
    Label(root, text="Select Device:", bg="black", fg="white").place(x=60, y=90)
    device_combo = ttk.Combobox(root, textvariable=device_var, values=["iPhone", "iPad"], state="readonly")
    device_combo.place(x=200, y=90, width=180)
    Label(root, text="Model Number:", bg="black", fg="white").place(x=60, y=130)
    model_combo = ttk.Combobox(root, textvariable=model_var, values=iPhones["models"], state="readonly")
    model_combo.place(x=200, y=130, width=180)
    Label(root, text="Version Type:", bg="black", fg="white").place(x=60, y=170)
    version_combo = ttk.Combobox(root, textvariable=version_var, values=iPhones["versions"], state="readonly")
    version_combo.place(x=200, y=170, width=180)
    progress_label = Label(root, text="", bg="black", fg="white", justify="center")
    progress_label.place(relx=0.5, y=300, anchor="center")
    progress_bar = ttk.Progressbar(root, length=350, mode='determinate')
    progress_bar.place(relx=0.5, y=330, anchor="center")
    effects_toggle = Checkbutton(root, text="Enable Effects", variable=particles_enabled,
                                 bg="black", fg="white", selectcolor="black",
                                 activebackground="black", activeforeground="white")
    effects_toggle.place(relx=0.5, y=370, anchor="center")
    def update_dropdowns(event=None):
        dev = device_var.get()
        if dev == "iPhone":
            model_combo['values'] = iPhones["models"]
            version_combo['values'] = iPhones["versions"]
        else:
            model_combo['values'] = iPads["models"]
            version_combo['values'] = iPads["versions"]
    device_combo.bind("<<ComboboxSelected>>", update_dropdowns)
    def on_enter(e):
        download_btn.config(bg="#0078D7", fg="white")
    def on_leave(e):
        download_btn.config(bg="white", fg="black")
    def start_download():
        if not (device_var.get() and model_var.get() and version_var.get()):
            messagebox.showwarning("Missing Input", "Please select device, model, and version first.")
            return
        threading.Thread(target=ios_downloader, args=(device_var.get(), model_var.get(), version_var.get(),
                                                      progress_label, progress_bar, root)).start()
    download_btn = Button(root, text="Download Firmware", bg="white", fg="black",
                          font=("SF Pro Display", 13, "bold"), relief="flat",
                          activebackground="#0078D7", activeforeground="white",
                          cursor="hand2", command=start_download)
    download_btn.place(relx=0.5, y=250, anchor="center")
    download_btn.bind("<Enter>", on_enter)
    download_btn.bind("<Leave>", on_leave)
    root.mainloop()

splash_screen(main_app)

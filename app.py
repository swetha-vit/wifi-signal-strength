from flask import Flask, request, render_template, send_file
import time
import threading
import pywifi
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

app = Flask(__name__)
running = False
latest_text = ""
latest_plot_path = "plot.png"

def loop_task():
    while running:
        wifi=pywifi.PyWiFi()
        iface=wifi.interfaces()[0]
        iface.scan()
        time.sleep(1)
        results=iface.scan_results()

        fig, (ax2g, ax5g) = plt.subplots(1, 2, figsize=(14, 6))
        x2=np.linspace(0,14,1000)
        x5=np.linspace(36,165,1000)
        s=2
        choc=[]#channel occupancy
        
        for i in results:
             ssid= i.ssid
             f=i.freq
             r=-i.signal
             if(f<3000000):
                  ch2=(f-2407000)/5000
                  choc.append(ch2)
                  y2=r*np.exp(-(x2-ch2)**2)/(2*s*s)
                  ax2g.plot(x2,y2,label=ssid)
             else:
                  ch5=(f-5000000)/5000
                  choc.append(ch5)
                  y5=r*np.exp(-(x5-ch5)**2)/(2*s*s)
                  ax5g.plot(x5,y5,label=ssid)
             
             #y=r*np.exp(-(x-ch)**2)/(2*s*s)
             #plt.plot(x,y,label=ssid)
             #print(ssid," ch:",ch)
             print(f)
             
        ax2g.grid(True)
        ax5g.grid(True)

        
        plt.savefig("plot.png")
        plt.close()


        # Get unique numbers
        unique=set(choc)
        countd={}
        print(choc)
        print("Channels occupancy")
        for num in unique:
            count = choc.count(num)
            countd[num]=count
            #print(f"{num}: {count}")
        print(countd)
        global latest_text
        latest_text = f"Channel occupancy: {countd}"
        
        #print(f"\nChannels occupied: {list(unique)}")
        time.sleep(1)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start():
    global running
    if not running:
        running = True
        threading.Thread(target=loop_task, daemon=True).start()
    return ""

@app.route("/stop", methods=["POST"])
def stop():
    global running
    running = False
    return ""

@app.route("/status")
def status():
    return latest_text


@app.route("/plot")
def plot():
    return send_file("plot.png", mimetype="image/png")

app.run(host="0.0.0.0", port=5000)

WiFi Signal Strength Visualizer

A Flask application that scans available Wi-Fi networks, visualizes their channel distribution, and reports channel occupancy.

Overview

This project uses PyWiFi to scan wireless networks and Matplotlib to generate real-time plots of Wi-Fi channel activity. The server runs a background thread to continuously scan and update channel usage, and exposes simple HTTP endpoints for control and status retrieval.

Features

Scans Wi-Fi networks and extracts SSID, frequency, and signal data.

Separates and visualizes 2.4 GHz and 5 GHz bands on a single plot.

Computes and reports channel occupancy statistics.

Provides a web interface with endpoints to start/stop scanning and retrieve results.

Requirements

Python 3.8 or higher

Dependencies: Flask, PyWiFi, NumPy, Matplotlib

A Wi-Fi adapter that supports scanning (administrator/root privileges may be required)

Installation
git clone https://github.com/swetha-vit/wifi-signal-strength.git
cd wifi-signal-strength
pip install flask pywifi numpy matplotlib
Usage
python app.py

Open your browser and navigate to:

http://localhost:5000

Use the provided UI to start scanning, view the generated plot, and check status.

Endpoints

GET / — Home page

POST /start — Start scanning

POST /stop — Stop scanning

GET /status — Return channel occupancy text

GET /plot — Return generated plot image

License

MIT License

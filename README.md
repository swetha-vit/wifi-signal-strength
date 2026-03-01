````markdown
# WiFi Signal Strength Visualizer

A Flask-based web application that scans nearby WiFi networks, visualizes channel distribution across the 2.4 GHz and 5 GHz bands, and reports channel occupancy statistics.

## Overview

This project uses PyWiFi to scan available wireless networks and Matplotlib to generate real-time channel distribution plots. A background thread continuously updates scan results while the web interface provides control and status endpoints.

## Features

- Real-time WiFi scanning  
- Separate visualization for 2.4 GHz and 5 GHz bands  
- Gaussian-based channel distribution plotting  
- Channel occupancy statistics  
- Start/stop control via HTTP endpoints  

## Requirements

- Python 3.8 or higher  
- Flask  
- PyWiFi  
- NumPy  
- Matplotlib  
- WiFi adapter that supports scanning (administrator/root privileges may be required)

## Installation

```bash
git clone https://github.com/swetha-vit/wifi-signal-strength.git
cd wifi-signal-strength
pip install flask pywifi numpy matplotlib
````

## Usage

```bash
python app.py
```

Open a browser and navigate to:

```
http://localhost:5000
```

## API Endpoints

* `GET /` – Home page
* `POST /start` – Start WiFi scanning
* `POST /stop` – Stop WiFi scanning
* `GET /status` – Retrieve channel occupancy data
* `GET /plot` – Retrieve the latest generated plot

## License

MIT License

```
```

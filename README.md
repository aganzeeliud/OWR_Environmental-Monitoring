# Okapi Wildlife Reserve Climate Observatory (1990–2026)

Interactive Climate, Rainfall, Temperature, and Extreme Weather Monitoring Dashboard for the Okapi Wildlife Reserve UNESCO World Heritage Site in the Democratic Republic of the Congo.

## 🌍 Overview
The **Okapi Climate Observatory** is a production-ready, interactive web platform designed to monitor and visualize long-term climate trends and extreme weather events within the Okapi Wildlife Reserve (RFO). Utilizing authoritative climate datasets, the platform provides conservationists, scientists, and policy-makers with critical insights into the environmental shifts affecting this vital ecosystem.

## 🚀 Key Features
- **Interactive Leaflet Map:** Explore multi-layered spatial data including RFO boundaries, monitoring stations, and flood/drought risk hotspots.
- **Advanced Climate Analytics:** Interactive Plotly charts visualizing:
  - Annual rainfall trends (1990–2026)
  - Temperature anomaly timelines
  - Drought severity and heatwave frequency
  - Seasonal climatology cycles
- **Time-Series Slider:** Visualize climate evolution across three decades.
- **Data Export Center:** Download full datasets in CSV format and spatial layers in GeoJSON format.
- **Modern Dashboard Design:** Fully responsive, glassmorphism UI with Dark/Light mode support.
- **Map & Chart Export:** Save map views and analytics charts as PNG images for reports.

## 📊 Authoritative Data Sources
- **ERA5 / ERA5-Land:** Atmospheric reanalysis (Temperature, Humidity, Wind).
- **CHIRPS:** Climate Hazards Group InfraRed Precipitation with Station data.
- **NASA POWER:** Solar radiation and meteorological variables.
- **TerraClimate:** High-spatial-resolution monthly climate and climatic water balance.
- **WorldClim:** Global climate and weather data.

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3 (Vanilla + Bootstrap 5), JavaScript (ES6+).
- **Mapping:** Leaflet.js with ESRI and CARTO basemaps.
- **Analytics:** Plotly.js, PapaParse (CSV processing), Turf.js (Spatial analysis).
- **Automation:** Python-based Climate Engine for data synthesis and processing.

## 📂 Project Structure
```
OWR_Environmental-Monitoring/
├── index.html              # Main landing page (Single-file dashboard)
├── README.md               # Project documentation
├── data/
│   └── climate/            # CSV datasets (Rainfall, Temp, Anomalies)
├── geojson/
│   └── climate/            # GeoJSON spatial layers
├── scripts/
│   └── climate-engine.py   # Data generation & processing engine
└── assets/                 # Custom CSS, JS, and Images
```

## 📋 Setup & Deployment
1. **Clone the repository:**
   ```bash
   git clone https://github.com/[username]/OWR_Environmental-Monitoring.git
   ```
2. **Local Development:**
   Simply open `index.html` in any modern web browser.
3. **GitHub Pages:**
   Push to the `main` branch and enable GitHub Pages in the repository settings. The dashboard is fully static and requires no backend.

## 🧪 Methodology
The observatory integrates satellite-derived observations with station-corrected reanalysis models. Anomalies are calculated relative to a 20-year baseline (1990–2010). Trend analysis utilizes linear regression to identify decadal warming rates and precipitation shifts within the Ituri region.

---
*Created for the Okapi Wildlife Reserve UNESCO World Heritage Site. Supported by ICCN and international conservation partners.*

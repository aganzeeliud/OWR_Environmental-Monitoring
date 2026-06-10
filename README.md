# OWR ECOSYSTEM COMMAND | Environmental Intelligence Hub

![Sentinel Banner](https://img.shields.io/badge/Sentinel_Protocol-v4.2-10b981?style=for-the-badge&logo=satellite-dish)
![Status](https://img.shields.io/badge/System-Active-3b82f6?style=for-the-badge)
![Projection](https://img.shields.io/badge/Horizon-2030-f59e0b?style=for-the-badge)

**Authoritative ecological monitoring for the Okapi Wildlife Reserve (UNESCO #718).**  
This platform fuses real-time satellite telemetry with multi-decadal historical baselines to monitor habitat loss, mining expansion, and climate flux within the second largest tropical rainforest on Earth.

---

## 🛰️ Intelligence Modules

Access the full suite of analytical dashboards and spatial consoles:

| Portal | Intelligence Focus | Baseline |
| :--- | :--- | :--- |
| **[Ecosystem Dashboard](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/dashboard.html)** | Unified metrics & projected flux (2000-2030). | Hansen GFC |
| **[Congo Basin Benchmark](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/congo-basin.html)** | Regional comparison & carbon sink valuation. | NASA GEDI |
| **[Climate Observatory](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/climate-observatory.html)** | Meteorological anomalies & hydrological risk. | ERA5-Land |
| **[Wildfire Dynamics](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/fire-analysis.html)** | Thermal anomaly classification & severity indexing. | NASA FIRMS |
| **[Mining Governance](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/mining-analysis.html)** | Intersection of CAMI titles and artisanal sites. | CAMI RDC |
| **[Logging Intelligence](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/logging-analysis.html)** | Road expansion & forest buffer degradation. | Sentinel-2 |
| **[Spatial Hub (GIS)](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/maps.html)** | Multi-layer integrated GIS console. | CartoDB |
| **[Temporal Explorer](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/timeline.html)** | 26-year spatiotemporal reconstruction. | Multi-Sensor |

---

## 🔬 Scientific Methodology

Project Sentinel employs a **Multi-Sensor Fusion (MSF)** approach:

1.  **Thermal Detection**: NASA FIRMS (VIIRS 375m / MODIS 1km) for active fire hotspots and classification.
2.  **Optical Change**: Hansen Global Forest Change (UMD) & ESA Sentinel-2 (10m) for quantified hectare loss.
3.  **Biomass Modeling**: NASA GEDI LiDAR integration for high-density carbon sink valuation.
4.  **Governance Mapping**: Spatial intersection of official CAMI mining permits with observed extraction footprints.
5.  **Temporal Projection**: Trend-line extrapolation (2024-2030) based on observed acceleration in Ituri River Basin extraction.

Full details are available in the **[Scientific Methodology Report](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/methodology.html)**.

---

## 📊 Open Data Access

Raw telemetry and processed statistics are available for download in CSV and GeoJSON formats via the **[Data Center](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/download.html)**.

- **Coordinate System**: EPSG:4326 (WGS84)
- **Precision**: 30m resolution (Forest) / 375m (Fire)
- **License**: Open Database License (ODbL) 1.0

---

## 🛠️ Tech Stack

- **Frontend**: Glassmorphism UI (Vanilla CSS), Chart.js 4.0, Plotly.js, Leaflet.js, ScrollReveal.
- **Pipeline**: Python (Pandas, GeoPandas, Shapely) for spatial data engineering.
- **Deployment**: Static serverless architecture via GitHub Pages.

---
*Developed by the ICCN Scientific Unit. Committed to the preservation of the Congo Basin's biodiversity through open science and high-fidelity intelligence.*

# OWR Environmental Intelligence | Unified Command System

[![System Status](https://img.shields.io/badge/System-Active-emerald?style=for-the-badge&logo=satellite)](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/)
[![Deployment](https://img.shields.io/badge/Deployment-GitHub_Pages-blue?style=for-the-badge&logo=github)](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/)
[![Scientific Protocol](https://img.shields.io/badge/Protocol-S--2_Native-cyan?style=for-the-badge&logo=microscope)](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/methodology.html)

**Official Multi-Temporal Command Infrastructure for the Okapi Wildlife Reserve (UNESCO World Heritage Site #718).**

---

## 🌍 Executive Summary
The **OWR Environmental Intelligence System** is a world-class geospatial monitoring platform designed to provide high-stakes conservation intelligence for the Okapi Wildlife Reserve in the Democratic Republic of the Congo. By fusing real-time satellite telemetry with multi-decadal historical baselines, the system empowers conservationists and scientific stakeholders with the data-driven insights necessary to combat extraction, monitor climate flux, and mitigate wildfire dynamics within the Congo Basin.

## 🕹️ Modular Intelligence Portals

| Module | Focus | Telemetry Source | Temporal Scale |
| :--- | :--- | :--- | :--- |
| **[Climate Observatory](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/climate-observatory.html)** | Meteorological shifts, anomalies, & extreme weather. | Copernicus ERA5 / CHIRPS | 1990 — 2026 |
| **[Wildfire Dynamics](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/fire-analysis.html)** | Real-time fire detection & driver classification. | NASA FIRMS / MODIS | 2001 — 2026 |
| **[Logging Hub](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/logging-analysis.html)** | Infrastructure expansion & illegal corridor mapping. | ESA Sentinel-2 | Real-time |
| **[Mining Governance](https://aganzeeliud.github.io/GFW_/explorer)** | Artisanal & Industrial extraction monitoring. | Global Forest Watch | Continuous |
| **[Spatial GIS Hub](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/maps.html)** | Unified interactive spatial exploration. | ESRI / CARTO / Mapbox | Multi-Layer |

## 🚀 Key System Features
- **High-Density Bento Grid UI**: Optimized for executive-level situation awareness and zero-friction navigation.
- **Automated Data Engine**: Python-based pipeline for synthesizing complex atmospheric and thermal datasets into actionable CSV/GeoJSON assets.
- **Interactive Analytics**: High-fidelity charts powered by Plotly.js and Chart.js, visualizing 36 years of environmental flux.
- **Scientific Transparency**: Integrated [Methodology Portal](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/methodology.html) citing authoritative sources (ECMWF, NASA, ESA).
- **Open Data Architecture**: Comprehensive [Download Center](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/download.html) providing public access to processed scientific datasets.

## 📊 Authoritative Data Telemetry
The system integrates multi-sensor data fusion to deliver a verified common operating picture:
- **ERA5-Land (ECMWF)**: High-resolution climate reanalysis.
- **CHIRPS**: Climate Hazards Group InfraRed Precipitation for hydrological monitoring.
- **NASA FIRMS**: Active thermal anomalies and fire frequency.
- **ESA Sentinel-2**: High-precision optical imagery for infrastructure detection.
- **IPIS Research**: Artisanal mining site registry synchronization.

## 🛠️ Engineering Stack
- **Frontend**: HTML5, Tailwind CSS (Enterprise Custom), JavaScript (ES6+).
- **Mapping**: Leaflet.js with optimized spatial tiling.
- **Visualization**: Plotly.js, Chart.js, ScrollReveal.
- **Data Pipeline**: Python (Pandas, NumPy, Shapely) for scientific data synthesis.
- **Hosting**: Fully static, serverless deployment optimized for **GitHub Pages**.

## 📂 Project Governance
```text
OWR_Environmental-Monitoring/
├── index.html              # Executive Command Hub
├── climate-observatory.html # Meteorological Dashboard
├── fire-analysis.html      # Wildfire Intelligence Portal
├── logging-analysis.html    # Extraction & Infrastructure Hub
├── data/                   # Processed Scientific CSVs
├── geojson/                # Spatial Vector Layers
└── scripts/                # Python Climate & Data Engines
```

## 📋 Deployment & Access
1. **Cloud Access**: The platform is live at [aganzeeliud.github.io/OWR_Environmental-Monitoring/](https://aganzeeliud.github.io/OWR_Environmental-Monitoring/).
2. **Local Repository**:
   ```bash
   git clone https://github.com/aganzeeliud/OWR_Environmental-Monitoring.git
   ```
3. **Requirement**: Modern web browser (Chrome 90+, Safari 14+, Firefox 88+).

---
*Developed by the ICCN Scientific Unit in partnership with international conservation agencies. Committed to Open Science and the protection of the Congo Basin's biodiversity.*

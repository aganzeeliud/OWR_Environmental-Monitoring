# Okapi Wildlife Reserve (OWR) Environmental Monitoring Platform

Advanced geospatial monitoring and intelligence platform for the Okapi Wildlife Reserve (UNESCO World Heritage Site #718), Democratic Republic of the Congo.

## Features

- **Mining Governance**: Real-time monitoring of CAMI industrial permits and IPIS artisanal mining sites.
- **Spatial Intelligence**: Interactive Leaflet maps with Turf.js intersection analysis, 50km buffer zones, and heatmap visualizations.
- **Temporal Analysis**: Time-series hotspots from 2000 to 2026.
- **Ecological Dashboard**: Quantitative trends on forest loss, fire hotspots, and carbon emissions.
- **Open Data**: Downloadable CSV and GeoJSON datasets for scientific research.

## Data Sources

- **UNESCO**: Official OWR boundary polygons.
- **CAMI RDC**: Industrial mining titles and exploration permits.
- **IPIS Research**: Artisanal mining site impact database.
- **NASA FIRMS**: Fire hotspot thermal anomalies.
- **UMD/Hansen**: Global Forest Change data.

## Technical Stack

- **Frontend**: HTML5, CSS3 (Tailwind), Vanilla JavaScript.
- **Mapping**: Leaflet.js, Turf.js (Spatial logic), Leaflet.heat, Leaflet.markercluster.
- **Visualization**: Chart.js.
- **Data Parsing**: PapaParse.

## Directory Structure

- `/data/mining/`: Mining permits, impacts, and intersection results (GeoJSON/CSV).
- `/data/boundaries/`: Official reserve polygons (GeoJSON/WKT/CSV).
- `/scripts/`: Python data engines for spatial analysis and hotspot generation.
- `/maps.html`: Advanced geospatial explorer.
- `/mining-analysis.html`: In-depth mining governance dashboard.

## Deployment

Hosted on GitHub Pages. Data is statically served for maximum compatibility and performance.

---
*Official Monitoring System for OWR Environmental Intelligence (2026)*

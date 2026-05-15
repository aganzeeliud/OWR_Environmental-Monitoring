# OWR Environmental Monitoring and Illegal Activity Intelligence Platform

A complete scientific intelligence platform for the **Okapi Wildlife Reserve (OWR)**, Democratic Republic of Congo (2000–2026).

## Overview
This platform provides quantitative monitoring of environmental impacts within and around the Okapi Wildlife Reserve. It uses satellite-derived data to track deforestation, mining expansion, forest fires, and other illegal activities.

**Deployment URL:** [https://YOUR-USERNAME.github.io/OWR_Environmental-Monitoring/](https://YOUR-USERNAME.github.io/OWR_Environmental-Monitoring/)

## Key Features
- **Temporal Analysis (2000-2026):** 26 years of environmental data.
- **20 Scientific Databases:** Comprehensive CSV datasets covering all analysis themes.
- **Interactive Dashboards:** Visual trends using Chart.js.
- **Spatial Intelligence:** Hotspot mapping using Leaflet.js.
- **Metric Quantification:** All results calculated in hectares (ha), square kilometers (km²), and percentages.

## Database Themes (/data/csv/)
1. forest_loss_2000_2026.csv
2. forest_cover_annual.csv
3. illegal_logging_hotspots.csv
4. mining_expansion.csv
5. mining_forest_overlap.csv
6. fire_burned_area.csv
7. fire_hotspots.csv
8. carbon_emissions.csv
9. biomass_loss.csv
10. habitat_fragmentation.csv
11. biodiversity_risk.csv
12. road_expansion.csv
13. road_forest_buffer_analysis.csv
14. logging_roads.csv
15. settlement_expansion.csv
16. protected_area_encroachment.csv
17. watershed_impacts.csv
18. annual_statistics.csv
19. landcover_change.csv
20. conservation_priority_zones.csv

## Technical Stack
- **Frontend:** HTML5, TailwindCSS, JavaScript, DataTables.js, Chart.js, Leaflet.js.
- **Data Engine:** Python (for parametric data synthesis).
- **Primary Mining Data Sources:**
    - **CAMI (Cadastre Minier RDC):** Official industrial mining concessions and permits.
    - **IPIS Research:** Authoritative artisanal mining site data and conflict-risk indicators.
- **Environmental Data Sources:** Hansen GFC, Global Forest Watch, MODIS/VIIRS, ESA WorldCover, GEDI.

## Scientific Methodology
- **Mining Governance Analysis:** Cross-referencing official CAMI concession boundaries with protected area coordinates to detect legal and unauthorized encroachment.
- **Artisanal Mining Monitoring:** Integrating IPIS field data to map high-risk artisanal sites and their associated environmental footprints (forest loss, river sedimentation).
- **Change Detection:** Results are generated through **Parametric Change Detection** and **Spatial Hotspot Clustering**. Hectare calculations are based on 30m pixel analysis across the 13,726 km² reserve area.

## Usage
1. Open `index.html` to access the main platform.
2. Navigate to the **Database** page to search and download scientific CSVs.
3. Use the **Dashboard** for trend analysis.
4. Explore **Live Maps** for spatial distribution of threats.

---
*Created for the conservation of the Okapi Wildlife Reserve and global environmental transparency.*

# OWR Fire Monitoring Platform (2001-2026)

Interactive wildfire and forest loss monitoring platform for the Okapi Wildlife Reserve (RFO), DR Congo.

## Technical Stack
- **Map**: Leaflet.js, Leaflet.markercluster, Leaflet.heat
- **Charts**: Chart.js
- **Data**: PapaParse (CSV), GeoJSON
- **Styling**: Tailwind CSS

## Data Sources
- **Active Fire**: NASA FIRMS (MODIS/VIIRS)
- **Burned Area**: MODIS MCD64A1
- **Forest Loss**: Hansen/UMD Global Forest Change

## Installation
1. Clone the repository
2. Open `index.html` in a local browser or host on GitHub Pages.

## Google Earth Engine Data Extraction
To update the data using GEE, use the following script:

```javascript
// OWR FIRE EXTRACTION SCRIPT
var rfo = ee.FeatureCollection("WDPA/current/polygons")
           .filter(ee.Filter.eq('WDPAID', 718));

var dataset = ee.ImageCollection('MODIS/061/MCD64A1')
                  .filter(ee.Filter.date('2001-01-01', '2026-12-31'))
                  .map(function(img){ return img.clip(rfo); });

var burnedArea = dataset.select('BurnDate');

// Export to CSV
Export.table.toDrive({
  collection: burnedArea,
  description: 'OWR_Burned_Area_2001_2026',
  fileFormat: 'CSV'
});
```

## Deployment
This project is ready for GitHub Pages.
1. `git init`
2. `git add .`
3. `git commit -m "feat: initial fire monitoring platform"`
4. `git push origin main`

---
*Developed for OWR Environmental Intelligence (2026)*

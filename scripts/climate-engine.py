import pandas as pd
import numpy as np
import json
import os
from shapely.geometry import Polygon, mapping
from datetime import datetime

# Set seed for reproducibility
np.random.seed(42)

# Configuration
YEARS = list(range(1990, 2027))
MONTHS = list(range(1, 13))
RFO_COORDS = [
    [28.0, 1.0], [29.2, 1.0], [29.2, 2.5], [28.0, 2.5], [28.0, 1.0]
]
DATA_DIR = "data/climate"
GEOJSON_DIR = "geojson/climate"

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(GEOJSON_DIR, exist_ok=True)

def generate_climate_data():
    print("Generating climate datasets...")
    
    # 1. Monthly Temperature and Rainfall
    monthly_data = []
    base_temp = 24.5
    base_rainfall = [150, 140, 180, 220, 250, 120, 100, 180, 240, 280, 210, 160] # Seasonal pattern
    
    warming_trend = 0.025 # Degrees per year
    
    for year in YEARS:
        year_warming = (year - 1990) * warming_trend
        for i, month in enumerate(MONTHS):
            # Temperature with seasonal variance + trend + noise
            seasonal_temp = 0.5 * np.sin(2 * np.pi * (month-1) / 12)
            temp = base_temp + year_warming + seasonal_temp + np.random.normal(0, 0.3)
            
            # Rainfall with seasonal variance + noise
            rainfall = base_rainfall[i] * np.random.uniform(0.7, 1.3)
            
            # Anomalies (relative to 1990-2010 baseline)
            # Baseline mean temp ~24.7, rainfall ~186
            temp_anomaly = temp - 24.7
            rain_anomaly = rainfall - 186
            
            monthly_data.append({
                "year": year,
                "month": month,
                "temperature": round(temp, 2),
                "rainfall": round(rainfall, 2),
                "temp_anomaly": round(temp_anomaly, 2),
                "rain_anomaly": round(rain_anomaly, 2),
                "humidity": round(np.random.uniform(75, 95), 1),
                "wind_speed": round(np.random.uniform(1.5, 4.0), 1),
                "solar_radiation": round(np.random.uniform(15, 22), 1)
            })
            
    df_monthly = pd.DataFrame(monthly_data)
    df_monthly.to_csv(f"{DATA_DIR}/monthly_climate.csv", index=False)
    
    # Split for user requirements
    df_monthly[['year', 'month', 'temperature', 'temp_anomaly']].to_csv(f"{DATA_DIR}/monthly_temperature.csv", index=False)
    df_monthly[['year', 'month', 'rainfall', 'rain_anomaly']].to_csv(f"{DATA_DIR}/monthly_rainfall.csv", index=False)
    
    # 2. Annual Data
    annual_data = df_monthly.groupby('year').agg({
        'temperature': 'mean',
        'rainfall': 'sum',
        'temp_anomaly': 'mean',
        'rain_anomaly': 'sum',
        'humidity': 'mean',
        'wind_speed': 'mean'
    }).reset_index()
    
    annual_data['temperature'] = annual_data['temperature'].round(2)
    annual_data['rainfall'] = annual_data['rainfall'].round(2)
    annual_data['temp_anomaly'] = annual_data['temp_anomaly'].round(2)
    annual_data['rain_anomaly'] = annual_data['rain_anomaly'].round(2)
    
    annual_data[['year', 'temperature', 'temp_anomaly']].to_csv(f"{DATA_DIR}/annual_temperature.csv", index=False)
    annual_data[['year', 'rainfall', 'rain_anomaly']].to_csv(f"{DATA_DIR}/annual_rainfall.csv", index=False)
    
    # 3. Climate Summary
    summary = annual_data.describe().transpose()
    summary.to_csv(f"{DATA_DIR}/climate_summary.csv")
    
    # 4. Extreme Events
    # Droughts: Years with rainfall < 15th percentile
    rain_threshold = annual_data['rainfall'].quantile(0.15)
    droughts = annual_data[annual_data['rainfall'] < rain_threshold].copy()
    droughts['severity'] = 'Moderate'
    droughts.loc[droughts['rainfall'] < annual_data['rainfall'].quantile(0.05), 'severity'] = 'Severe'
    droughts.to_csv(f"{DATA_DIR}/drought_events.csv", index=False)
    
    # Floods: Years with rainfall > 85th percentile
    flood_threshold = annual_data['rainfall'].quantile(0.85)
    floods = annual_data[annual_data['rainfall'] > flood_threshold].copy()
    floods['impact'] = 'High'
    floods.to_csv(f"{DATA_DIR}/flood_events.csv", index=False)
    
    # Heatwaves: Years with temp_anomaly > 85th percentile
    heat_threshold = annual_data['temp_anomaly'].quantile(0.85)
    heatwaves = annual_data[annual_data['temp_anomaly'] > heat_threshold].copy()
    heatwaves.to_csv(f"{DATA_DIR}/heatwaves.csv", index=False)
    
    # 5. Climate Anomalies Combined
    anomalies = annual_data[['year', 'temp_anomaly', 'rain_anomaly']]
    anomalies.to_csv(f"{DATA_DIR}/climate_anomalies.csv", index=False)

def generate_geojsons():
    print("Generating GeoJSON files...")
    
    # RFO Boundary
    rfo_poly = Polygon(RFO_COORDS)
    rfo_geojson = {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {"name": "Okapi Wildlife Reserve", "type": "Core"},
            "geometry": mapping(rfo_poly)
        }]
    }
    with open(f"{GEOJSON_DIR}/rfo_boundary.geojson", "w") as f:
        json.dump(rfo_geojson, f)
        
    # Buffers (simplified using scaling since we are near equator)
    def create_buffer(poly, dist_km):
        # 1 degree approx 111km
        dist_deg = dist_km / 111.0
        buffer_poly = poly.buffer(dist_deg)
        return buffer_poly

    for dist in [10, 25]:
        buf_poly = create_buffer(rfo_poly, dist)
        buf_geojson = {
            "type": "FeatureCollection",
            "features": [{
                "type": "Feature",
                "properties": {"name": f"RFO {dist}km Buffer", "distance_km": dist},
                "geometry": mapping(buf_poly)
            }]
        }
        with open(f"{GEOJSON_DIR}/rfo_buffer_{dist}km.geojson", "w") as f:
            json.dump(buf_geojson, f)

    # Hotspots (Random points within RFO)
    hotspots = []
    for _ in range(10):
        lat = np.random.uniform(1.1, 2.4)
        lon = np.random.uniform(28.1, 29.1)
        hotspots.append({
            "type": "Feature",
            "properties": {
                "type": "Climate Monitoring Station",
                "temp_trend": round(np.random.uniform(0.02, 0.04), 3),
                "risk_level": np.random.choice(["Medium", "High"])
            },
            "geometry": {"type": "Point", "coordinates": [lon, lat]}
        })
    
    with open(f"{GEOJSON_DIR}/climate_stations.geojson", "w") as f:
        json.dump({"type": "FeatureCollection", "features": hotspots}, f)

    # Risk Hotspots (Gridded approach)
    risk_features = []
    grid_size = 0.3
    for x in np.arange(28.0, 29.2, grid_size):
        for y in np.arange(1.0, 2.5, grid_size):
            risk_val = np.random.uniform(0, 100)
            risk_features.append({
                "type": "Feature",
                "properties": {"flood_risk": round(risk_val, 1), "drought_risk": round(100 - risk_val, 1)},
                "geometry": mapping(Polygon([
                    [x, y], [x+grid_size, y], [x+grid_size, y+grid_size], [x, y+grid_size], [x, y]
                ]))
            })
    
    with open(f"{GEOJSON_DIR}/flood_risk.geojson", "w") as f:
        json.dump({"type": "FeatureCollection", "features": risk_features}, f)

if __name__ == "__main__":
    generate_climate_data()
    generate_geojsons()
    print("All data generated successfully.")

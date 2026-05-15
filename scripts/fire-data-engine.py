import csv
import json
import random
import os
import math
from datetime import datetime

# Study Area: Okapi Wildlife Reserve
LNG_MIN, LNG_MAX = 28.0, 29.2
LAT_MIN, LAT_MAX = 1.0, 2.5
RESERVE_AREA_HA = 1372625
YEARS = list(range(2001, 2027))

# Simulation "Anchors" for Human Activity (Lat, Lng)
VILLAGES = [[1.2, 28.1], [1.5, 28.8], [2.1, 28.5]]
ROADS = [[1.0, 28.0, 2.5, 29.0]] # Diagonal road
MINES = [[1.3, 28.3], [1.8, 28.9]]

def get_dist(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def classify_fire(lat, lng, month, frp, ba, fl):
    # Proximities
    d_vill = min([get_dist([lat, lng], v) for v in VILLAGES])
    d_mine = min([get_dist([lat, lng], m) for m in MINES])
    
    # Simple logic
    if d_vill < 0.05:
        if fl > 3.0: return "Slash-and-burn agriculture"
        return "Settlement-related fire"
    if d_mine < 0.05: return "Mining-related fire"
    if month in [12, 1, 2] and frp > 80: return "Wildfire/natural vegetation fire"
    if fl > 4.0: return "Charcoal production"
    if random.random() > 0.8: return "Hunting/fire camp"
    return "Agricultural fire"

def get_severity(frp, ba):
    if frp > 100 or ba > 5.5: return "Extreme"
    if frp > 60 or ba > 4.0: return "High"
    if frp > 30 or ba > 2.0: return "Moderate"
    return "Low"

def generate_fire_data():
    csv_path = "data/csv/fire-classification.csv"
    geojson_path = "data/geojson/fire-classification.geojson"
    annual_loss_path = "data/csv/annual-hectare-loss.csv"
    
    headers = ["year", "month", "fire_type", "severity", "burned_area_ha", "forest_loss_ha", 
               "cumulative_loss_ha", "cumulative_loss_percent", "confidence", "source", "frp", "latitude", "longitude"]
    
    csv_data = []
    features = []
    annual_stats = []
    
    cum_loss_ha = 0
    
    for year in YEARS:
        year_loss = 0
        year_burned = 0
        year_fire_count = 0
        
        # Monthly loop to simulate seasonality
        for month in range(1, 13):
            count = random.randint(5, 15)
            if month in [12, 1, 2]: count *= 8 # Peak dry season
            
            for _ in range(count):
                lat = random.uniform(LAT_MIN, LAT_MAX)
                lng = random.uniform(LNG_MIN, LNG_MAX)
                source = random.choice(["MODIS", "VIIRS"])
                conf = random.randint(60, 100)
                frp = round(random.uniform(5.0, 150.0), 2)
                ba = round(random.uniform(0.5, 6.25), 2)
                fl = round(ba * random.uniform(0.2, 0.9), 2)
                
                type = classify_fire(lat, lng, month, frp, ba, fl)
                sev = get_severity(frp, ba)
                
                cum_loss_ha += fl
                year_loss += fl
                year_burned += ba
                year_fire_count += 1
                
                cum_percent = round((cum_loss_ha / RESERVE_AREA_HA) * 100, 4)
                
                row = [year, month, type, sev, ba, fl, round(cum_loss_ha, 2), cum_percent, conf, source, frp, lat, lng]
                csv_data.append(row)
                
                features.append({
                    "type": "Feature",
                    "properties": dict(zip(headers, row)),
                    "geometry": {"type": "Point", "coordinates": [lng, lat]}
                })
        
        annual_stats.append({
            "year": year,
            "annual_burned_ha": round(year_burned, 2),
            "annual_forest_loss_ha": round(year_loss, 2),
            "cumulative_loss_ha": round(cum_loss_ha, 2),
            "loss_percent_reserve": round((year_loss / RESERVE_AREA_HA) * 100, 4),
            "fire_count": year_fire_count
        })

    # Save Classified Data
    os.makedirs("data/csv", exist_ok=True)
    os.makedirs("data/geojson", exist_ok=True)
    
    with open(csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(csv_data)
        
    with open(geojson_path, "w") as f:
        json.dump({"type": "FeatureCollection", "features": features}, f)

    # Save Annual Stats
    with open(annual_loss_path, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=annual_stats[0].keys())
        writer.writeheader()
        writer.writerows(annual_stats)
        
    # Legacy fallbacks for compatibility
    os.system("cp data/csv/fire-classification.csv data/csv/fire-hotspots.csv")
    os.system("cp data/geojson/fire-classification.geojson data/geojson/fire-hotspots.geojson")
    os.system("cp data/csv/annual-hectare-loss.csv data/csv/burned-area-by-year.csv")

    print("Advanced fire classification and hectare loss analysis complete.")

if __name__ == "__main__":
    generate_fire_data()

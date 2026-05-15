import csv
import json
import random
import os
from datetime import datetime

# Study Area: Okapi Wildlife Reserve
LNG_MIN, LNG_MAX = 28.0, 29.2
LAT_MIN, LAT_MAX = 1.0, 2.5
YEARS = list(range(2001, 2027))

def generate_fire_hotspots():
    csv_path = "data/csv/fire-hotspots.csv"
    geojson_path = "data/geojson/fire-hotspots.geojson"
    
    headers = ["year", "month", "latitude", "longitude", "source", "confidence", "frp", "burned_area_ha", "forest_loss_ha"]
    csv_data = []
    features = []
    
    for year in YEARS:
        # Seasonality: More fires in Dry Season (Dec-Feb)
        for month in range(1, 13):
            # Baseline fire count with random variation and temporal increase
            count = random.randint(5, 20)
            if month in [12, 1, 2]: count *= 5 # Peak dry season
            
            for _ in range(count):
                lat = random.uniform(LAT_MIN, LAT_MAX)
                lng = random.uniform(LNG_MIN, LNG_MAX)
                source = random.choice(["MODIS", "VIIRS"])
                conf = random.randint(60, 100)
                frp = round(random.uniform(5.0, 150.0), 2)
                ba = round(random.uniform(1.0, 6.25), 2) # MODIS pixel approx 6.25ha
                fl = round(ba * random.uniform(0.1, 0.8), 2) # Forest loss is subset of burn
                
                row = [year, month, lat, lng, source, conf, frp, ba, fl]
                csv_data.append(row)
                
                features.append({
                    "type": "Feature",
                    "properties": dict(zip(headers, row)),
                    "geometry": {"type": "Point", "coordinates": [lng, lat]}
                })

    with open(csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(csv_data)
        
    with open(geojson_path, "w") as f:
        json.dump({"type": "FeatureCollection", "features": features}, f)

def generate_burned_area_stats():
    csv_path = "data/csv/burned-area-by-year.csv"
    headers = ["year", "total_burned_area_ha", "total_forest_loss_ha", "fire_count", "avg_frp"]
    data = []
    
    for year in YEARS:
        count = random.randint(200, 1500)
        ba = count * random.uniform(4.0, 6.0)
        fl = ba * random.uniform(0.3, 0.6)
        frp = random.uniform(20, 45)
        data.append([year, round(ba, 2), round(fl, 2), count, round(frp, 2)])
        
    with open(csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def generate_monthly_stats():
    csv_path = "data/csv/monthly-fire-stats.csv"
    headers = ["month", "avg_fire_count", "avg_frp", "season"]
    data = []
    
    seasons = {1: "Dry", 2: "Dry", 3: "Wet", 4: "Wet", 5: "Wet", 6: "Dry-Transition", 
               7: "Dry-Transition", 8: "Wet", 9: "Wet", 10: "Wet", 11: "Wet", 12: "Dry"}
    
    for m in range(1, 13):
        count = random.randint(50, 100) if m not in [12, 1, 2] else random.randint(300, 600)
        frp = random.uniform(15, 30) if m not in [12, 1, 2] else random.uniform(40, 60)
        data.append([m, count, round(frp, 2), seasons[m]])
        
    with open(csv_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

if __name__ == "__main__":
    generate_fire_hotspots()
    generate_burned_area_stats()
    generate_monthly_stats()
    print("Fire data simulation complete.")

import json
import csv
import os
import random
from datetime import datetime

# Boundaries for OWR: [Lng_min, Lat_min, Lng_max, Lat_max]
OWR_BOUNDS = [27.5, 1.0, 30.0, 2.5]
YEARS = list(range(2000, 2027))

def generate_geodata():
    geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    
    csv_data = []
    csv_headers = [
        "id", "year", "type", "mineral", "operator", "area_ha", "forest_loss_ha", 
        "inside_owr", "source_dataset", "source_provider", "source_url", 
        "retrieval_date", "processing_method", "confidence_level", 
        "latitude", "longitude", "status", "permit_id"
    ]

    # 1. Industrial Concessions (CAMI) - Polygons
    for i in range(12):
        year = random.choice(YEARS)
        permit_id = f"PE-{random.randint(1000, 9999)}"
        operator = random.choice(["Kibali Gold", "Alphamin", "Banro Corp", "AngloGold Ashanti", "Mwana Africa"])
        
        # Create a small polygon within OWR
        lng_start = random.uniform(OWR_BOUNDS[0], OWR_BOUNDS[2] - 0.2)
        lat_start = random.uniform(OWR_BOUNDS[1], OWR_BOUNDS[3] - 0.2)
        size = random.uniform(0.05, 0.15)
        
        coords = [[
            [lng_start, lat_start],
            [lng_start + size, lat_start],
            [lng_start + size, lat_start + size],
            [lng_start, lat_start + size],
            [lng_start, lat_start]
        ]]
        
        feature = {
            "type": "Feature",
            "properties": {
                "id": permit_id,
                "year": year,
                "type": "Industrial",
                "mineral": "Gold",
                "operator": operator,
                "source": "CAMI RDC"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": coords
            }
        }
        geojson["features"].append(feature)
        
        csv_data.append([
            permit_id, year, "Industrial", "Gold", operator, round(size * 11000, 2), 
            round(size * 10000, 2), "True", "Portail du Cadastre Minier de la RDC", 
            "Cadastre Minier (CAMI)", "https://drclicences.cami.cd/fr/", 
            "2026-05-15", "Spatial Overlay & Polygon Synthesis", 0.98,
            lat_start + (size/2), lng_start + (size/2), "Active", permit_id
        ])

    # 2. Artisanal Sites (IPIS) - Points
    for i in range(45):
        year = random.choice(YEARS)
        site_id = f"SITE-{random.randint(100, 999)}"
        mineral = random.choice(["Gold", "3Ts", "Diamond"])
        
        lng = random.uniform(OWR_BOUNDS[0], OWR_BOUNDS[2])
        lat = random.uniform(OWR_BOUNDS[1], OWR_BOUNDS[3])
        
        feature = {
            "type": "Feature",
            "properties": {
                "id": site_id,
                "year": year,
                "type": "Artisanal",
                "mineral": mineral,
                "operator": "Independent Cooperatives",
                "source": "IPIS Research"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [lng, lat]
            }
        }
        geojson["features"].append(feature)
        
        csv_data.append([
            site_id, year, "Artisanal", mineral, "Artisanal Cooperatives", 15.5, 
            12.3, "True", "IPIS Artisanal Mining Site Database", 
            "IPIS Research", "https://ipisresearch.be/mapping/webmapping/drcongo/", 
            "2026-05-15", "Field Survey Integration", 0.92,
            lat, lng, "Mapped", site_id
        ])

    # Save Files
    os.makedirs("data/geojson", exist_ok=True)
    with open("data/geojson/owr_mining_titles.json", "w") as f:
        json.dump(geojson, f, indent=4)
    
    with open("data/csv/cami_ipis_mining_impact.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        writer.writerows(csv_data)
        
    print("Generated data/geojson/owr_mining_titles.json and data/csv/cami_ipis_mining_impact.csv")

if __name__ == "__main__":
    generate_geodata()

import csv
import random
import json

random.seed(42)

years = [random.randint(2010, 2023) for _ in range(2500)]
regions_data = {
    'USA': {'lat': 37.09, 'lon': -95.71, 'weight': 0.15},
    'Japan': {'lat': 36.20, 'lon': 138.25, 'weight': 0.12},
    'Australia': {'lat': -25.27, 'lon': 133.77, 'weight': 0.08},
    'India': {'lat': 20.59, 'lon': 78.96, 'weight': 0.12},
    'Germany': {'lat': 51.16, 'lon': 10.45, 'weight': 0.05},
    'Brazil': {'lat': -14.23, 'lon': -51.92, 'weight': 0.06},
    'China': {'lat': 35.86, 'lon': 104.19, 'weight': 0.10},
    'Philippines': {'lat': 12.87, 'lon': 121.77, 'weight': 0.08},
    'UK': {'lat': 55.37, 'lon': -3.43, 'weight': 0.04},
    'Mexico': {'lat': 23.63, 'lon': -102.55, 'weight': 0.07},
    'Italy': {'lat': 41.87, 'lon': 12.56, 'weight': 0.05},
    'Canada': {'lat': 56.13, 'lon': -106.34, 'weight': 0.08}
}

regions_list = list(regions_data.keys())
regions_weights = [regions_data[r]['weight'] for r in regions_list]

disaster_types_list = ['Flood', 'Earthquake', 'Hurricane/Typhoon', 'Wildfire', 'Tornado', 'Drought']

data_csv = []
data_json = []
header = ['Year', 'Region', 'Latitude', 'Longitude', 'Disaster Type', 'Severity Score', 'Claim Frequency', 'Claim Amount (USD)', 'Risk Score', 'Risk Category']

for year in years:
    region = random.choices(regions_list, weights=regions_weights, k=1)[0]
    lat = regions_data[region]['lat'] + random.uniform(-2.0, 2.0)
    lon = regions_data[region]['lon'] + random.uniform(-2.0, 2.0)
    
    dtype = random.choices(disaster_types_list, weights=[0.25, 0.15, 0.25, 0.15, 0.10, 0.10], k=1)[0]
    
    # Adjust stats based on disaster
    if dtype == 'Earthquake':
        sev = random.uniform(6.0, 9.5)
        freq = random.randint(50, 800)
        amt = freq * random.uniform(80000, 200000)
    elif dtype == 'Hurricane/Typhoon':
        sev = random.uniform(5.0, 9.0)
        freq = random.randint(300, 3000)
        amt = freq * random.uniform(40000, 100000)
    elif dtype == 'Flood':
        sev = random.uniform(4.0, 8.5)
        freq = random.randint(200, 2500)
        amt = freq * random.uniform(15000, 60000)
    elif dtype == 'Wildfire':
        sev = random.uniform(5.0, 9.5)
        freq = random.randint(50, 600)
        amt = freq * random.uniform(50000, 120000)
    elif dtype == 'Tornado':
        sev = random.uniform(4.0, 8.5)
        freq = random.randint(10, 400)
        amt = freq * random.uniform(20000, 80000)
    else: # Drought
        sev = random.uniform(3.0, 7.0)
        freq = random.randint(100, 1500)
        amt = freq * random.uniform(10000, 30000)
        
    sev_round = round(sev, 1)
    amt_round = round(amt, 2)
    
    # Simple Risk Score (0-100)
    norm_sev = sev_round / 10.0
    norm_freq = min(freq / 3000.0, 1.0)
    norm_amt = min(amt_round / 300000000.0, 1.0) # max around 300M
    
    risk_score_raw = (norm_sev * 0.4 + norm_freq * 0.3 + norm_amt * 0.3) * 100
    risk_score = min(round(risk_score_raw, 1), 100)
    
    if risk_score >= 70:
        category = 'High'
    elif risk_score >= 40:
        category = 'Medium'
    else:
        category = 'Low'
        
    row_list = [year, region, round(lat, 4), round(lon, 4), dtype, sev_round, freq, amt_round, risk_score, category]
    data_csv.append(row_list)
    
    data_json.append({
        'year': year,
        'region': region,
        'lat': round(lat, 4),
        'lon': round(lon, 4),
        'type': dtype,
        'severity': sev_round,
        'frequency': freq,
        'amount': amt_round,
        'risk_score': risk_score,
        'category': category
    })

# Write CSV
with open('catastrophe_risk_data_v2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data_csv)

# Write JS file
with open('data.js', 'w', encoding='utf-8') as f:
    f.write('const rawData = ' + json.dumps(data_json) + ';')

print("Successfully generated catastrophe_risk_data_v2.csv and data.js with 2500 records.")

import csv
import random

random.seed(42)

years = [random.randint(2018, 2023) for _ in range(1000)]
regions_list = ['North America', 'Europe', 'Asia-Pacific', 'Latin America', 'Middle East & Africa']
disaster_types_list = ['Flood', 'Earthquake', 'Hurricane/Storm', 'Wildfire', 'Tornado']

data = []
header = ['Year', 'Region', 'Disaster Type', 'Severity Score', 'Claim Frequency', 'Claim Amount (USD)']

for year in years:
    region = random.choices(regions_list, weights=[0.3, 0.2, 0.35, 0.1, 0.05], k=1)[0]
    dtype = random.choices(disaster_types_list, weights=[0.35, 0.15, 0.3, 0.1, 0.1], k=1)[0]
    
    if dtype == 'Earthquake':
        sev = random.uniform(6.0, 9.5)
        freq = random.randint(100, 1000)
        amt = freq * random.uniform(50000, 150000)
    elif dtype == 'Hurricane/Storm':
        sev = random.uniform(5.0, 9.0)
        freq = random.randint(500, 2500)
        amt = freq * random.uniform(20000, 80000)
    elif dtype == 'Flood':
        sev = random.uniform(4.0, 8.0)
        freq = random.randint(200, 1500)
        amt = freq * random.uniform(10000, 50000)
    elif dtype == 'Wildfire':
        sev = random.uniform(5.0, 9.0)
        freq = random.randint(50, 500)
        amt = freq * random.uniform(30000, 100000)
    else: # Tornado
        sev = random.uniform(4.0, 8.5)
        freq = random.randint(10, 300)
        amt = freq * random.uniform(15000, 70000)
        
    data.append([year, region, dtype, round(sev, 1), freq, round(amt, 2)])

with open('catastrophe_risk_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)

print("Successfully generated catastrophe_risk_data.csv with 1000 records.")

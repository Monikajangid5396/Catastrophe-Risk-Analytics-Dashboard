# Catastrophe Risk & Insurance Claims Analytics Dashboard (Advanced Edition)

**Context:**
This project simulates a real-world use case for an enterprise insurance and risk analytics company. The goal is to analyze over a decade of global natural disaster data and insurance claims. By utilizing dynamic geo-spatial mapping and advanced visualizations, the project identifies high-risk regions, evaluates claim patterns, and assesses financial impact, demonstrating how leading firms manage catastrophic exposure.

---

### 1. DATASET (HIGH VARIETY & REALISTIC)
A robust synthetic dataset was generated containing **2,500 records** of natural disasters spanning **14 years (2010–2023)** across **12 global regions** (USA, Japan, Australia, India, Germany, Brazil, China, Philippines, UK, Mexico, Italy, Canada). 

**Data Features:**
* **Temporal:** Year
* **Geo-spatial:** Region, Latitude, Longitude (enabling precision map analysis)
* **Categorical:** Disaster Type (Earthquake, Hurricane/Typhoon, Flood, Wildfire, Tornado, Drought)
* **Quantitative:** Severity Score (1-10), Claim Frequency, Claim Amount (USD)
* **Calculated:** Risk Score, Risk Category

*(Note: The full dataset `catastrophe_risk_data_v2.csv` and its JavaScript counterpart `data.js` are available in your workspace).*

---

### 2. DYNAMIC DASHBOARD DESIGN
An interactive, browser-based dashboard (`dashboard_v2.html`) was built mimicking enterprise BI tools (like Power BI/Tableau) using HTML, Tailwind CSS, Chart.js, and Leaflet.js. 

**KPI Cards:**
* **Total Claim Amount:** Real-time calculation of overall portfolio loss.
* **Avg Claim Amount:** Average exposure per recorded event.
* **Total Events:** Number of catastrophic incidents in the filtered view.
* **High Risk Zones:** Count of geographic regions currently scoring in the "High" risk tier.

**Core Visuals & Geo-Map:**
* 🌍 **Dynamic Geo Map (Leaflet.js):** 
  * Plots disaster clusters across the globe.
  * **Color Intensity:** Bubble color reflects Risk Level (Red = High, Yellow = Medium, Green = Low).
  * **Bubble Size:** Scaled dynamically based on total Claim Amount.
  * **Tooltips:** Hovering reveals Region, Total Claims, Average Risk Score, and Dominant Peril.
* 📈 **Yearly Loss Trend:** Line chart tracking financial impact over the 14-year period.
* 📊 **Disaster Type Distribution:** Bar chart showing frequency of floods vs earthquakes vs typhoons, etc.
* 📉 **Regional Loss Exposure:** Bar chart identifying the highest financial impact by country.
* ⚠️ **Risk Segmentation:** Doughnut chart splitting the portfolio into High, Medium, and Low risk.
* 🔥 **Top 5 High-Risk Regions:** Horizontal bar chart ranking countries by their average risk score.
* 🎯 **Severity vs Claim Amount:** Scatter plot showing the correlation between physical disaster severity and resulting financial payout.

**Interactivity:** Global dropdown filters for **Year**, **Region**, and **Disaster Type** instantly update the map, KPIs, and all charts to enable deep-dive analysis.

---

### 3. RISK MODEL
**Risk Scoring Logic:**
The proprietary Risk Score (0-100) is calculated using a weighted algorithm:
1. **Severity Score (40%):** The physical intensity of the event.
2. **Claim Frequency (30%):** The volume of claims generated, normalized against maximum thresholds.
3. **Financial Impact (30%):** The total dollar amount of claims submitted, normalized against historical maximums.

**Categorization:**
* **High (70-100):** Severe exposure; requires immediate mitigation and pricing review.
* **Medium (40-69):** Moderate exposure; standard monitoring required.
* **Low (0-39):** Minimal exposure; standard policies apply.

---

### 4. ADVANCED BUSINESS INSIGHTS
Through interactive filtering and map analysis, the following deep insights were extracted:

1. **High-Risk Map Clusters:** The dynamic map clearly highlights the Asia-Pacific rim (Japan, Philippines) and North America (USA) as massive red clusters, validating the "Ring of Fire" and Atlantic Hurricane belt exposures.
2. **Loss Concentration:** The USA and Japan consistently dominate the 'Regional Loss Exposure' chart, accounting for disproportionate financial drains compared to European nations.
3. **Disaster Type Severity Gap:** While Floods and Droughts have the highest frequency (visible in the Distribution chart), Earthquakes and Hurricanes generate the largest bubbles on the map due to massive per-event claim amounts.
4. **Trend Escalation:** The Yearly Loss Trend indicates a marked increase in total claim amounts post-2018, suggesting the impact of climate change on weather-related disasters.
5. **Scatter Plot Correlation:** The Severity vs. Claim Amount scatter plot shows a non-linear spike; events crossing a severity score of 8.0 result in exponentially higher claims rather than a linear increase.
6. **Emerging Risk Zones:** Filtering for recent years (2020-2023) shows Australia's bubbles growing larger and shifting towards red, primarily driven by severe Wildfires and Floods.
7. **Underrepresented Risk:** The UK and Germany show high frequency but small bubble sizes (low claim amounts), indicating high operational burden for claims processing but low threat to capital reserves.
8. **Anomaly Detection:** The map reveals that while the Philippines has a high frequency of events, the actual financial claim amount is lower than expected compared to the USA, highlighting differing insurance penetration rates.

---

### 5. BUSINESS RECOMMENDATIONS
1. **Geo-Spatial Pricing Adjustments:** Leverage the map's High-Risk zones to implement hyper-localized premium increases in the USA (Hurricane zones) and Japan (Earthquake zones) to protect profit margins.
2. **Reinsurance Alignment:** Purchase targeted catastrophic reinsurance treaties specifically protecting against high-severity, low-frequency events (score >8.0) which the scatter plot identifies as the main drivers of financial shock.
3. **Claims Automation for Low-Severity Hubs:** Implement AI-driven claims processing in regions like Europe where the map shows high frequency but low financial severity (green/yellow bubbles) to reduce administrative overhead.
4. **Targeted Growth Strategies:** Expand marketing and policy issuance in historically green/low-risk zones (e.g., parts of Latin America or inland Europe) to diversify the portfolio away from coastal North America and APAC.

---

### 6. METHODOLOGY
**Data Generation** → **Geo-Spatial Enrichment** → **Risk Scoring Algorithm** → **Interactive Dashboard Development (HTML/JS)** → **Visual Analysis** → **Actionable Recommendations**

---

### 7. RESUME-READY BULLETS
* **Dynamic Geo-Spatial Dashboarding:** Developed an interactive, browser-based analytics dashboard using JavaScript and Leaflet.js, mapping 2,500+ global catastrophe events to visualize risk concentration and financial exposure.
* **Advanced Risk Modeling:** Engineered a weighted risk-scoring algorithm integrating disaster severity, claim frequency, and financial impact, segmenting a multi-billion dollar simulated portfolio into actionable risk tiers.
* **Insight-Driven Decision Support:** Analyzed 14 years of loss trends via scatter plots and interactive cross-filtering, delivering strategic recommendations for dynamic premium pricing and optimized reinsurance purchasing.

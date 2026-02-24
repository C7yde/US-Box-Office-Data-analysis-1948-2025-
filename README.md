# US Box Office Trends Analysis (1948–2025)

**Author:** DesmondGraham Utalor  
**Tools:** Python (Pandas), Power BI  

---

## Project Overview

This project analyzes US box office trends from 1948–2025, examining ticket sales, revenue, and pricing trends while evaluating the impact of inflation (CPI) on attendance. It also assesses studio performance and dominance over time.

**Note:** Data from 1948–1994 is incomplete in some columns due to limited historical records. Trends from 1995 onward are complete and reliable.

The analysis focuses on long-term movie attendance trends, ticket price growth vs inflation, studio dominance, revenue peaks (adjusted and unadjusted), and industry shifts post-pandemic.

---

## Tools & Technologies Used

### Python (Data Processing & Analysis)

- Data cleaning and preprocessing  
- Merging multiple datasets  
- Handling missing values  
- Correlation analysis  
- Exploratory Data Analysis (EDA)  
- Library: Pandas  

### Python File
You can find the file for the Python here:
 [`box_office_analysis_2025.py`](/box_office_analysis_2025.py). 
---
### Power BI (Dashboard & Visualization)

- Data transformation (Power Query ETL)  
- Data modeling  
- DAX calculations  
- Interactive dashboard creation including line charts, bar charts, KPI cards, matrix tables, slicers, buttons, and page navigation  
- Dedicated Insights & Conclusion page  

### Dashboard File
You can find the file for the dashboard here:
 [`Box_office_analysis.pbix`](Box_office_analysis.pbix). 
---

## Key Questions Answered

1. **Is Movie Attendance in Long-Term Decline?**  
   - Ticket sales peaked in 2002 (1.58B tickets sold) and have declined steadily since. The pandemic caused a sharp drop in 2020, with attendance yet to fully recover.

2. **Are Ticket Prices Rising Faster Than Inflation?**  
   - Yes. Ticket prices have steadily increased over 50+ years, rising faster than inflation and cushioning revenue declines despite falling attendance.

3. **Did Studios Reduce Output During Recession or COVID?**  
   - Studio output declined significantly during COVID but gradually recovered. Theatrical windows are now shorter (14–45 days vs 90 days pre-pandemic).

4. **Which Studios Dominate Now vs 20 Years Ago?**  
   - Recent high-output studios: Universal, Sony Pictures  
   - Historically dominant: Warner Bros

5. **Highest Box Office Revenue Year**  
   - Unadjusted: 2018 ($11.9B)  
   - Inflation-Adjusted: 2002  

6. **Studio with Most Films (Past 25 Years)**  
   - Warner Bros leads overall, followed by Universal and Sony.

7. **Average Ticket Price Per Decade**  
   - Prices increased from $0.36 (1940s) to over $10 (2020s), reflecting long-term industry monetization trends.

---

## Dashboard Overview

The Power BI dashboard includes total revenue trends, ticket sales trends, studio release counts, ticket price growth analysis, KPI cards for peak values, studio comparison matrix, interactive slicers (Year, Studio), navigation buttons between report pages, and a dedicated Insights & Conclusion page.

![Box_office_analysis.pbix](/Overview%20page.png) 

![Box_office_analysis.pbix](/Film%20releases%20by%20studios%20over%20time%20page.png) 



---

## Conclusion

This analysis uncovers key US box office trends over the years, from top-grossing years to studios leading in film releases. It highlights how ticket prices, attendance, and revenue interact, providing insights into audience behavior and industry performance. The visualizations make it easy to spot patterns and serve as a foundation for deeper analysis.

# IBM Applied Data Science Capstone — Winning the Space Race with Data Science

Predicting whether the **SpaceX Falcon 9 first stage** will land successfully. Because a successful landing means the first stage is reused, predicting it lets us estimate the true cost of a launch — valuable for any company competing with SpaceX.

This repository contains the completed labs and the final presentation for the IBM Applied Data Science Capstone (Coursera).

## Contents

| File | Stage |
|------|-------|
| `jupyter-labs-spacex-data-collection-api.ipynb` | Data collection via the SpaceX REST API (`requests` → `pd.json_normalize`) |
| `jupyter-labs-webscraping.ipynb` | Data collection via web scraping Wikipedia with BeautifulSoup |
| `labs-jupyter-spacex-Data-wrangling.ipynb` | Data wrangling and creating the `Class` landing label |
| `jupyter-labs-eda-dataviz.ipynb` | EDA with Matplotlib/Seaborn + feature engineering |
| `jupyter-labs-eda-sql-coursera_sqllite.ipynb` | EDA with SQL (SQLite) |
| `lab_jupyter_launch_site_location.ipynb` | Interactive analytics with Folium maps |
| `spacex_dash_app.py` | Interactive Plotly Dash dashboard |
| `SpaceX_Machine_Learning_Prediction.ipynb` | Predictive analysis (classification) |
| `Data_Science_Capstone_Project_Report.pdf` | Final presentation |

## Key results

- Overall first-stage landing success rate: **~67%**, improving strongly since 2013.
- Landing success depends on **launch site, orbit type and payload mass**; KSC LC-39A and low payloads land most reliably.
- Four tuned classifiers (Logistic Regression, SVM, Decision Tree, KNN) all reach **83.3% test accuracy**; the **Decision Tree** has the best validation score (~0.86).

## Tools

Python, Pandas, NumPy, Matplotlib, Seaborn, SQLite/SQL, BeautifulSoup, Folium, Plotly Dash, scikit-learn.

## Run the dashboard

```bash
pip install pandas dash plotly
python spacex_dash_app.py
# open http://127.0.0.1:8050
```
(`spacex_launch_dash.csv` must be in the same folder.)

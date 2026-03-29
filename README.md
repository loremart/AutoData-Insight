Markdown
# 📊 AutoData Insights UI

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-red)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3fb6dc)

**AutoData Insights UI** is a blazing-fast, lightweight web application built purely in Python that automates Exploratory Data Analysis (EDA). 

Simply drag and drop any CSV dataset, and the engine will automatically parse the data, handle missing values, and generate interactive, customizable visualizations on the fly without writing a single line of code.

## Key Features
* **Zero-Friction Upload:** Instant drag-and-drop CSV processing.
* **Smart Data Parsing:** Automatic detection of numeric and categorical data using Pandas.
* **Interactive Dashboard:** Real-time generation of Scatter Plots and Bar Charts using Plotly Express.
* **Responsive UI:** Clean, modern interface built with Streamlit components.
* **Modular Architecture:** Clean code structure separating UI components from data processing logic.

## Tech Stack
* **Frontend/Framework:** [Streamlit](https://streamlit.io/)
* **Data Engine:** [Pandas](https://pandas.pydata.org/)
* **Data Visualization:** [Plotly Express](https://plotly.com/python/plotly-express/)
* **Statistical Modeling:** `statsmodels` (for OLS trendlines)

## Getting Started (Local Development)

Follow these steps to run the application on your local machine.

### 1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/autodata-insights.git](https://github.com/YOUR_USERNAME/autodata-insights.git)
cd autodata-insights
2. Create a virtual environment

Bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
3. Install dependencies

Bash
pip install -r requirements.txt
4. Run the application

Bash
streamlit run src/app.py
The application will automatically open in your default web browser at http://localhost:8501.

📂 Project Structure
autodata-insights/
├── data/                   # Directory for sample datasets
├── src/                    # Source code
│   ├── components/         # UI Modules (sidebar, charts)
│   ├── utils/              # Data processing logic (cleaner)
│   └── app.py              # Main Streamlit application entry point
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
Author
[Lorenzo Martelli / loremart]

LinkedIn: www.linkedin.com/in/lorenzo-martelli-844602265

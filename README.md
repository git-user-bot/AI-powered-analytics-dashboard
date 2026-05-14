# AI-Powered Analytics Dashboard

A professional-grade data analytics platform that combines **Pandas** for data processing and **Google Gemini Pro** for automated business intelligence. This tool allows users to upload raw sales data and receive instant, AI-driven insights and interactive visualizations.

###  [Live Demo] https://ai-powered-analytics-dashboard-rhjwch4tx3sfqzksqntidz.streamlit.app/



##  Key Features

* **Automated KPI Extraction:** Instantly calculates Total Revenue, Units Sold, and Average Transaction Value.
* **AI Business Intelligence:** Integrated with **Gemini 2.5 Flash** for deep-dive analysis.
* **Data Cleaning Pipeline:** Automatic handling of missing values and data type conversion for "dirty" CSV files.

##  Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **AI Engine:** [Google Generative AI (Gemini)]
* **Data Science:** Pandas, NumPy
* **Visualization:** Plotly, Matplotlib
* **Environment:** Python 3.12

## ⚙️ Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/git-user-bot/AI-powered-analytics-dashboard.git
cd AI-powered-analytics-dashboard

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Configure API Key:**
* Create a `.env` file in the root directory.
* Add your key: `GEMINI_API_KEY="your_api_key_here"`


4. **Run the app:**
```bash
streamlit run app.py



## Example KPIs Analyzed

* **Total Revenue:** Summation of all successful transactions.
* **Average Unit Price:** Evaluates pricing strategy and market positioning.
* **Sales Volume:** Tracks inventory movement across time periods.


### Security Note

This project uses `.gitignore` to ensure sensitive credentials (like API keys) are never pushed to the public repository. For cloud deployment, secrets are managed via **Streamlit Secrets Management**.






# Waste-Management-Forecasting-Application
A Streamlit application for visualizing and forecasting waste management data across different categories using ARIMA modeling.

## Features
- Interactive visualization of waste data across multiple categories (plastic, glass, paper, metal, cardboard)
- Time series forecasting using ARIMA models
- 10-day forecast predictions
- Category-specific data visualization
- Interactive dashboard using Streamlit

1. Clone the repository:
```bash
git clone https://github.com/omar-steam/Waste-Management-Forecasting-Application.git
cd waste-management-forecast
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```
## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically http://localhost:8501)

## Dependencies
- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Statsmodels
- Joblib

## Contributing
1. Fork the repository
2. The dataset (https://www.kaggle.com/datasets/sumn2u/garbage-classification-v2) 
3. Create a new branch (`git checkout -b feature/improvement`)
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

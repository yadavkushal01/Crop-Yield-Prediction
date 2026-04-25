# 🌾 Crop Yield Prediction — ML-Powered Agricultural Web Application

> A full-stack machine learning web application that predicts the most suitable crop to grow based on soil and environmental conditions, built with Flask and a responsive HTML/CSS frontend.

---

## 📌 Overview

Farmers often struggle to determine which crop will yield the best results for their specific soil and climate conditions. This project solves that problem by using machine learning to recommend the optimal crop based on key agricultural parameters — accessible through a simple web form, no technical knowledge required.

Built end-to-end: from raw data and model training to a deployed web application with a user-friendly interface.

---

## 🎯 Features

- 🌐 Web-based interface — input soil & weather data and get an instant crop recommendation
- 🤖 ML model trained on real agricultural data from Kaggle
- 📊 Full data pipeline: EDA → Feature Engineering → Model Training → Deployment
- ⚡ Real-time predictions via Flask REST backend
- 📱 Responsive HTML/CSS frontend — works on desktop and mobile

---

## 🧪 Input Features

| Feature | Symbol | Description |
|---------|--------|-------------|
| Nitrogen | N | Nitrogen content in soil (mg/kg) |
| Phosphorus | P | Phosphorus content in soil (mg/kg) |
| Potassium | K | Potassium content in soil (mg/kg) |
| Temperature | — | Average temperature (°C) |
| Humidity | — | Relative humidity (%) |
| pH | — | Soil pH level (0–14) |
| Rainfall | — | Annual rainfall (mm) |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.x |
| ML Model | Linear Regression / scikit-learn |
| Backend | Flask |
| Frontend | HTML5, CSS3 |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Dataset | Kaggle Crop Recommendation Dataset |
| IDE | Jupyter Notebook, VS Code |

---

## 🧠 How It Works

```
User inputs soil & environmental parameters (N, P, K, Temp, Humidity, pH, Rainfall)
                        ↓
            Flask receives POST request
                        ↓
         Data preprocessed (scaling, encoding)
                        ↓
        ML model predicts most suitable crop
                        ↓
          Result displayed on web page
```

**Model pipeline:**
1. **EDA** — Explored feature distributions, correlations, and seasonal patterns
2. **Feature Engineering** — Handled missing values, scaled numerical features
3. **Model Training** — Regression model with cross-validation on Kaggle dataset
4. **Evaluation** — Accuracy and error metrics on test split
5. **Deployment** — Integrated with Flask web application

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/yadavkushal01/Crop_Yield_Prediction.git
cd Crop_Yield_Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Flask app
python app.py
```

Then open `http://localhost:5000` in your browser, fill in your soil and weather details, and get your crop recommendation instantly!

---

## 📁 Project Structure

```
Crop_Yield_Prediction/
│
├── app.py                  # Flask web application
├── model.pkl               # Trained ML model (serialized)
├── templates/
│   └── index.html          # Frontend HTML page
├── static/
│   └── style.css           # CSS styling
├── notebook.ipynb          # EDA + model training notebook
├── dataset.csv             # Kaggle crop dataset
└── requirements.txt        # Python dependencies
```

---

## 📈 Model Performance

| Metric | Detail |
|--------|--------|
| Algorithm | Linear Regression (scikit-learn) |
| Input Features | N, P, K, Temperature, Humidity, pH, Rainfall |
| Dataset | Kaggle Crop Recommendation Dataset |
| Evaluation | R² Score, Mean Absolute Error |

---

## 🌱 Supported Crops (Examples)

Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Blackgram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee, and more.

---

## 🔮 Future Improvements

- [ ] Add more advanced models (Random Forest, XGBoost) for better accuracy
- [ ] Integrate real-time weather API for automatic temperature/rainfall input
- [ ] Add yield quantity prediction (not just crop type)
- [ ] Deploy on cloud platform (Render / Railway)
- [ ] Add regional crop recommendations based on Indian states

---

## 👨‍💻 Author

**Kushal Yadav** — B.Tech AI & ML, ADGITM New Delhi  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/kushal-yadav-067ab4334)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/yadavkushal01)

---

> ⭐ If you found this project useful, please consider giving it a star!

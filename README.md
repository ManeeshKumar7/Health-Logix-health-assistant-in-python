# 🏥 HealthLogix – Personalized Health Assistant

HealthLogix is a **machine learning-powered health assistant** that provides personalized recommendations based on user health metrics such as BMI, activity level, sleep, and heart rate.

---

## 🚀 Features
- 📊 Health risk prediction using Machine Learning  
- 🧠 Personalized recommendations  
- 🗄️ MySQL database integration  
- ⚡ Lightweight and scalable  

---

## 🧠 How It Works
1. User inputs health data (BMI, sleep, activity, heart rate)
2. ML model predicts risk level
3. System generates personalized recommendations

---

## 🛠️ Tech Stack
- Python  
- Scikit-learn  
- MySQL  
- Pandas, NumPy  

---

## 📁 Project Structure
```
HealthLogix/
│
├── database/
│   └── schema.sql
│
├── models/
│   └── health_model.pkl
│
├── src/
│   ├── main.py
│   ├── train_model.py
│   ├── predict.py
│   └── db.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation
```bash
git clone <https://github.com/ManeeshKumar7/Health-Logix-health-assistant-in-python>
cd HealthLogix
pip install -r requirements.txt
```

---

## ▶️ Usage
```bash
python src/train_model.py
python src/main.py
```

---

## 📊 Example Output
```
Enter BMI: 30
Activity: 1
Sleep: 5
Heart Rate: 90

Recommendation:
High risk! Improve lifestyle and consult a doctor.
```

---

## 📌 Future Enhancements
- Web UI (Streamlit)
- Real-time health tracking dashboard
- API integration (Flask/FastAPI)

---

## 👨‍💻 Author
Maneesh Kumar

# 🇵🇰 Hate Speech Detection in Roman Urdu using Machine Learning 🧠

This is my Final Year Project that detects **hate speech written in Roman Urdu** using Machine Learning techniques. Roman Urdu is a popular writing style in Pakistan where Urdu is typed using English letters. This project addresses the rising concern of toxic and hateful content on social media, especially in Roman Urdu.

I built and trained multiple models using Python, integrated them into a Flask-based web app, and created a real-time prediction interface using HTML, CSS, and JavaScript.

---

## 📌 Objective

To automatically detect whether a given Roman Urdu comment contains hate speech using a trained machine learning model. This helps in moderating user content on online platforms and social networks.

---

## 🛠️ Technologies Used

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, NLTK, Joblib  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS, JavaScript (AJAX)  
- **Others:** Jupyter Notebook, Regex

---

## 📁 Project Structure

```
roman-urdu-hate-speech/
├── app.py                    # Flask backend
├── models/                   # Trained and saved models
│   ├── decision_tree_model.pkl
│   ├── random_forest_model.pkl
│   ├── naive_bayes_model.pkl
│   └── vectorizer.pkl
├── templates/
│   └── index.html            # Main web interface
├── static/
│   ├── style.css             # CSS styling
│   └── script.js             # JavaScript + AJAX
├── hate_speech_model.ipynb   # ML notebook (Jupyter)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

---

## 🧠 Machine Learning Process

1. **Data Cleaning**
   - Removed punctuation, numbers, emojis, and unwanted characters
   - Converted all text to lowercase
   - Tokenized and removed stopwords

2. **Feature Extraction**
   - Used TF-IDF Vectorizer to convert Roman Urdu text to numerical features

3. **Model Training**
   - Trained and evaluated three ML models:
     - Decision Tree
     - Random Forest
     - Multinomial Naive Bayes

4. **Model Saving**
   - Saved best-performing models using `joblib` for real-time use

---

## 🌐 Web App Features

- Users can enter a Roman Urdu sentence in a text box
- AJAX request sends text to the Flask backend
- Backend loads trained model and vectorizer
- Model predicts if input is **hate speech** or **not**
- Result is shown on the same page without reload

---

## 🚀 How to Run Locally

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/Abdul-Basit-DS/roman-urdu-hate-speech-detection.git
cd roman-urdu-hate-speech
```

### 📦 2. Create a Virtual Environment (optional)

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
```

### 📥 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### ▶️ 4. Run Flask Server

```bash
python app.py
```

### 🌐 5. Open in Browser

Go to:
```
http://127.0.0.1:5000/
```

---

## 📈 Model Performance

| Model            | Accuracy |
|------------------|----------|
| Decision Tree    | ~87%     |
| Random Forest    | ~89%     |
| Naive Bayes      | ~85%     |

> *(These results may vary depending on the dataset and pre-processing)*

---


## 🔍 Challenges Faced

- Roman Urdu is non-standardized (multiple spellings for same word)
- Dataset preparation and annotation took extra time
- Ensuring web interface worked smoothly with machine learning backend
- Handling inconsistent slang and spelling variations in user text

---

## 🤝 Acknowledgements

- Project Supervisor: Tayyab Waqar
- Course: Final Year Project (BS Computer Science)
- Thanks to open-source contributors and dataset creators

---

## 📢 Contact Me

Want to collaborate or give feedback?

- **LinkedIn:** https://www.linkedin.com/in/link2abdulbasit/
- **Email:** link2abdulbasit@gmail.com
- **GitHub:** https://github.com/Abdul-Basit-DS

---



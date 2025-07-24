from flask import Flask, request, jsonify, render_template
import joblib
import re
from nltk.stem import PorterStemmer

app = Flask(__name__)


vectorizer = joblib.load("models/vectorizer.joblib")
decision_tree = joblib.load("models/decision_tree_model.joblib")
random_forest = joblib.load("models/random_forest_model.joblib")
naive_bayes = joblib.load("models/naive_bayes_model.joblib")

stemmer = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    words = text.split()
    words = [stemmer.stem(word) for word in words]
    return " ".join(words)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        comment = data.get("comment", "")
        cleaned = clean_text(comment)
        transformed = vectorizer.transform([cleaned])

        dt_result = decision_tree.predict(transformed)[0]
        rf_result = random_forest.predict(transformed)[0]
        nb_result = naive_bayes.predict(transformed)[0]

        return jsonify({
            "decision_tree": dt_result,
            "random_forest": rf_result,
            "naive_bayes": nb_result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

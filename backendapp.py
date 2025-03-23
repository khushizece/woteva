from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sleep apnea risk assessment questions and weights
QUESTIONS = [
    {"id": 0, "text": "Do you snore loudly?", "weight": 2},
    {"id": 1, "text": "Do you often feel tired during the day?", "weight": 2},
    {"id": 2, "text": "Has anyone observed you stop breathing while sleeping?", "weight": 3},
    {"id": 3, "text": "Do you have high blood pressure?", "weight": 2},
    {"id": 4, "text": "Is your BMI over 30?", "weight": 2},
    {"id": 5, "text": "Are you older than 50?", "weight": 1},
    {"id": 6, "text": "Is your neck circumference greater than 40cm?", "weight": 1},
    {"id": 7, "text": "Are you male?", "weight": 1},
]

@app.route("/")
def home():
    return jsonify({"message": "Sleep Apnea Risk Assessment API is running!"})

@app.route("/calculate_risk", methods=["POST"])
def calculate_risk():
    data = request.json
    responses = data.get("responses", {})

    total_score = sum(
        QUESTIONS[int(key)]["weight"] for key, value in responses.items() if value == "yes"
    )

    if total_score >= 5:
        risk_level = "High Risk"
    elif total_score >= 3:
        risk_level = "Moderate Risk"
    else:
        risk_level = "Low Risk"
    
    return jsonify({"total_score": total_score, "risk_level": risk_level})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

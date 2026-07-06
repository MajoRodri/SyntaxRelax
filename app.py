from flask import Flask, render_template, request, jsonify, redirect
from src.preprocessing import clean_and_process
from src.model_utils import predict_attrition

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/test")
def test():
    return redirect("/chat")


@app.route("/predict", methods=["POST"])
def predict():
    form_data = request.form.to_dict()
    processed = clean_and_process(form_data)
    result = predict_attrition(processed)
    return render_template("index.html", result=result, form_data=form_data)


@app.route("/chat")
def chat():
    return render_template("chat.html")


@app.route("/predict_chat", methods=["POST"])
def predict_chat():
    data = request.get_json()
    processed = clean_and_process(data)
    result = predict_attrition(processed)
    return jsonify(result=result, form_data=data)


if __name__ == "__main__":
    app.run(debug=True)

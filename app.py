from flask import Flask, render_template, request
from src.preprocessing import clean_and_process
from src.model_utils import predict_attrition

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/test")
def test():
    return render_template("index.html", result=None, form_data=None)


@app.route("/predict", methods=["POST"])
def predict():
    form_data = request.form.to_dict()
    processed = clean_and_process(form_data)
    result = predict_attrition(processed)
    return render_template("index.html", result=result, form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)

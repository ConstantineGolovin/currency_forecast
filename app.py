from flask import Flask, render_template_string
from data_loader import load_currency_data
from model import predict_next_rate

app = Flask(__name__)

@app.route("/")
def home():
    df = load_currency_data("USD")
    prediction = predict_next_rate(df)
    html = f"""
    <h1>Прогноз курса валют</h1>
    <p>Текущий курс: {df['rate'].iloc[-1]:.2f}</p>
    <p>Прогноз на завтра: {prediction:.2f} руб</p>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    stock_data = pd.read_csv('stock_data.csv')
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    stock_data.sort_values('Date', inplace=True)
    X = stock_data[['Open', 'High', 'Low', 'Volume']]
    y = stock_data['Close']
    model = RandomForestRegressor()
    model.fit(X, y)
    open_price = float(request.form['open'])
    high_price = float(request.form['high'])
    low_price = float(request.form['low'])
    volume = float(request.form['volume'])
    current_date = datetime.now().strftime('%Y-%m-%d')
    input_data = pd.DataFrame({'Date': [current_date],
                               'Open': [open_price],
                               'High': [high_price],
                               'Low': [low_price],
                               'Volume': [volume]})
    input_data['Date'] = pd.to_datetime(input_data['Date'])
    stock_data = stock_data.append(input_data, ignore_index=True)
    next_day = stock_data.tail(1).copy()
    next_day['Date'] = next_day['Date'] + pd.DateOffset(days=1)
    next_day.drop(columns=['Close'], inplace=True)
    prediction = model.predict(next_day[['Open', 'High', 'Low', 'Volume']])

    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from datetime import datetime

app = Flask(__name__)

# Function to update stock_data
def update_stock_data(input_data):
    try:
        stock_data = pd.read_csv('stock_data.csv')
        print("Type of stock_data inside update_stock_data:", type(stock_data))  # Print the type
        stock_data['Date'] = pd.to_datetime(stock_data['Date'])
        stock_data.sort_values('Date', inplace=True)
    except Exception as e:
        print("Error reading CSV file:", e)
        stock_data = pd.DataFrame(columns=['Date', 'Open', 'High', 'Low', 'Volume'])
    
    # Concatenate new input_data with stock_data
    updated_stock_data = pd.concat([stock_data, input_data], ignore_index=True)
    
    # Return updated DataFrame
    return updated_stock_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
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
    
    # Call the update_stock_data function to update stock_data
    updated_stock_data = update_stock_data(input_data)
    
    if not updated_stock_data.empty:
        X = updated_stock_data[['Open', 'High', 'Low', 'Volume']]
        y = updated_stock_data['Close']
        
        # Drop rows with NaN values in y (Close)
        updated_stock_data.dropna(subset=['Close'], inplace=True)
        X = updated_stock_data[['Open', 'High', 'Low', 'Volume']]
        y = updated_stock_data['Close']
        
        model = RandomForestRegressor()
        model.fit(X, y)
        
        next_day = updated_stock_data.tail(1).copy()
        next_day['Date'] = next_day['Date'] + pd.DateOffset(days=1)
        next_day.drop(columns=['Close'], inplace=True)
        
        try:
            prediction = model.predict(next_day[['Open', 'High', 'Low', 'Volume']])
        except Exception as e:
            print("Error predicting:", e)
            prediction = None
    else:
        prediction = None

    return render_template('index.html', prediction=prediction[0] if prediction is not None else "Error predicting")


if __name__ == '__main__':
    app.run(debug=True)

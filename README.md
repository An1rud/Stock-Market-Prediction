# Stock Price Prediction Web App
- This code creates a Flask web app for predicting the next day's stock closing price. Users input current day's stock data (open, high, low, volume), and a Random Forest Regressor model predicts the price for the following day. The prediction is displayed on the webpage.

## Installation
Clone the repository:
```bash
git clone https://github.com/yourusername/stock-price-prediction.git
```
Install the required Python packages:

```bash
pip install -r requirements.txt
```
## Usage
Run the Flask app:
```bash
python app.py
```
Enter the latest stock data (Open, High, Low, Volume) in the input fields.

Click on the "Predict" button to get the predicted closing price for the next day.

## Files
- app.py: The main Flask application file containing the routes and prediction logic.
- templates/: Directory containing HTML templates for the web pages.
- index.html: The main HTML file for the home page and prediction results.
- static/: Directory for static files such as images.
- stock_data.csv: CSV file containing historical stock data.
## Dependencies
- Flask: Web framework for Python
- pandas: Data manipulation library
- scikit-learn: Machine learning library for the Random Forest Regressor
- datetime: Library for manipulating dates and times
### Notes
- This app uses a simple Random Forest Regressor model for stock price prediction. For more accurate predictions, consider using more sophisticated models or additional features.

- The stock_data.csv file should contain historical stock data with columns: Date, Open, High, Low, Close, and Volume.

- Make sure to handle errors gracefully, especially when reading CSV files or making predictions.

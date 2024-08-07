# Stock Market Prediction Web App

This is a stock market prediction web application built using .NET. The application utilizes machine learning to predict stock prices based on historical data.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Stock Market Prediction Web App leverages machine learning to predict future stock prices. The application reads historical stock data, trains a machine learning model, and provides predictions.

## Features

- Upload CSV or Excel files containing historical stock data.
- Train a machine learning model on the uploaded data.
- Predict future stock prices based on the trained model.
- Display data previews and visualizations.

## Prerequisites

- .NET 8.0 SDK
- Microsoft.ML
- Microsoft.ML.Data

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/An1rud/Stock-Market-Prediction.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Stock-Market-Prediction
   ```
3. Restore the required packages:
   ```sh
   dotnet restore
   ```
4. Build the project:
   ```sh
   dotnet build
   ```

## Usage

1. Run the application:
   ```sh
   dotnet run
   ```
2. Open your web browser and navigate to `http://localhost:5000` to access the web app.

3. Upload your historical stock data in CSV or Excel format.

4. Train the model by selecting the relevant options.

5. View the predictions and visualizations generated by the model.

## Project Structure

```
StockMarketPredictionApp/
├── Controllers/
│   └── HomeController.cs
├── Models/
│   └── StockModel.cs
├── Views/
│   └── Home/
│       └── Index.cshtml
├── wwwroot/
│   └── css/
│       └── site.css
├── Data/
│   └── StockData.cs
├── Program.cs
├── Startup.cs
└── StockMarketPredictionApp.csproj
```

- `Controllers/`: Contains the MVC controllers for handling HTTP requests.
- `Models/`: Contains the data models used in the application.
- `Views/`: Contains the Razor views for rendering HTML.
- `wwwroot/`: Contains static files such as CSS and JavaScript.
- `Data/`: Contains classes for data loading and manipulation.
- `Program.cs`: The entry point of the application.
- `Startup.cs`: Configures the application services and middleware.


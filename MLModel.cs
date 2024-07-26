using Microsoft.ML;
using Microsoft.ML.Data;
using StockMarketPrediction.Models;
using System;
using System.IO;

namespace StockMarketPrediction
{
    public class MLModel
    {
        private static readonly string ModelPath = Path.Combine(Environment.CurrentDirectory, "MLModel.zip");

        public void TrainModel()
        {
            var context = new MLContext();
            var data = context.Data.LoadFromTextFile<StockData>("wwwroot/data/stock_data.csv", separatorChar: ',', hasHeader: true);

            var pipeline = context.Transforms.Concatenate("Features", "Open", "High", "Low", "Volume")
                .Append(context.Transforms.CopyColumns(outputColumnName: "Label", inputColumnName: "Close"))
                .Append(context.Regression.Trainers.FastTree());

            var model = pipeline.Fit(data);
            context.Model.Save(model, data.Schema, ModelPath);
        }

        public float Predict(float open, float high, float low, float volume)
        {
            var context = new MLContext();
            var model = context.Model.Load(ModelPath, out var schema);
            var predictionEngine = context.Model.CreatePredictionEngine<StockData, StockPrediction>(model);

            var stockData = new StockData
            {
                Open = open,
                High = high,
                Low = low,
                Volume = volume
            };

            var prediction = predictionEngine.Predict(stockData);
            return prediction.PredictedClose;
        }
    }
}

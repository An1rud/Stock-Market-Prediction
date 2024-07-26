using Microsoft.AspNetCore.Mvc;
using StockMarketPrediction.Models;
using System.Diagnostics;

namespace StockMarketPrediction.Controllers
{
    public class HomeController : Controller
    {
        private readonly MLModel _mlModel;

        public HomeController()
        {
            _mlModel = new MLModel();
            _mlModel.TrainModel();
        }

        public IActionResult Index()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Predict(float open, float high, float low, float volume)
        {
            Debug.WriteLine("Received form data: ");
            Debug.WriteLine($"Open: {open}, High: {high}, Low: {low}, Volume: {volume}");

            var prediction = _mlModel.Predict(open, high, low, volume);

            Debug.WriteLine($"Prediction: {prediction}");

            ViewBag.Prediction = prediction;
            return View("Result");
        }
    }
}

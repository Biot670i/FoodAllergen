
using Microsoft.AspNetCore.Mvc;

namespace FoodAllergen.Controller
{
    public class CsvController : ControllerBase
    {
        // Controller action to serve the CSV file
        public IActionResult GetCsvFile()
        {
            string filePath = @"C:\Users\mecum\source\repos\Accesion_query\AllergenDB.csv";
            string csvContent = System.IO.File.ReadAllText(filePath);
            return Content(csvContent, "text/csv");
        }
    }
}
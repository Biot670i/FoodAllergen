namespace FoodAllergen.Models
{
    namespace FoodAllergen.Models
    {
        public class SwissDto
        {
            public string Token { get; set; }
            public string ProjectId { get; set; }
            public string TargetSequences { get; set; }
            public string TemplateSequence { get; set; }
            public int TemplateSeqresOffset { get; set; }
            public string PdbId { get; set; }
            public string AuthAsymId { get; set; }
            public int AssemblyId { get; set; }
            public string TemplateCoordinates { get; set; }
            public string ProjectTitle { get; set; }
            public string CoordinatesUrl { get; set; }
            public string DownloadId { get; set; }
            public string DownloadUrl { get; set; }
            public string Status { get; set; }
            public List<ModelDto> Models { get; set; }
        }

        public class ModelDto
        {
            public string CoordinatesUrl { get; set; }
            // Add other properties of Model if required
        }
    }
}
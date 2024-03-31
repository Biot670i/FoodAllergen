namespace FoodAllergen.Models
{
    public class Browse_DbDto
    {
        public Guid Id { get; set; }
        public string Species { get; set; }
        public string? Common { get; set; }
        public string? IUIS_Allergen { get; set; }
        public string Type { get; set; }
        public string Group { get; set; }
        public string Allergenicity { get; set; }
        public short Length { get; set; }
        public string Accession { get; set; }
        public int GI { get; set; }
        public byte _1st_Version { get; set; }
    }
}
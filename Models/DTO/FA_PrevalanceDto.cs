namespace FoodAllergen.Models.DTO
{
    public class FA_PrevalanceDto
    {
        public string Variable { get; set; }
        public string? Prevalence_of_Current_FA_95_CI { get; set; }
        public string? P_Value { get; set; }
        public string? Prevalence_of_Adult_Onset_Current_FA_95_CI { get; set; }
        public string? P_Value2 { get; set; }

    }
}

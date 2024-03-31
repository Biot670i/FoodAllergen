namespace FoodAllergen.DTO
{
    public class FA_PrevalanceDto
    {
        public int Id { get; set; }
        public string Variable { get; set; }
        public PrevalenceInfo Prevalence_of_Current_FA_95_CI { get; set; }
        public PrevalenceInfo Prevalence_of_Adult_Onset_Current_FA_95_CI { get; set; }
        public double P_Value2 { get; set; }
    }

    public class PrevalenceInfo
    {
        public double Value { get; set; }
        public (double LowerBound, double UpperBound)? Range { get; set; } // Nullable range
    }
}
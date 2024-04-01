using System.ComponentModel.DataAnnotations;

namespace FoodAllergen.Models.DTO
{
    public class RegisterRequestDto
    {
        [Required]
        [DataType(DataType.EmailAddress)]
        public string Username { get; set; }

        [Required]
        [DataType(DataType.Password)]
        public string Password { get; set; }

        [Required]
        [DataType(DataType.Password)]
        [Compare(nameof(Password))] // Ensures that ConfirmPassword matches Password
        public string ConfirmPassword { get; set; }

        public string[] Roles { get; set; }
    }
}
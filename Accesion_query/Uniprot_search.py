import csv
import requests

def search_uniprot(accession_numbers):
    for accession_number in accession_numbers:
        # Construct the URL for retrieving protein information in text format
        url = f"https://rest.uniprot.org/uniprotkb/{accession_number}.fasta"

        # Send HTTP GET request to UniProt REST API
        response = requests.get(url)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            # Save the response content to a file
            filename = f"uniport_data_{accession_number}.fasta"
            with open(filename, 'w') as f:
                f.write(response.text)
            print(f"UniProt data saved to {filename}")
        else:
            print(f"Failed to retrieve information for accession number {accession_number}")

def main():
    common_name = input("Which common name do you want to find? ").strip()  # Remove leading/trailing whitespace
    csv_file = "AllergenDB.csv"  # Update with the actual filename
    accession_numbers = []
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Get the header row
        print("Header row:", header)
        if 'Common' not in header:
            print("Common Name column not found in CSV file.")
            return
        common_name_index = header.index('Common')
        accession_number_index = header.index('Accession') if 'Accession' in header else None
        for row in reader:
            row_common_name = row[common_name_index].strip() if len(row) > common_name_index else ''
            print(f"Comparing '{common_name}' with '{row_common_name}'")
            if row_common_name.lower() == common_name.lower():
                accession_number = row[accession_number_index] if accession_number_index is not None else None
                if accession_number:
                    accession_numbers.append(accession_number)
        if accession_numbers:
            search_uniprot(accession_numbers)
        else:
            print("No accession numbers found for the given common name.")

if __name__ == "__main__":
    main()
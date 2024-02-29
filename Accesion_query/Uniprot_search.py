import csv
import requests

def search_uniprot(accession_number):
    # Construct the URL for retrieving protein information in text format
    url = f"https://rest.uniprot.org/uniprotkb/{accession_number}.txt"

    # Send HTTP GET request to UniProt REST API
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Save the response content to a file
        filename = f"uniport_data_{accession_number}.txt"
        with open(filename, 'w') as f:
            f.write(response.text)
        print(f"UniProt data saved to {filename}")
    else:
        print(f"Failed to retrieve information for accession number {accession_number}")

def main():
    common_name = input("Which common name do you want to find? ").strip()  # Remove leading/trailing whitespace
    csv_file = "AllergenDB.csv"  # Update with the actual filename
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
                    search_uniprot(accession_number)
                else:
                    print("Accession number not found for the given common name.")
                break
        else:
            print(f"No entry found for common name '{common_name}'")

if __name__ == "__main__":
    main()

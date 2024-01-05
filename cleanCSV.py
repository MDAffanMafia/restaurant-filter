import csv

def clean_csv(input_path, output_path):
    with open(input_path, 'r') as infile, open(output_path, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames

        # Create a writer with the same fieldnames
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            # Clean up each row
            clean_row = {key: value.strip() if isinstance(value, str) else value for key, value in row.items()}
            writer.writerow(clean_row)

if __name__ == "__main__":
    input_csv = 'D:/restaurantSearch/restaurantSearch/restaurants_small.csv'  # Update with the correct path
    output_csv = 'D:/restaurantSearch/restaurantSearch/restaurantFinal.csv'  # Update with the desired output path

    clean_csv(input_csv, output_csv)

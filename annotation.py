import os
import csv
import sys

def create_csv(folder_name):
    # Create a CSV file with three columns: folder, filename, class
    with open('file_info_miss_1.csv', 'w', newline='') as csvfile:
        fieldnames = ['folder', 'filename', 'class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Iterate through files and subfolders in the specified folder
        for root, dirs, files in os.walk(folder_name):
            for filename in files:
                # Get folder name and file name
                folder = os.path.basename(root)
                filepath = os.path.join(root, filename)

                # Determine class based on folder name
                class_value = 0 if folder == 'fold14' else 1

                # Write to CSV
                writer.writerow({'folder': folder, 'filename': filename, 'class': class_value})

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_name>")
        sys.exit(1)

    folder_name = "DataSet"
    create_csv(folder_name)
    print("CSV file created successfully.")

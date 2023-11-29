import csv

input_file_path = "0.edges"
output_file_path = "output.csv"

with open(input_file_path, "r") as input_file:
    lines = input_file.readlines()

edges = [line.strip().split() for line in lines]

with open(output_file_path, "w", newline="") as output_file:
    csv_writer = csv.writer(output_file)
    csv_writer.writerow(["numeric_id_1", "numeric_id_2"])  # Write header
    csv_writer.writerows(edges)
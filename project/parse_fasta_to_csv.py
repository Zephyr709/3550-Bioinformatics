
import csv

input_file = 'EnterobactericaeaP3.fas'
output_file = 'parsed_sequences.csv'

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_writer = csv.writer(outfile)
    csv_writer.writerow(['index', 'direction', 'sequence'])
    
    for line in infile:
        if line.startswith('>'):
            parts = line[1:].strip().split('_')
            index = parts[1]
            direction = parts[2]
        else:
            sequence = line.strip()
            csv_writer.writerow([index, direction, sequence])
import os
import csv

input_folder = 'path/to/your/folder'
output_folder = 'path/to/output/folder'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.fas'):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, f'parsed_{filename}.csv')
        
        with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(['index', 'direction', 'sequence'])
            
            for line in infile:
                if line.startswith('>'):
                    parts = line[1:].strip().split('_')
                    index = parts[1] if len(parts) > 1 else '1'
                    direction = parts[2] if len(parts) > 2 else parts[1]
                else:
                    sequence = line.strip()
                    csv_writer.writerow([index, direction, sequence])
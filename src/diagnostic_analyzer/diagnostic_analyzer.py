import os

def analyze_diagnostic_log(input_file):
    prefix = "#PE"

    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    size_threshold_bytes = 4000
    
    file_size = os.path.getsize(input_file)
    print(f"File size: {file_size :.2f} Byte(s)")
    
    if file_size <= size_threshold_bytes:
        print("Strategy: File is small enough. Reading entirely into memory...")
        
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        processed_lines = []
        for line in lines:
            processed_lines.append(line)

    else:
        print("Strategy: File is too large. Streaming line-by-line to protect memory...")
        output_file = "filtered_tmp_file.log"
        
        with open(input_file, "r", encoding="utf-8") as infile, \
            open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                if line.startswith(prefix):
                    outfile.write(line)
        print(f"filtered entries written to '{output_file}'")
    
    print("Processing complete!")

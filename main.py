import re
import csv

def convert(input_file, output_file, filter_string, mode):

    input = input_file
    output = output_file
    filter = filter_string

    with open(input, 'r', encoding='utf-8') as f_in, open(output, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            if mode == 0:
                if filter not in line:
                    f_out.write(line)
            if mode == 1:
                if filter in line:
                    f_out.write(line)


def extract_numbers(filename, output_filename):
    with open(filename, 'r') as file:
        text = file.read()
        numbers = re.findall(r'\d+\.\d+|\d+', text)  # 부동 소수점에 대한 정규 표현식 추가

        divided_numbers = [numbers[i:i + 4] for i in range(0, len(numbers), 4)]

        with open(output_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(divided_numbers)


convert("WaterDrop_RMSProp.txt", "WaterDrop_RMSProp1.txt", "b'", 0)
convert("WaterDrop_RMSProp1.txt", "WaterDrop_RMSProp2.txt", "basic_session_run_hooks", 0)
convert("WaterDrop_RMSProp2.txt", "WaterDrop_RMSProp3.txt", "global", 0)
convert("WaterDrop_RMSProp3.txt", "WaterDrop_RMSProp_output.txt", "step", 1)

# extract_numbers("WaterDrop_Adam_output.txt", "WaterDrop_Adam_output.csv")
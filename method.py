import docx
import re

def extract_table_columns(docx_file_path, output_txt_file):
    doc = docx.Document(docx_file_path)
    extracted_data = []
    table_number = 0

    for table in doc.tables:
        table_number += 1
        print("Table number:", table_number)

        try:
            found_xyz = False
            x_index, y_index, z_index = None, None, None

            for row in table.rows:
                headings = [cell.text.strip().lower() for cell in row.cells]

                if 'x' in headings and 'y' in headings and 'z' in headings:
                    x_index = headings.index('x')
                    y_index = headings.index('y')
                    z_index = headings.index('z')
                    found_xyz = True
                    break

            if found_xyz:
                extracted_data.append(f"\nTable {table_number}\nX\tY\tZ")
                for row in table.rows:
                    data = [cell.text.strip() for cell in row.cells]

                    if len(data) > max(x_index, y_index, z_index):
                        x_value = re.findall(r'\d+\.?\d*', data[x_index])
                        y_value = re.findall(r'\d+\.?\d*', data[y_index])
                        z_value = re.findall(r'\d+\.?\d*', data[z_index])

                        x_value = ' '.join(x_value)
                        y_value = ' '.join(y_value)
                        z_value = ' '.join(z_value)
                        extracted_data.append(f"{x_value}\t{y_value}\t{z_value}")
            else:
                print(f"Skipping Table {table_number} - Does not meet criteria")
        except docx.oxml.exceptions.InvalidXmlError:
            print(f"Skipping Table {table_number} - Invalid Table Structure")

    with open(output_txt_file, 'w') as txt_file:
        for line in extracted_data:
            txt_file.write(line + '\n')


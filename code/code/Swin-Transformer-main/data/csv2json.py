import pandas as pd
import json


def csv_to_json_list(csv_file_path, output_json_path):

    df = pd.read_csv(csv_file_path)
    json_data = df.values.tolist()
    with open(output_json_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"CSV file '{csv_file_path}' has been converted to JSON list format and saved to '{output_json_path}'")



csv_file = "Test.csv"
output_file = "test.json"
csv_to_json_list(csv_file, output_file)
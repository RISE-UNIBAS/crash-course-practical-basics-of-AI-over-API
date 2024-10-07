"""Test script to measure the difference between two JSON files.
The script loads two JSON files and compares the objects in them to find the differences.
This is a try to use the output of two different models to compare the results to get
an idea of the accuracy of the answers."""
import json
from deepdiff import DeepDiff


# Load the two JSON files
def load_json(file_path):
    """Load a JSON file from the given path."""
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)


json_list_1 = load_json('../answers/google/3693659.json')
json_list_2 = load_json('../answers/openai/3693659.json')

# Loop through each object in the lists and compare them
for i, (obj1, obj2) in enumerate(zip(json_list_1[:10], json_list_2[:10])):
    diff = DeepDiff(obj1, obj2, ignore_order=True)
    diff_count = len(diff)

    print(f"Object {i + 1} Differences ({len(diff)}):")
    if 'values_changed' in diff:
        for value in diff['values_changed']:
            old_val = diff['values_changed'][value]['old_value']
            new_val = diff['values_changed'][value]['new_value']
            print(f"Value Change for {value}: {old_val} -> {new_val}")

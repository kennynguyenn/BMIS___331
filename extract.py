import json

def extract_descriptions(json_file, key_name):
    with open(json_file) as file:
        data = json.load(file)

    descriptions = [item[key_name] for item in data if key_name in item]
    return descriptions

def descriptions_to_dict(descriptions_list):
    return {f"Job Description {index + 1}": desc for index, desc in enumerate(descriptions_list)}

def write_dict_to_json(descriptions_dict, output_file):
    with open(output_file, "w") as file:
        json.dump(descriptions_dict, file, indent=2)

json_file = "/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/results/jobs.json"
key_name = "description"
output_json_file = "all_JD.json"

descriptions_list = extract_descriptions(json_file, key_name)

descriptions_dict = descriptions_to_dict(descriptions_list)


write_dict_to_json(descriptions_dict, output_json_file)

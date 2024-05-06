import json
from bs4 import BeautifulSoup

def clean_html_tags(description):
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(description, 'html.parser')
    # Remove all HTML tags
    cleaned_text = soup.get_text(separator=' ', strip=True)
    return cleaned_text

def clean_descriptions(descriptions_dict):
    cleaned_descriptions = {}
    for key, description in descriptions_dict.items():
        cleaned_description = clean_html_tags(description)
        cleaned_descriptions[key] = cleaned_description
    return cleaned_descriptions

# Load job descriptions from JSON file
with open('/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/all_JD.json') as file:
    data = json.load(file)

# Clean HTML tags from job descriptions
cleaned_descriptions = clean_descriptions(data)

# Write cleaned descriptions to clean.json
output_file_path = ""

# Write cleaned descriptions to clean.json
with open('clean.json', 'w') as outfile:
    json.dump(cleaned_descriptions, outfile, indent=2)
import os
from tika import unpack
import json
from collections import Counter
import re

def convert_pdf_to_text(pdf_file_path):
    # Convert PDF to text using Apache Tika
    text_output = unpack.from_file(pdf_file_path)
    return text_output

def clean_text(text_content):
    # Remove unwanted characters and normalize spaces
    cleaned_text = re.sub(r'\s+', ' ', text_content).strip()
    return cleaned_text

def count_word_occurrences(cleaned_text):
    words = cleaned_text.split()
    word_counts = Counter(words)
    return word_counts

def save_word_counts_to_file(word_counts, output_file_path):
    word_counts_dict = dict(word_counts)

    # Save the word counts as JSON to a new file
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(word_counts_dict, output_file, ensure_ascii=False, indent=4)

def main():
    # Path to PDF file
    pdf_file_path = '/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/mock.pdf'
    extracted_text = convert_pdf_to_text(pdf_file_path)
    cleaned_text = clean_text(extracted_text['content'])
    word_counts = count_word_occurrences(cleaned_text)
    output_file_path = '/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/tika-python-master/word_counts.json'
    save_word_counts_to_file(word_counts, output_file_path)

    print(f"Word counts extracted from PDF and saved to '{output_file_path}' successfully!")

if __name__ == "__main__":
    main()

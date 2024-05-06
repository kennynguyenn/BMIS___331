import csv
import json

def load_words_json(file_path):
    # Load words from a JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return set(data.keys())  # Extract unique words from JSON data

def load_words_csv(file_path):
    # Load words from a CSV file, skipping the first row (headers)
    words = set()
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            word = row[1]  # Assuming the word is in the second column
            words.add(word)
    return words

def calculate_matching_percentage(words1, words2):
    # Calculate the matching percentage of words between two sets of words
    matching_words = len(words1 & words2)  # Count common words
    total_words1 = len(words1)
    total_words2 = len(words2)

    if total_words1 == 0 or total_words2 == 0:
        return 0.0
    
    percentage = (matching_words / min(total_words1, total_words2)) * 100
    return percentage

def main():
    # Path to the first word list JSON file
    file_path1 = '/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/tika-python-master/word_counts.json'

    # Path to the second word list CSV file
    file_path2 = '/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/words.csv'
    words1 = load_words_json(file_path1)
    words2 = load_words_csv(file_path2)
    matching_percentage = calculate_matching_percentage(words1, words2)

    # Output the matching percentage
    print(f"Matching percentage between the two files: {matching_percentage:.2f}%")

if __name__ == "__main__":
    main()

import json
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv

# Load NLTK stopwords
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenize words
    words = word_tokenize(text)
    # Remove stopwords
    words = [word for word in words if word not in stop_words]
    return words

def count_word_frequencies(descriptions):
    # Initialize Counter object to count word frequencies
    word_counts = Counter()
    for desc in descriptions:
        words = preprocess_text(desc)  # Access description directly
        word_counts.update(words)
    return word_counts

def rank_top_words(word_counts, top_n=50):
    # Sort word frequencies in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    # Select top N words
    top_words = sorted_words[:top_n]
    return top_words

# Load job descriptions from JSON file
with open('/Users/kenny/Documents/School_related_shits/Spring_2024/BMIS_331/Final_Proj/indeed-scraper/clean.json') as file:
    data = json.load(file)

# Check if data is a dictionary
if isinstance(data, dict):
    # Extract job descriptions from JSON data
    job_descriptions = list(data.values())  # Convert dict_values object to list

    # Count word frequencies across all job descriptions
    word_counts = count_word_frequencies(job_descriptions)

    # Rank and select top 50 most common words
    top_words = rank_top_words(word_counts)

    # Write top 50 words and their frequencies to a CSV file
    with open('words.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Rank', 'Word', 'Frequency'])
        for idx, (word, freq) in enumerate(top_words, 1):
            csv_writer.writerow([idx, word, freq])

    print("Top 50 words ranked saved to words.csv")
else:
    print("Error: Data is not in the expected format.")

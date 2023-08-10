
# Import libraries
import requests
import json
import random
import re

# Define constants
COCA_URL = "https://api.sketchengine.eu/bonito/run.cgi/corp_info?corpname=preloaded%2Fcoca_2020_1"
SKETCH_URL = "https://api.sketchengine.eu/bonito/run.cgi/wordsketch?corpname=preloaded%2Fcoca_2020_1&lemma={}&format=json"
SAMPLE_SIZE = 100

# Define functions
def get_corpus_size():
# Get the size of COCA corpus
    response = requests.get(COCA_URL)
    data = json.loads(response.text)
    size = data["corpus_info"]["size"]
    return size

def get_word_freq(word):
# Get the frequency of a word in COCA corpus
    response = requests.get(SKETCH_URL.format(word))
    data = json.loads(response.text)
    freq = data["freq"]
    return freq

def get_word_examples(word):
# Get a list of examples of a word in COCA corpus
    response = requests.get(SKETCH_URL.format(word))
    data = json.loads(response.text)
    examples = data["Examples"]
    return examples

def sample_sentences(word):
# Sample a random subset of sentences from the examples of a word
    examples = get_word_examples(word)
    sentences = [example["text"] for example in examples]
    sample = random.sample(sentences, SAMPLE_SIZE)
    return sample

def check_misuse(sentence, word):
# Check if a sentence contains a misuse of a word
# Based on a simple heuristic: if the word is followed by "for" or "of", and the complement is not negative, then it is a misuse
    pattern = r"\b{}\b\s+(for|of)\s+\w+".format(word)
    match = re.search(pattern, sentence)
    if match:
        complement = match.group().split()[-1]
    negative_words = ["crime", "scandal", "corruption", "violence", "abuse", "murder", "fraud", "terror", "evil", "sin"]
    if complement not in negative_words:
        return True
    else:
        return False
    
def estimate_misuse_rate(word):
# Estimate the misuse rate of a word in COCA corpus
    sample = sample_sentences(word)
    misuse_count = 0
    for sentence in sample:
        if check_misuse(sentence, word):
            misuse_count += 1
    misuse_rate = misuse_count / SAMPLE_SIZE
    return misuse_rate

# Main program
corpus_size = get_corpus_size()
notoriety_freq = get_word_freq("notoriety")
notorious_freq = get_word_freq("notorious")
notoriety_misuse_rate = estimate_misuse_rate("notoriety")
notorious_misuse_rate = estimate_misuse_rate("notorious")

print(f"The size of COCA corpus is {corpus_size} tokens.")
print(f"The word 'notoriety' appears {notoriety_freq} times in the corpus.")
print(f"The word 'notorious' appears {notorious_freq} times in the corpus.")
print(f"The estimated misuse rate of 'notoriety' is {notoriety_misuse_rate * 100}%.")
print(f"The estimated misuse rate of 'notorious' is {notorious_misuse_rate * 100}%.")

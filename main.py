from collections import Counter

#Boots provided this as a more concise way to count characters
def count_characters(file_content):
    # Normalize to lowercase and use Counter directly on the concatenated string of all words
    return Counter(char for word in file_content.lower().split() for char in word if char.isalpha())

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(file_content):
    words = file_content.lower().split()
    return len(words)
    
# Old code to count characters using a loop:
# def count_characters(file_content):
#     words = file_content.lower().split()
#     character_counts = {}
#     # Iterate over each character in each word, counting occurrences and storing in dictionary.
#     for word in words:
#         for char in word:
#             if char not in character_counts:
#                 character_counts[char] = 1
#             else:
#                 character_counts[char] += 1
#     return character_counts

def convert_dictionary(dictionary):
    # Convert dictionary to list of dictionaries, keeping only alphanumeric keys
    return [{"letter": key, "count": value} for key, value in dictionary.items() if key.isalpha()]

def sort_on(dictionary):
    return dictionary["count"]

def print_results(dictionary, word_count, path_to_book):
    print(f"--- Begin report of {path_to_book} ---\n")
    print(f"{word_count} words found in the document.\n")
    
    for item in dictionary:
        print(f"The '{item['letter']}' was found {item['count']} times.")

    print("\n--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)    
    word_count = count_words(text)
    dict = convert_dictionary(count_characters(text))
    dict.sort(reverse=True, key=sort_on)
    print_results(dict, word_count, path_to_file)
main()
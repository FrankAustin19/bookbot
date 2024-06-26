def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = countwords(file_contents)
        char_count = character_scenes(file_contents)
        make_report(file_contents)
        

def countwords(text):
    words = text.split()
    word_count = len(words)
    return word_count

def character_scenes(text):
    lowered_string = text.lower()  
    char_counts = {}               

    for char in lowered_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
     
def sort_on(dict):
    return dict["count"]

def make_report(text):
    word_count = countwords(text)
    char_count = character_scenes(text)

    list_of_dicts = []
    for char, count in char_count.items():
        list_of_dicts.append({"char": char, "count": count})

    list_of_dicts.sort(key=sort_on, reverse=True)

    print(f" --- BEGIN REPORT ---")
    print(f"{word_count} words found in the document")

    for item in list_of_dicts:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['count']} times")


    print(f" --- End report ---")


if __name__ == "__main__":
    main()


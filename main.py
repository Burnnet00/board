def find_first_non_repeating_character(text):
    words = text.split() #
    non_repeating_chars = []
    for word in words:
        char_count = {}
        for char in word:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        for char in word:
            if char_count[char] == 1:
                non_repeating_chars.append(char)
                break
    for char in non_repeating_chars:
        if non_repeating_chars.count(char) == 1:
            return char
    return None

text = "C makes it easy for you to shoot yourself in the foot. C++ makes"
print(find_first_non_repeating_character(text))

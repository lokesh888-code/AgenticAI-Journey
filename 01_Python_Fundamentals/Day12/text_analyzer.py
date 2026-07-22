def analyze_text(text):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for ch in text if ch in vowels)
    consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)

    return {
        "characters": len(text),
        "words": len(text.split()),
        "vowels": vowel_count,
        "consonants": consonant_count,
        "spaces": text.count(" ")
    }



# count = sum(1 if i % 2 == 0 else 0 for i in range(1, 6))
# print(count)  # 2  (because 2 and 4 are even)
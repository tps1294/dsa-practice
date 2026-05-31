# Count words challenge

def count_words(text):
    words = text.split()
    counts = {}

    for word in words:
        counts[word] = counts.get(word ,) + 1
        return counts
    
    print (count_words("the cat sat on the mat the cat"))


    
        
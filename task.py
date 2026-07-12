# Input sentence
sentence = "Machine learning is transforming the world"

# Split the sentence into words
words = sentence.split()

# Print the result
print(words)


# Input text containing multiple sentences
text = "Machine learning is a branch of AI. It helps computers learn from data. It is used in many applications."

# Split the text into sentences
sentences = text.split(".")

# Print each sentence
for sentence in sentences:
    if sentence.strip():   # Ignore empty strings
        print(sentence.strip())
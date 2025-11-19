def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])
sentence="hello world python"
output=reverse_words(sentence)
print(output)
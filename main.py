from textblob import TextBlob
words = ["Machne", "Learnin","bitween","holl","teble"]
corrected_words = []
for i in words:
    corrected_words.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected Words are :")
for i in corrected_words:
    print(i.correct(), end=" ")

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


lemmatizer = WordNetLemmatizer()


text = "The striped bats were hanging on their feet and ate best fishes"


words = word_tokenize(text)


print("Original Word : Lemmatized Word")
for word in words:
    lemma = lemmatizer.lemmatize(word)
    print(f"{word:<15} : {lemma}")

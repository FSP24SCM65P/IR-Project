from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "The cat chased the mouse around the house.",
    "A sudden gust of wind knocked over the trash cans.",
    "She smiled warmly as she greeted her old friend.",
    "The sun dipped below the horizon, painting the sky with hues of orange and pink.",
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
print(vectorizer.get_feature_names_out())
print(X.toarray())

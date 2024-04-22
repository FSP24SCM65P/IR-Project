from flask import Flask, request, jsonify, abort
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk
from nltk.corpus import wordnet as wn
from spellchecker import SpellChecker

nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)

documents = [
    "Python code examples for machine learning",
    "Flask is a micro web framework for Python",
    "Natural language processing with NLTK"
]
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

spell = SpellChecker()

def check_spelling_and_expand(query):
    corrected_query = []
    for word in query.split():
        if spell.unknown([word]):
            corrected_word = spell.correction(word)
        else:
            corrected_word = word

        corrected_query.append(corrected_word)

        synonyms = set()
        for syn in wn.synsets(corrected_word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())

        corrected_query.extend(list(synonyms))
    return ' '.join(corrected_query)

@app.route('/search', methods=['POST'])
def search():
    if not request.is_json:
        return abort(400, description="Missing JSON in request")

    json_data = request.get_json()
    query = json_data.get('query', '')

    if not query:
        return abort(400, description="Empty query")

    corrected_query = check_spelling_and_expand(query)

    query_vec = tfidf_vectorizer.transform([corrected_query])
    cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()
    top_k_indices = cosine_similarities.argsort()[-5:][::-1]  # Change 5 to the desired K

    top_k_results = [(documents[index], cosine_similarities[index]) for index in top_k_indices]

    return jsonify({
        'corrected_query': corrected_query,
        'results': top_k_results
    })

if __name__ == '__main__':
    app.run(debug=True)

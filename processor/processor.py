from flask import Flask, request, jsonify, abort
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk
from nltk.corpus import wordnet as wn
from spellchecker import SpellChecker

# Download necessary NLTK datasets
nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)

# Dummy dataset and vectorizer for demonstration purposes
documents = [
    "Python code examples for machine learning",
    "Flask is a micro web framework for Python",
    "Natural language processing with NLTK"
]
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Initialize spell checker
spell = SpellChecker()

def check_spelling_and_expand(query):
    corrected_query = []
    for word in query.split():
        # Check the spelling
        if spell.unknown([word]):
            corrected_word = spell.correction(word)
        else:
            corrected_word = word

        corrected_query.append(corrected_word)

        # Expand the query with synonyms
        synonyms = set()
        for syn in wn.synsets(corrected_word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())

        corrected_query.extend(list(synonyms))
    return ' '.join(corrected_query)

@app.route('/search', methods=['POST'])
def search():
    # Check if JSON is provided
    if not request.is_json:
        return abort(400, description="Missing JSON in request")

    # Extract the query from the JSON request
    json_data = request.get_json()
    query = json_data.get('query', '')

    # Validate the query
    if not query:
        return abort(400, description="Empty query")

    # Optional: Check spelling and expand query
    corrected_query = check_spelling_and_expand(query)

    # Process the query and get top-K results
    query_vec = tfidf_vectorizer.transform([corrected_query])
    cosine_similarities = linear_kernel(query_vec, tfidf_matrix).flatten()
    top_k_indices = cosine_similarities.argsort()[-5:][::-1]  # Change 5 to the desired K

    # Get top-K results
    top_k_results = [(documents[index], cosine_similarities[index]) for index in top_k_indices]

    return jsonify({
        'corrected_query': corrected_query,
        'results': top_k_results
    })

if __name__ == '__main__':
    app.run(debug=True)

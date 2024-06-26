import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer

def read_html_files(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".html"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                text = f.read()
                documents.append(text)
    return documents

def convert_to_json(documents, json_folder):
    for i, document in enumerate(documents):
        json_data = {
            "id": i,
            "content": document
        }
        with open(os.path.join(json_folder, f"document_{i}.json"), "w") as json_file:
            json.dump(json_data, json_file)

def index_documents(documents):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)
    return X, vectorizer

def construct_inverted_index(documents, vectorizer):
    inverted_index = {}
    terms = vectorizer.get_feature_names_out()
    for i, document in enumerate(documents):
        for term in terms:
            if term in document:
                if term in inverted_index:
                    inverted_index[term].append(i)
                else:
                    inverted_index[term] = [i]
    return inverted_index

if __name__ == "__main__":
    html_folder = "../crawler/"
    json_folder = html_folder  
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)
    
    documents = read_html_files(html_folder)
    
    convert_to_json(documents, json_folder)
    
    X, vectorizer = index_documents(documents)
    
    inverted_index = construct_inverted_index(documents, vectorizer)
    
    print("Inverted Index:")
    for term, document_ids in inverted_index.items():
        print(f"{term}: {document_ids}")

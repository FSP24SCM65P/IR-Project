# IR-Project

Project Report

### Abstract

This report delves into the development and analysis of three Python files: `crawler.py`, `indexer.py`, and `processor.py`. 

### Overview

These files collectively represent a system for web crawling, text indexing, and search processing. The `crawler.py` file utilizes the Scrapy library to crawl web pages, the `indexer.py` file employs the sklearn library to index text documents using TF-IDF, and the `processor.py` file creates a Flask API to handle search queries. The solution aims to provide a framework for web data collection, text analysis, and search functionality.

### Design

The system comprises three main components: the crawler for data collection, the indexer for text processing, and the processor for search functionality. The crawler initiates the process by traversing web pages and storing HTML content locally. The indexer then processes text documents using TF-IDF vectorization to generate feature vectors. Lastly, the processor utilizes a Flask API to receive search queries, corrects spelling errors, expands query terms with synonyms, and retrieves relevant documents based on cosine similarity scores.

### Architecture

- **Crawler (`crawler.py`)**:
  - Utilizes Scrapy library for web crawling.
  - Implements a CrawlSpider to follow links recursively.
  - Saves HTML content of crawled pages locally.
  
- **Indexer (`indexer.py`)**:
  - Uses sklearn's TfidfVectorizer for text document indexing.
  - Converts text documents into TF-IDF feature vectors.
  - Demonstrates basic usage of TF-IDF for text processing.
  
- **Processor (`processor.py`)**:
  - Implements a Flask API to handle search queries.
  - Corrects spelling errors in queries using the SpellChecker library.
  - Expands query terms with synonyms using NLTK's WordNet.
  - Calculates cosine similarity between query and indexed documents.
  - Returns top-k relevant search results.

### Operation

- **Commands**: 
  - Run `crawler.py` to initiate web crawling.
  - Run `indexer.py` to index text documents.
  - Run `processor.py` to start the Flask API for search functionality.

- **Inputs**: 
  - For the crawler: start URL, maximum pages, maximum depth.
  - For the processor: search queries in JSON format.

- **Installation**:
  - Install required libraries using pip (`scrapy`, `flask`, `scikit-learn`, `nltk`, `spellchecker`).
  - Ensure proper dependencies are installed.

### Conclusion

The system demonstrates successful integration of web crawling, text indexing, and search functionality. It effectively retrieves relevant documents based on user queries, despite potential spelling errors, and expands search terms using synonyms. However, further enhancements could include improved handling of large-scale data, optimization of indexing algorithms, and enhancing the user interface for better usability.

### Data Sources

- **Scrapy Documentation**: [Scrapy Documentation](https://docs.scrapy.org/en/latest/)
- **NLTK Documentation**: [NLTK Documentation](https://www.nltk.org/)
- **sklearn Documentation**: [sklearn Documentation](https://scikit-learn.org/stable/documentation.html)
- **Flask Documentation**: [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)

### Test Cases

- **Framework**: 
  - Utilize unit testing frameworks such as `unittest` or `pytest`.
  - Design test cases to cover various scenarios like successful crawling, accurate indexing, and relevant search results.
  - Implement mocks or fixtures for external dependencies.

### Source Code

- The source code listings for `crawler.py`, `indexer.py`, and `processor.py` are provided in the report.
- Detailed documentation and comments within the source code explain the functionality and usage of each component.
- Dependencies include `scrapy`, `flask`, `scikit-learn`, `nltk`, and `spellchecker`.

### Bibliography

- **Scrapy Documentation**: Scrapinghub Ltd. (2022). *Scrapy Documentation*. Retrieved from [https://docs.scrapy.org/en/latest/](https://docs.scrapy.org/en/latest/)
- **NLTK Documentation**: Bird, S., Loper, E., & Klein, E. (2009). *Natural Language Processing with Python*. O'Reilly Media.
- **sklearn Documentation**: Pedregosa, F., et al. (2011). *Scikit-learn: Machine Learning in Python*. Journal of Machine Learning Research, 12, 2825-2830.
- **Flask Documentation**: Pallets Projects. (2022). *Flask Documentation*. Retrieved from [https://flask.palletsprojects.com/en/2.0.x/](https://flask.palletsprojects.com/en/2.0.x/)

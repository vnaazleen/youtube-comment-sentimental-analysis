import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

def filter_comments(comments):
    no_of_comments = len(comments)
    # Stripping and deleting all the invisible break characters
    # U+FEFF was called a ZERO WIDTH NO-BREAK SPACE
    # Converting them into lowercase
    for i in range(0, no_of_comments):
        comments[i] = comments[i].strip('\ufeff')
        comments[i] = comments[i].lower()

    # Stop words are a set of commonly used words in a language. 
    # Examples of stop words in English are “a”, “the”, “is”, “are” and etc.
    # Stop words are commonly used in Text Mining and Natural Language Processing (NLP) 
    # to eliminate words that are so commonly used that they carry very little useful information.
    stop_words = set(stopwords.words('english'))

    filtered_comments = []
    for comment in comments:
        # Splitting the comment into tokens
        word_tokens = word_tokenize(comment)

        # Links in comments 
        links = [w for w in word_tokens if w.startswith('www.') or w.startswith('http')]

        # Mentions in comments
        mentions = [w for w in word_tokens if w.startswith('@')]

        # Eliminating stop words, links and mentions from comment
        filter = [w for w in word_tokens if w not in stop_words and w not in links and w not in mentions]

        filtered_comments.append(filter)
    
    return filtered_comments
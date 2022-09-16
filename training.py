import nltk
import random
import pickle
import os.path 
from nltk.corpus import movie_reviews

word_features = []

def train_classifier():
    '''
        Building & Training a Classifier model
    '''

    # checking if we have already created the model
    if(os.path.isfile("classifier.pickle")):
        return 

    documents = []
    for category in movie_reviews.categories():
        for fileid in movie_reviews.fileids(category):
            documents.append((list(movie_reviews.words(fileid)),category))

    # Getting all the words from movie reviews, converting them to lowercase
    all_words = []
    for w in movie_reviews.words():
        all_words.append(w.lower())

    # Creating a frequency map for words
    all_words = nltk.FreqDist(all_words)

    # Getting most common 9000 words and adding them to word features
    for w in all_words.most_common(9000):
        if(len(w[0]) >= 3):
            word_features.append(w[0])

    feature_sets = [(find_features(rev), category) for (rev, category) in documents]

    random.shuffle(feature_sets)

    # Training the classifier
    classifier = nltk.NaiveBayesClassifier.train(feature_sets[:2000])

    # Saving the classifier
    save_classifier = open("classifier.pickle","wb")
    pickle.dump(classifier,save_classifier)
    save_classifier.close()

def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
import pickle
import numpy as np
import yaml
import random
import spacy
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from keras.models import load_model

model = load_model('Model.h5')


intents = yaml.safe_load(open("data/intents.yaml").read())
words = pickle.load(open("data/words.pkl",'rb'))
classes = pickle.load(open("data/classes.pkl",'rb'))

# Get Intents    
def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence
def bow(sentence, words):
    
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                
    return(np.array(bag))

def predict_class(sentence, model= model):
    
    # filter predictions below a threshold
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = {"intent":classes[r[0]] for r in results}
    return return_list

# Get Entities
path = 'Name Entity Recognition'
nlp = spacy.load(path)

def NER(sentence):
    doc = nlp(sentence)
    result = {ent.label_: ent.text for ent in doc.ents}        
    return result
    
    
# Final Function That Return Natural Language Understanding For Utterance
def NLU(sentence):
    intent = predict_class(sentence)
    entity = NER(sentence)
    
    if entity == {}:
        result = {'Intent': intent['intent'],'Entities':None}
    else:
        result = {'Intent': intent['intent'],'Entities':entity}
        
    return result



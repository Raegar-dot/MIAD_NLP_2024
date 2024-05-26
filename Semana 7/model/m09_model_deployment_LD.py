#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#Asegurarse de tener descargados los recursos necesarios de NLTK
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')



def lemmatize_as_verb(text):
    words = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(w, pos='v') for w in words]


def predict_genre(vyear,vtitle,vplot):

    clf = joblib.load(os.path.dirname(__file__) + '/model_project2_v1.pkl') 
    vectorizer = joblib.load(os.path.dirname(__file__) + '/vectorizer.pkl') 
    

    # Create features
    var_year = int(vyear)
    var_title = str(vtitle)
    var_plot = str(vplot)
    

    print(var_year)
    print(var_title)
    print(var_plot)
    #media = 55072.956895
    #desviacion = 40880.96774371
    
    
    #df['Mileage'] = (var_mileage-media)/desviacion

    #df = pd.DataFrame(columns=['Year', 'Mileage','State','Make', 'Model'])
    X_test_dtm = vectorizer.transform(var_plot)

    data = {
        'year': [var_year],
        'title': [var_title],
        'plot': [var_plot], 
        }
    df = pd.DataFrame(data)

    print(df)


    # Make prediction
    p1 = clf.predict(X_test_dtm)

    return p1


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add an URL')
        
    else:

        vyear = sys.argv[1]
        vtitle = sys.argv[2]
        vplot = sys.argv[3]

        p1 = predict_genre(vyear,vtitle,vplot)
        
        print('Year: ' + str(vyear) + ' ' + 'Title: ' + str(vtitle) + ' '  + 'Plot: ' + str(vplot))
        print("Movie's Genre: ", p1)
        
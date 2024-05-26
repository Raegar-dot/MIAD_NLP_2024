#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os



def predict_genre(vyear,vtitle,vplot):

    clf = joblib.load(os.path.dirname(__file__) + '/model_project2_v1.pkl') 

    # Create features
    
    # make_code = pd.read_csv('df_make_code.csv')
    # make_dict = make_code.set_index('Make')['Code'].to_dict()

    # model_code = pd.read_csv('df_model_code.csv')
    # model_dict = model_code.set_index('Model')['Code'].to_dict()

    # state_code = pd.read_csv('df_state_code.csv')
    # state_dict = state_code.set_index('State')['Code'].to_dict()
    

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
    
    data = {
        'year': [var_year],
        'title': [var_title],
        'plot': [var_plot], 
        }
    df = pd.DataFrame(data)

    print(df)


    # Make prediction
    p1 = clf.predict(df)

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
        
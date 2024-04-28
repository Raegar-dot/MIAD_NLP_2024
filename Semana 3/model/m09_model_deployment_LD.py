#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os



def predict_price(year,mileage,state,make,model):

    Rgr = joblib.load(os.path.dirname(__file__) + '/CarPriceRegressor2.pkl') 

    # Create features
    
    make_code = pd.read_csv('df_make_code.csv')
    make_dict = make_code.set_index('Make')['Code'].to_dict()

    model_code = pd.read_csv('df_model_code.csv')
    model_dict = model_code.set_index('Model')['Code'].to_dict()

    state_code = pd.read_csv('df_state_code.csv')
    state_dict = state_code.set_index('State')['Code'].to_dict()
    

    var_year = int(year)
    var_mileage = float(mileage)
    var_state = int(state_dict[' '+ state.upper()])
    var_make = int(make_dict[make.upper()])
    var_model = int(model_dict[model.upper()])
    #media = 55072.956895
    #desviacion = 40880.96774371
    
    
    #df['Mileage'] = (var_mileage-media)/desviacion

    df = pd.DataFrame(columns=['Year', 'Mileage','State','Make', 'Model'])
    
    df['Year'] = var_year
    df['Mileage'] = var_mileage
    df['State'] = var_state
    df['Make'] = var_make
    df['Model'] = var_model
    
    



    # Make prediction
    p1 = Rgr.predict(df)

    return p1


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Please add an URL')
        
    else:

        year = sys.argv[1]
        mileage = sys.argv[2]
        state = sys.argv[3]
        make = sys.argv[4]
        model = sys.argv[5]

        p1 = predict_price(year,mileage,state,make,model)
        
        print('Year: ' + str(year) + ' ' + 'Mileage: ' + str(mileage) + ' '  + 'State: ' + str(state) + ' ' + 'Make: ' + str(make) + ' ' +'Model: ' + str(model))
        print("Car's Price: ", p1)
        
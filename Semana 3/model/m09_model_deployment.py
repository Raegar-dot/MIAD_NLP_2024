#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os



def predict_price(year,mileage,state,make,model):

    Rgr = joblib.load(os.path.dirname(__file__) + '/CarPriceRegressor.pkl') 

    # Create features
    
    col_names = pd.read_csv('model/col_nes.csv')['0'].to_list()
    
    var_state = state 
    var_make = make
    var_model = model
    var_model_short =  var_model[:4]
    var_year = int(year)
    var_mileage = float(mileage)
    media = 55072.956895
    desviacion = 40880.96774371
    
    df = pd.DataFrame(columns=col_names)

    for col in df.columns:
        if col.startswith('State_'):
            if col.split('_')[1] == var_state:
                df.loc[0, col] = 1
            else:
                df.loc[0, col] = 0

    for col in df.columns:
        if col.startswith('Make_'):
            if col.split('_')[1] == var_make:
                df.loc[0, col] = 1
            else:
                df.loc[0, col] = 0

    for col in df.columns:
        if col.startswith('Model_'):
            if col.split('_')[1] == var_model_short:
                df.loc[0, col] = 1
            else:
                df.loc[0, col] = 0

    df['Year'] = var_year

    df['Mileage'] = (var_mileage-media)/desviacion

    columnas_enteras = list(df.columns)
    columnas_enteras.remove('Mileage')
    for col in columnas_enteras:
        df[col] = df[col].astype(int)
    
    df = df.sort_index(axis=1)

    df.columns = df.columns.str.upper()



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
        
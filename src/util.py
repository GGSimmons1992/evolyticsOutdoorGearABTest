import pandas as pd
import math
from datetime import datetime

def tryParse(x):
    isnumber = True
    numberValue = math.nan
    try:
        numberValue = float(x)
        return isnumber,numberValue
    except ValueError:
        isnumber = False
        return isnumber,numberValue

def conversionPerUser(df):
    uniqueUsers = list(set(df['source_visitor_id']))
    conversionDictionary = {
        'user': [],
        'experimentalVisits': [],
        'ordersMade': [],
        'totalRevenueFromUser':[]
    }
    for user in uniqueUsers:
        conversionDictionary['user'].append(user)
        userDF = df[df['source_visitor_id'] == user]
        conversionDictionary['experimentalVisits'].append(userDF.shape[0])
        conversionDictionary['ordersMade'].append(userDF['purchase_flag'].sum())
        conversionDictionary['totalRevenueFromUser'].append(userDF['orderRevenue'].sum())
    conversionDF = pd.DataFrame(conversionDictionary,columns=list(conversionDictionary.keys()))
    conversionDF['conversionRate'] = conversionDF['ordersMade']/conversionDF['experimentalVisits']
    return conversionDF

def displayFeatureImportances(columns,fittedModel):
    importance = fittedModel.feature_importances_
    featureImportance = pd.DataFrame({
        "feature": columns,
        "featureImportance": importance
        },columns = ["feature","featureImportance"])
    featureImportancesSorted = featureImportance.sort_values(by="featureImportance", ascending=False)
    for i in range(10):
        featureRow = featureImportancesSorted.iloc[i]
        feature = featureRow['feature']
        featureValue = featureRow['featureImportance']
        print(f'Rank {i}: {feature}: score: {featureValue}')
        
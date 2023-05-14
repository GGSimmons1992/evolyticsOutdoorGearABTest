import math

def isNan(x):
    if type(x) != str:
        return math.isnan(x) or math.isinf(x)
    return x == 'nan'

def tryParse(x):
    isnumber = True
    numberValue = math.nan
    try:
        numberValue = float(x)
        return isnumber,numberValue
    except ValueError:
        isnumber = False
        return isnumber,numberValue
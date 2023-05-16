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

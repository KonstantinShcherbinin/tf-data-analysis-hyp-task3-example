import pandas as pd
import numpy as np
from scipy import stats


chat_id = 324151080 # Ваш chat ID, не меняйте название переменной

def solution(rvs1, rvs2) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t, pval = stats.ttest_ind(rvs1, rvs2, equal_var=False)
    #return pval
    if pval > 0.08:
        return True
    else:
        return False
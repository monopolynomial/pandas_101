import numpy as np
import pandas as pd
data=pd.DataFrame({'x1':[1,2,1],'x2':[4,5,6]})
data.sort_values('x1')
data.groupby('x1').sum()
data.sum(axis=1)# sum of each row
# great! any function can be used 😎
data.max(axis=1)
data.max(axis=0)


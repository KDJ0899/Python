'''
Created on 2018. 8. 12.

@author: user
'''
import numpy as np

xy=np.loadtxt('Data_01_test_score.csv',dtype=np.float32)
x_data=xy[:,0:-1]
y_data=xy[:,[-1]]

print(x_data.shape,x_data,len(x_data))
print(y_data.shape,y_data)
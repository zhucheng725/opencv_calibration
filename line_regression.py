

from sklearn.linear_model import LinearRegression
import numpy as np

'''get result
y = b0 + b1x
'''

x = np.array([2.58,1.0,0.9,1.99,2.6,2.71,2.75,2.17,5.18,7.51,7.44,7.6,7.9,6.11,6.47,3.95,7.96,8.54,9.49]).reshape((-1, 1))
y = np.array([2.75,1.75,1.36,2.47,3.26,2.9,3.09,2.7,6.5,10.9,10.79,11.08,11.1,7.71,8.8,4.76,12.16,15.40,18.51])

model = LinearRegression()
model = model.fit(x, y)
r_sq = model.score(x, y)
print('coefficient of determination(𝑅²) :', r_sq)
print('intercept:', model.intercept_)# （标量） 系数b0 intercept:
print('slope:', model.coef_)#（数组）斜率b1 slope

y_pred = model.predict(x)
#print('predicted response:', y_pred, sep='\n')
#predicted response:
#[8.33333333 13.73333333 19.13333333 24.53333333 29.93333333 35.33333333]

'''forecast'''
z = np.arange(5).reshape((-1, 1))
y = model.predict(z)
#print(y)
#







import sklearn.pipeline as pl
import sklearn.linear_model as lm
import sklearn.preprocessing as sp
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as sm

from sklearn.linear_model import LinearRegression


'''get result
y = b0 + b1x
b0 = intercept
b1--bn = coef
'''

x = np.array([2.58,1.0,0.9,1.99,2.6,2.71,2.75,2.17,5.18,7.51,7.44,7.6,7.9,6.11,6.47,3.95,7.96,8.54,9.49,1.45,2.8,1.92,2.52,3.78,4.7,5.19,6.72,1.98,2.48,2.95,1.75,2.3,2.96,1.89,1.8,1.79]).reshape((-1, 1))
y = np.array([2.75,1.75,1.36,2.47,3.26,2.9,3.09,2.7,6.5,10.9,10.79,11.08,11.1,7.71,8.8,4.76,12.16,15.40,18.51,1.42,3.23,2.84,3.11,4.43,5.6,6.5,9.11,2.55,2.87,3.19,2.52,2.92,3.2,2.71,3.15,3.45])


model = LinearRegression()
poly_feat = sp.PolynomialFeatures(1)
mo = model.fit(poly_feat.fit_transform(x),y )
print('mo.coef',mo.coef_)
print('mo.intercept_:',mo.intercept_)
r_sq = mo.score(poly_feat.fit_transform(x), y)
print('coefficient of determination(𝑅²) :', r_sq)
'''
print('mo.coef_[0]',mo.coef_[0])
print('mo.coef_[1]',mo.coef_[1])
print('mo.coef_[2]',mo.coef_[2])
print('mo.coef_[3]',mo.coef_[3])
'''
'''
def create(w0, w1, w2,w3, x):
    return w0+ w1*x + w2*x**2 + w3*x**3
'''
def create(w0, w1, x):
    return w0+ w1*x 

#print('pred', create(w0=mo.intercept_, w1=mo.coef_[1], w2=mo.coef_[2], w3=mo.coef_[3],x=x[0]))
print('pred', create(w0=mo.intercept_, w1=mo.coef_[1] ,x=x[0]))
print('--------------')
print('mo pred', mo.predict(poly_feat.fit_transform(x)))
print('--------------')

print('y', y)
print('--------------')

pred_y = mo.predict(poly_feat.fit_transform(x))

# 模型评估
print('平均绝对值误差：', sm.mean_absolute_error(y, pred_y))
print('平均平方误差：', sm.mean_squared_error(y, pred_y))
print('中位绝对值误差：', sm.median_absolute_error(y, pred_y))
print('R2得分：', sm.r2_score(y, pred_y))

# 绘制多项式回归线
px = np.linspace(x.min(), x.max(), 1000)
px = px.reshape(-1, 1)
pred_py = model.predict(poly_feat.fit_transform(px))


# 绘制图像
plt.figure("Poly Regression", facecolor='lightgray')
plt.title('Poly Regression', fontsize=16)
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.xlabel('x')
plt.ylabel('y')

plt.scatter(x, y, s=60, marker='o', c='dodgerblue', label='static data')
plt.plot(px, pred_py, c='orangered', label='PolyFit Line')
plt.tight_layout()
plt.legend()
plt.savefig('/media/zhu/0003E52A000920B8/procedure/calibration/test.jpg')







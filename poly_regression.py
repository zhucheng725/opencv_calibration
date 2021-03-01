

import sklearn.pipeline as pl
import sklearn.linear_model as lm
import sklearn.preprocessing as sp
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as sm


'''get result
y = b0 + b1x
'''

x = np.array([2.58,1.0,0.9,1.99,2.6,2.71,2.75,2.17,5.18,7.51,7.44,7.6,7.9,6.11,6.47,3.95,7.96,8.54,9.49]).reshape((-1, 1))
y = np.array([2.75,1.75,1.36,2.47,3.26,2.9,3.09,2.7,6.5,10.9,10.79,11.08,11.1,7.71,8.8,4.76,12.16,15.40,18.51])



# 创建模型
model = pl.make_pipeline(
    sp.PolynomialFeatures(3),  # 多项式特征拓展器
    lm.LinearRegression()  # 线性回归器
)

# 训练模型
model.fit(x, y)
# 求预测值y
pred_y = model.predict(x)

# 模型评估
print('平均绝对值误差：', sm.mean_absolute_error(y, pred_y))
print('平均平方误差：', sm.mean_squared_error(y, pred_y))
print('中位绝对值误差：', sm.median_absolute_error(y, pred_y))
print('R2得分：', sm.r2_score(y, pred_y))

# 绘制多项式回归线
px = np.linspace(x.min(), x.max(), 1000)
px = px.reshape(-1, 1)
pred_py = model.predict(px)


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






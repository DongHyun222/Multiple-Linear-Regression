# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import pandas as pd
import numpy as np
import statsmodels.api as sm

from statsmodels.formula.api import ols
from sklearn.model_selection import train_test_split
# -

pip install jupytext

#변수엑셀보면 편의를 위해 날짜랑 단위 제거
data = pd.read_excel("변수.xlsx")
data.head()

data.info()

#피어슨 상관계수
corr = data.corr(method = 'pearson').round(2)
corr

# +
from sklearn.model_selection import train_test_split
x = data[['오 존', '이산화질소', '일산화탄소', '아황산가스', '평균기온', '일강수량', '평균 풍속', '최다풍향', '평균 상대습도', '평균 현지기압']]
y = data[['PM10']]
#8:2로 테스트데이터 나눔

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=365)
# -

x.head()

y.head()

#선형회귀모델 구축
x_train = sm.add_constant(x_train)
model = sm.OLS(y_train, x_train, axis=1)
model_trained = model.fit()
model_trained.summary()







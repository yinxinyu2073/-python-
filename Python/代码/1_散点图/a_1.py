#!/usr/bin/env python
# coding: utf-8

#导包
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *
import math

#上传数据
data=pd.read_excel(r"C:/Users/YXY/Desktop/picture/Python/数据/1_散点图/data_1_1.xlsx")
# data
df=pd.DataFrame(
    {
        'x1':data['x1'],
        'x2':data['x2'],
        'y':data['fitness']
    }
)


# a_1 
# 标准散点图
# 库：pyplot
plt.scatter(df.index,df['x1'],c='red',s=1,marker='o')







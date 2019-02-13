# -*- coding: utf-8 -*-

"""
visualize.py

数据可视化工具函数库

@author: Gui jasper
@email: 
@date: 2019.02.13

---------------

FUNCTION LIST:
- df_sampling(df, nsamples, force=True)
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

import seaborn as sns
sns.set(style="darkgrid")


def visualizing_data(X, labels=None, title="scatter plot"):
    """
    可视化数据集
    @X <np.array>: X只有1列 -> histogram X有两列 -> scatter X>3列 -> tsne降为两列后绘制scatter
    @labels <1darray>: 每个样本对应的类别
    @title <str>: 图标题
    """
    if len(X.shape) == 1: # 确保Ｘ是２维数据
        X = X.reshape(-1, 1)
    n_col = X.shape[1]
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    colors=['b','g','r','c','m','y','k','chocolate','gold','lightgrey', 'skyblue', 'lime']
    if n_col == 1:
        ax.hist(X[:, 0])
    else:

        if n_col > 2:
            X_ = (X - X.min(0)) / (X.max(0) - X.min(0))
            X = TSNE(n_components=2, random_state=0).fit_transform(X_)
        if labels is not None:
            unique_labels = set(labels)
            for i in unique_labels:
                ax.scatter(X[labels==i, 0], X[labels==i, 1], c=colors[i], edgecolor='k', label=i)
                ax.legend()     
        else:
            ax.scatter(X[:, 0], X[:, 1])
    plt.title(title)


# -*- coding: utf-8 -*-

"""
datetime_utils.py

时间处理相关工具函数

@author: Jasper Gui
@email:
@date: 2019.3.5

---------------

FUNCTION LIST:
"""
import matplotlib.pyplot as plt
import numpy as np


def plot_some_imgs_each_cluster(im_list, save=0, name=""):
    """
    ONLY IMAGES CLUSTERING
    display some samples for each cluster
    @im_list <np.array>: [n_samples, height, weight, channel]
    """
    plt.figure(figsize=(20,20))
    for i, array in enumerate(im_list):
        plt.subplot(1, len(im_list), i+1)
        plt.imshow(array[:,:,::-1])
        plt.axis('off')
    if save:
        plt.savefig(r"C:\temp\{}.png".format(names))
    plt.show()



def show_lots_imgs_on_one_cluster(X, cluster_number, pages_of_images=5):
    """
    Show lots of images from cluster X.
    """
    
    # Grab the selection of images.
    X_selection = X[np.random.choice(np.where(km.labels_==cluster_number)[0], 9*pages_of_images)]
    
    # Plot 'em.
    print('Showing cluster {}'.format(cluster_number))
    for i in range(pages_of_images):
        plot_some_imgs_each_cluster(X_selection[i*9:(i+1)*9])
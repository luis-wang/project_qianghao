#coding:utf-8
#基于python2.7
'''

'''
import os, sys,time
import cv2
import numpy as np
from matplotlib import pyplot as plt
sys.path.append(r'D:\data\aptana34workspace\openvc_demo\1tutroals\Image-Processing-in-OpenCV')
from Simple_Thresholding import simple_threshod_output

def tune_best_thresh(path):
    """调节最佳的threshold"""
    
    for file in os.listdir(path):
        if file.endswith('.jpg'):
            filepath = dir + file
            print 'filepath:',filepath
            grayimg = cv2.imread(filepath,0)
            
            output = simple_threshod_output(grayimg,245)

            titles = ['BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
        
            for i in xrange(5):
                plt.subplot(2,3,i+1),plt.imshow(output[i], 'gray')
                plt.title(titles[i])
                plt.xticks([]),plt.yticks([])
         
            plt.show()    

if __name__ == '__main__':
    
    dir = 'E:/2kkkkk/cheliang_captcha/rgb/'
    tune_best_thresh(dir)







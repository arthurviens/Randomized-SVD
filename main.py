import matplotlib.pyplot as plt
import numpy as np
from math import ceil, log10
from time import perf_counter
from utils import *
from svd_func import *
from profiler import *

if __name__ == "__main__":
    # Transform the image in a matrix
    img = getColouredImage('./resources/small_6946x3906.jpg')
    # img = getColouredImage('./resources/big_12k×8k.jpg')
    # img = getColouredImage('./resources/huge_12kx14k.jpg')

    img = toGrayScale(img)

    A = np.array(img).transpose() #we transpose because the pic is horizontal

    m, n = A.shape
    size = m * n
    
    print("Matrix shape :", A.shape)
    print("Total number of pixels:", size)

    k = 500
    print("k : ", k) #Numbers of colums to project for estimation 



    ############################################################
    ############################################################
    ############################################################
    #Computing regular SVD
    # start = perf_counter()  
    # A_tilde = svd_regular(A)
    # end = perf_counter()
    
    # print("\n####################################################################")
    # print("Regular SVD")
    # print(">>> Duration : {:.5f} sec.".format(end-start))
    # rms = abs(np.linalg.norm(A - A_tilde))
    # rms_magnitude = ceil(log10(rms/size))
    # print(">>> Error magnitude : 10e" + str(rms_magnitude))
    # print(">>> Exact error RMS : " + str(rms))
    # print("####################################################################")


    # plt.figure(figsize=figsize)
    # plt.title("Regular SVD")    
    # plt.imshow(A_tilde.T, cmap='gray')

    ############################################################
    ############################################################
    ############################################################
    #Computing randomized svp with uniform random (random features)

    #execute_t_times(20, svd_rand_uniform, A, k) 


    # print_result(err, mag, dur, "Randomized uniform")

    # plt.figure(figsize=figsize)
    # plt.title("Randomized uniform SVD image")    
    # plt.imshow(A_tilde.T, cmap='gray')

    # start = perf_counter()  
    # A_tilde = svd_rand_uniform(A, k)
    # end = perf_counter()

    # print("\n####################################################################")
    # print("Randomized SVD using uniform law")
    # print(">>> Duration : {:.5f} sec.".format(end-start))
    # rms = abs(np.linalg.norm(A- A_tilde))
    # rms_magnitude = ceil(log10(rms/size))
    # print(">>> Error : 10e" + str(rms_magnitude))
    # print(">>> Exact error RMS : " + str(rms))
    # print("####################################################################")



    # ############################################################
    # ############################################################
    # ############################################################
    # #Randomized SVD using random columns
    # start = perf_counter()  
    # A_tilde = svd_rand_columns(A, k)
    # end = perf_counter()

    # print("\n####################################################################")
    # print("Randomized columns SVD")
    # print(">>> Duration : {:.5f} sec.".format(end-start))
    # rms = abs(np.linalg.norm(A - A_tilde))
    # rms_magnitude = ceil(log10(rms/size))
    # print(">>> Error : 10e" + str(rms_magnitude))
    # print(">>> Exact error RMS : " + str(rms))
    # print("####################################################################")

    # plt.figure(figsize=figsize)
    # plt.title("Randomized by colums SVD image")    
    # plt.imshow(A_tilde.T, cmap='gray')


    # # ############################################################
    # # ############################################################
    # # ############################################################
    # # #Randomized SVD using gaussian matrix
    # start = perf_counter()  
    # A_tilde = svd_rand_gaussian(A, k)
    # end = perf_counter()

    # print("\n####################################################################")
    # print("Randomized SVD using Gaussian law")
    # print(">>> Duration : {:.5f} sec.".format(end-start))
    # rms = abs(np.linalg.norm(A - A_tilde))
    # rms_magnitude = ceil(log10(rms/size))
    # print(">>> Error : 10e" + str(rms_magnitude))
    # print(">>> Exact error RMS : " + str(rms))
    # print("####################################################################")

    # plt.figure(figsize=figsize)
    # plt.title("Gaussian random SVD image")    
    # plt.imshow(A_tilde.T, cmap='gray')

    # plt.show()
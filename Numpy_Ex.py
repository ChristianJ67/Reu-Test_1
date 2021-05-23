import math
import numpy as np
import matplotlib.pyplot as plt
class MyLinReg:
    
    @staticmethod
    def mean(nd_a):
        """
        return the mean of the ndarray given
        """
        return np.sum(nd_a)/len(nd_a)

    @staticmethod
    def covar(cls, nd_a,nd_b):
        """
        return the covariance between the two ndarrays given
        asssume the mean is a sample mean, and therefore the denominator
        for calculating the convariance is one less then the number 
        of data points.
        """
        assert len(nd_a)==len(nd_b)
        a = nd_a - cls.mean(nd_a)
        b = nd_b - cls.mean(nd_b)
        return np.dot(a,b)/(len(a)-1)

    @staticmethod
    def var(cls, nd_a):
        """
        return the variance of the ndarray given
        """
        return cls.covar(nd_a,nd_a)

    @staticmethod
    def stddev(cls, nd_a):
        """
        return the standard deviation of the ndarray given
        """
        return np.sqrt(cls.var(nd_a)) 
    
    @staticmethod
    def pearson(cls, nd_a,nd_b):
        """
        return the Pearson R between the two ndarrays given
        """
        return cls.covar(nd_a,nd_b)/(cls.steddev(nd_a) * cls.steddev(nd_b))

    @staticmethod
    def linear_regression(cls,x,y):
        """
        do the linear regression between the two ndarrays given and 
        return a tuple with the slope, intercept, and a lambda 
        implementing the linear transformation of the regression.
        """
        m = cls.pearson(x,y)*cls.steddev(y)/cls.steddev(x)
        b = m*cls.mean(x) - cls.mean(y)
        rl = lambda x: m*x + b
        return(m,b,rl)
    
    

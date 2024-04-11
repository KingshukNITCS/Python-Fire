'''
Suppose a given restaurant receives an average of 100 customers per day. We can use the Poisson Distribution to find the probability that the restaurant receives 120 customers on a certain day.

So, we first import the libraries and then apply Poisson Distribution.
'''

from scipy.stats import poisson 
from matplotlib import pyplot as plt
poisson.pmf(120,100)

# Next, Let us generate a Poisson Distribution with sample size 10000.

x = poisson.rvs(mu = 3, size = 10000)

# Upon doing this we get a series of array with 10000 values but the average of the entire series is 3.

# Now let us plot this x with its Probability so that all the values get normalised to less than 1.

plt.hist(x, density = True, edgecolor = "Black")

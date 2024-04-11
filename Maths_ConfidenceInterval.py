'''
Confidence Interval is a range where we are certain that true value exists. The selection of a confidence level for an interval determines the probability that the confidence interval will contain the true parameter value. This range of values is generally used to deal with population-based data, extracting specific, valuable information with a certain amount of confidence, hence the term ‘Confidence Interval’. 
'''

'''
Method 1: Calculate confidence Intervals using the t Distribution
This approach is used to calculate confidence Intervals for the small dataset where the n<=30 and for this, the user needs to call the t.interval() function from the scipy.stats library to get the confidence interval for a population means of the given dataset in python.

Syntax: st.t.interval(alpha, length, loc, scale)) 

Parameters:

alpha: Probability that an RV will be drawn from the returned range.
length: Length of the data set
loc: location parameter
scale: scale parameter

In this example, we will be using the data set of size(n=20) and will be calculating the 90% confidence Intervals using the t Distribution using the  t.interval() function and passing the alpha parameter to 0.90 in the python.
'''


import numpy as np
import scipy.stats as st

# define sample data
gfg_data = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3,
			3, 4, 4, 5, 5, 5, 6, 7, 8, 10]

# create 90% confidence interval
st.t.interval(alpha=0.90, df=len(gfg_data)-1,
			loc=np.mean(gfg_data),
			scale=st.sem(gfg_data))

# Output: (2.962098014195961, 4.837901985804038)

'''
In this example, we will be using the data set of size(n=20) and will be calculating the 90% confidence Intervals using the t Distribution using the  t.interval() function and passing the alpha parameter to 0.99 in the python.
'''

import numpy as np
import scipy.stats as st

# define sample data
gfg_data = [1, 1, 1, 2, 2, 2, 3, 3, 3,
			3, 3, 4, 4, 5, 5, 5, 6,
			7, 8, 10]

# create 99% confidence interval
st.t.interval(alpha=0.99,
			df=len(gfg_data)-1,
			loc=np.mean(gfg_data),
			scale=st.sem(gfg_data))

# Output: (2.3481954013214263, 5.4518045986785735)

'''
Interpretation from example 1 and example 2:

In the case of example 1, the calculated confident mean interval of the population with 90% is (2.96-4.83), and in example 2 when calculated the confident mean interval of the population with 99% is (2.34-5.45), it can be interpreted that the example 2 confident interval is wider than the example 1 confident interval with the 95% of the population, which means that there are 99% chances the confidence interval of [2.34, 5.45] contains the true population mean
'''


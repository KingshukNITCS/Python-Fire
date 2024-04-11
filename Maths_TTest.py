'''
A t-test is a type of inferential statistic used to determine if there is a significant difference between the means of two groups, which may be related in certain features.

If t-value is large => the two groups belong to different groups. 

If t-value is small => the two groups belong to same group.

t-tests are widely used in the fields of research in hospitals by experts to gain important information about the medical data given to them about effects of various medicines and drugs on the population and helps them draw out important inferences regarding the same. However, it is the responsibility of the person to see to it that which t-test would bring out the best results and that all the assumptions of that t-test are adhered to.
'''
'''
The one-sample t-test is a statistical hypothesis test that can be used to see if the mean of an unknown population differs from a given or known value. In this article let’s learn how to perform a one-sample t-test.

null hypothesis: the mean of the areas is 5000.

alternative hypothesis: the mean of the areas is not  5000.
'''

# import packages
import scipy.stats as stats
import pandas as pd

# loading the csv file
data = pd.read_csv('areas.csv')
data.head()


'''
Conduct a One Sample T-Test in Python
To perform one-sample t-test we will use the scipy.stats.ttest_1samp() function to perform one- sample t-test. The T-test is calculated for the mean of one set of values. The null hypothesis is that the expected mean of a sample of independent observations is equal to the specified population mean, popmean.

Syntax: scipy.stats.ttest_1samp(a, popmean, axis=0).

parameters:

a : an array or iterable object of sample observations.
popmean : expected mean in the null hypothesis.
axis : its an optional parameter. represents axis.
returns : t statistic and two tailed p value.
'''

# import packages
import scipy.stats as stats
import pandas as pd

# loading the csv file
data = pd.read_csv('areas.csv')

# perform one sample t-test
t_statistic, p_value = stats.ttest_1samp(a=data, popmean=5000)
print(t_statistic , p_value)


'''
Output:

[-0.79248301] [0.44346471]
Here

t_statistic is  -0.79248301

p-value is 0.44346471

As the p_value for the given problem is more than 0.05 which is the alpha value, we accept the null hypothesis and the alternative hypothesis is rejected.
'''

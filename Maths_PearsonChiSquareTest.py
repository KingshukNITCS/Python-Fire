'''
Pearson’s Chi-Square is a statistical hypothesis test for independence between categorical variables. We will perform this chi-square test first using a mathematical approach and then using Python’s scipy module. 

Let us know some terms before we understand the chi-square distribution 

The Contingency table (also called crosstab) is used in statistics to summarise the relationship between several categorical variables. Here, we are taking a table that shows the number of men and women buying different types of pets.

A null Hypothesis is a general statistical statement or assumption about a population parameter that is assumed to be true Until we have sufficient evidence to reject it.
It is generally denoted by Ho.

The Alternate Hypothesis is considered as competing of the null hypothesis. It is generally denoted by H1. The general goal of our hypothesis testing is to test the Alternative hypothesis against the null hypothesis. 

P-value is used as a measure of evidence against the null hypothesis. If it is greater than our level of significance then we will accept our null hypothesis.
'''

'''
Performing the test using Python (scipy. stats) : 

SciPy is an Open Source Python library, which is used in mathematics, engineering, scientific and technical computing.  

Installation: To install scipy in our notebook, we will use this command.

pip install scipy
The chi2_contingency() function of scipy.stats module takes the contingency table element in 2d array format and it returns a tuple containing test statistics,  p-value, degrees of freedom, and expected table(the one we created from the calculated values) in that order.  Here, we need to compare the obtained p-value with an alpha value of 0.05. 
'''

from scipy.stats import chi2_contingency

# defining the table
data = [[207, 282, 241], [234, 242, 232]]
stat, p, dof, expected = chi2_contingency(data)

# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
	print('Dependent (reject H0)')
else:
	print('Independent (H0 holds true)')


'''
Output : 

p value is 0.1031971404730939
Independent (H0 holds true)
Since,

p-value > alpha 

Therefore, we accept H0, which shows that our variables do not have a significant relation.
'''

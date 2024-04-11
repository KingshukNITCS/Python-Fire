'''
Say we have a quiz of 20 MCQ Q's, only one option is correct out of 4 Options.

P( Getting a Question Correct ) = 1/4 = 0.25.

Lets implement the concept on Jupyter Notebook.

First we Import the necessary Library
'''

import pandas as pd
from scipy.stats import binom

# Next We take the variables
number_of_trials = 20
prob_of_success = 0.25

# Now We calculate the Binomial Values
binom.pmf(6, number_of_trials, prob_of_success)

# Next we calculate the probability of success for each occurrence.
successes = list(range(0,number_of_trials+1))
df = pd.DataFrame(successes)
df = df.rename(columns = {0:"Number_of_successes"})
probability = lambda x : binom.pdf(x, number_of_trials, prob_of_success)
df["Probability"] = df["Number_of_successes"].apply(probability)

# Now Let's Plot a bar graph to graphically display our findings.
plot = (x = "Number_of_successes", y = "Probability", kind = "bar")

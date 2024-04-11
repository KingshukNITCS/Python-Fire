import pandas as pd
from scipy.stats import binom

number_of_trials = 20
prob_of_success = 0.25

binom.pmf(6, number_of_trials, prob_of_success)

successes = list(range(0,number_of_trials+1))
df = pd.DataFrame(successes)
df = df.rename(columns = {0:"Number_of_successes"})
probability = lambda x : binom.pdf(x, number_of_trials, prob_of_success)
df["Probability"] = df["Number_of_successes"].apply(probability)

plot = (x = "Number_of_successes", y = "Probability", kind = "bar")

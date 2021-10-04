import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the csv file
edu = pd.read_csv('StudentsPerformance.csv')

# QUESTION ONE: Does completing a test preparation course make a difference in test scores?
# Here are those with no test prep:

no_prep = edu[edu['test preparation course'] == 'none']
print(no_prep.mean())

# Here are those who've completed a test prep course:
prep = edu[edu['test preparation course'] == 'completed']
print(prep.mean())


# QUESTION TWO: Assuming lower income families receive the free/reduced lunch, how does family income effect test scores?

# stand in the standard lunch
# f_r is the free/reduced lunch
stand = edu[edu['lunch'] == 'standard'].mean()
f_r = edu[edu['lunch'] == 'free/reduced'].mean()
print(stand)
print(f_r)

# QUESTION THREE: Is race a factor in test scores?

print('Group A')
g_a = edu[edu['race/ethnicity'] == 'group A'].mean()
print(g_a)

print('Group B')
g_b = edu[edu['race/ethnicity'] == 'group B'].mean()
print(g_b)

print('Group C')
g_c = edu[edu['race/ethnicity'] == 'group C'].mean()
print(g_c)

print('Group D')
g_d = edu[edu['race/ethnicity'] == 'group D'].mean()
print(g_d)

# As an example of a visual representation, here is a graph showing the means of the math scores for those with test prep versus without.
sns.countplot(data=edu, x='test preparation course')
sns.boxplot(x='test preparation course',
            y='math score',
            data=edu,
            showmeans=True)
plt.ylabel('Math Score')
plt.xlabel('Test Preparation')
plt.title('Test Prep & Math Scores')
plt.show()

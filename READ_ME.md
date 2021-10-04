# Overview

I am learning some basic data analysis, starting with the Pandas Library. I hope to one day improve my learning to serious data science.

This data set includes information on the following data:  
* Gender
* Race/Ethnicity
* Parental level of education
* Lunch Payments
* Test preparation course
* Math scores
* Reading scores
* Writing scores

I downloaded this database from Kaggle.
[Data set link here](https://www.kaggle.com/spscientist/students-performance-in-exams)


In this analysis I'm looking at race, income and test preparation to see if any of it has an effect on scoring outcome.  


[Software Demo Video](https://youtu.be/6WsgsEtsHCo)

# Data Analysis Results

QUESTION ONE: Does completing a test preparation course make a difference in test scores?
Here are the average results with no test prep:

    ANALYSIS: There is between a 5-10 point improvement in mean score, so it is worth it for students to invest in some test preparation.

QUESTION TWO: Assuming lower income families receive the free/reduced lunch, how does family income effect test scores?

    ANALYSIS: This was much more dramatic. Here there was a 7 to 12 point difference in scores with those of higher income families fairing better. Math showing the biggest difference.

QUESTION THREE: Is race a factor in test scores? 
    ANALYSIS: Group A consistently had the lowest test scores and Group D consistently had the highest. 
        There was a 6-8 point difference in most cases. 

# Development Environment

I used PyCharm for my environment this time in order to compare it with VScode that I used in my last video. 
This is less cluttered and I seem to prefer it, so far. 

    Programming languages and packages:
    * Python language
    * Pandas (for data analysis)
    * Matplotlib (for aid with seaborn)
    * Seaborn (to add a visual graphical component)

# Useful Websites

* [Python documentation](https://docs.python.org/3/)
* [Pandas documentation](https://pandas.pydata.org/docs/user_guide/index.html)
* [Seaborn documentatioin](https://seaborn.pydata.org/)

# Future Work

I plan on continuing to build this. 
* Part of my code will be deprecated in the future, therefore I need to learn what is replacing it. 
* I want to find another dataset to join with this one to see if school funding amounts are a contributor in test scores.
* I'd like to update the visualization with more comprehensive boxplots.
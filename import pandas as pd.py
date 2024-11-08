


import pandas as pd

data = pd.read_csv("S:\downloads\HW 2\LoanDataset - LoansDatasest.csv\LoanDataset - LoansDatasest.csv")

#print(data.head())

import matplotlib.pyplot as plt

'''
plt.plot(data['customer_age'], data["customer_income"], marker='o', color='r')
plt.xlabel('Age')
plt.ylabel('Income')
plt.title('Age vs Income')
plt.tight_layout()  

plt.show()

'''



#^^For the above code

#I was curious if age had any correlation with income, so I plotted the data to see if there was any correlation.

#Needless to say there was no correlation between age and income.

#the plot is beyond salvaging rip





'''
import matplotlib.pyplot as plt

loan_intent_counts = data['loan_intent'].value_counts() 
plt.bar(loan_intent_counts.index, loan_intent_counts.values)
plt.xlabel('Loan purpose')
plt.ylabel('Count')
plt.title('Number of poans by purpose')
plt.xticks(rotation=405)  
plt.show()


'''


#In the above code i decided to figure out how often loans are taken out and for what purpose

#thankfully this bar chart is actually functional unlike my last attempt at the line plot
#This gives us insight into just why most people take loans out and is very useful information for people in financial fields

'''
import matplotlib.pyplot as plt


avg_interest_by_term = data.groupby('term_years')['loan_int_rate'].mean()

plt.plot(avg_interest_by_term.index, avg_interest_by_term.values, marker='o')
plt.xlabel('Loan Term (Years)')
plt.ylabel('Average Interest Rate (%)')
plt.title('Average Interest Rate by Loan Term')
plt.show()

'''


'''
A chance at redemption on the line plot and it seems to be working well

Its supposed to visualize the relationship between loan term and the average interest rate
As the loan term is longer, we see that the interest rate makes an exponential jump,
suggesting that the longer the term of a loan is, the more interest you are looking at.

'''

import matplotlib.pyplot as plt


avg_age_by_home_ownership = data.groupby('home_ownership')['customer_age'].mean()
plt.bar(avg_age_by_home_ownership.index, avg_age_by_home_ownership.values)
plt.xlabel('Home Ownership Status')
plt.ylabel('Average Age')
plt.title('Average Age by Home Ownership Status')
plt.show()


# for this bar chart i decided to do the average age of customers based on homeownership status

#shows us the general age of customers with homes and gives us insight into different types of home ownership like ren or mortgage.
#also theres only a few categories in home_ownership so a bar chart is a clean way to display this information




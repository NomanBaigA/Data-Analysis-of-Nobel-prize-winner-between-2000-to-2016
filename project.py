import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

'''
####### FINAL PROJECT FOR CODE IN PLACE 2021 #######

This is Data Science project about the Nobel prize winners between 2000 to 2016. after running this
program we get 3 graph which shows different data about Nobel prize.
'''

def main():
    #Read data from .csv file
    nobel = pd.read_csv("nobelData.csv", parse_dates = True)

    #Plotting the top category, which category won the most Nobel Prizes
    by_category(nobel)

    #Plotting the top Country, which Country won the most Nobel Prizes
    by_country(nobel)

    #Plotting the top organization, which organization won the most Nobel Prizes
    by_organization(nobel)


def by_category(nobel):
    #Read data from category column
    category = nobel['Category'].value_counts()

    #Plotting Bar
    sns.barplot(x = category.index, y = category.values)

    #This code helps category name to be vertical
    plt.xticks(rotation = 90)

    #sets the title on graph
    plt.title('Nobel Prizes by Category (2000 to 2016)')

    #save graph as an image
    plt.savefig("for_category.png", bbox_inches = 'tight')

    #close plot
    plt.close()


def by_country(nobel):
    #Read data from Birth Country column
    country = nobel['Birth Country'].value_counts().head(10)

    #Plotting Bar
    sns.barplot(x = country.index, y = country.values)

    #This code helps Country names to be vertical
    plt.xticks(rotation= 90)

    #sets the title on graph
    plt.title('Top 10 Countries, which got the nobel prizes the most')

    #save graph as an image
    plt.savefig("for_country.png", bbox_inches = 'tight')

    #close plot
    plt.close()


def by_organization(nobel):
    #Read data from organization column
    organization = nobel['Organization Name'].value_counts().reset_index().head(10)

    #Plotting Bar
    sns.barplot(x = 'Organization Name', y = 'index', data = organization)

    #This code helps count numbers to be vertical
    plt.xticks(rotation = 90)

    #sets the title on graph
    plt.ylabel('Organization Name')

    #sets the title on graph
    plt.xlabel('Count')

    #save graph as an image
    plt.savefig("for_organization.png", bbox_inches = 'tight')

    #close plot
    plt.close()


if __name__ == '__main__':
    main()

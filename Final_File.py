# Assignment No. 01 
# Applied Data Science - 01
# Visualisation with three different types of plots.
# Muhammad Hamza Zafar
# Student ID : 22022247


import pandas as pd
import matplotlib.pyplot as plt

# Load data into a pandas dataframe

titanic     = pd.read_csv('train.csv')         # For Histogram and Pie Graph Representation.
vaccination = pd.read_csv('vaccinations.csv')  # For Bar-Stacked Plot and Line Graph Representation.

#Generating Line Plot

def create_line_plot(covid_vaccinations,x_label,y_label,title):
    
    """
Creates a line plot for COVID-19 vaccination data showing top 5 countries vaccination.

Parameters:
covid_vaccinations (pandas.DataFrame): A DataFrame containing COVID-19 vaccination data.
x_label (str): The label for the x-axis.
y_label (str): The label for the y-axis.
title (str): The title of the plot.

Returns:
None,Lines plot
"""
    
    
    country_vaccinations = covid_vaccinations.groupby('location').agg({'total_vaccinations': 'max'}).sort_values('total_vaccinations', ascending=False).head(5)
    # Filter the original data to include only the top 5 countries
    top_5_countries = covid_vaccinations[covid_vaccinations['location'].isin(country_vaccinations.index)]
    # Convert date column to datetime format
    top_5_countries['date'] = pd.to_datetime(top_5_countries['date'])

    # Create a line plot for each country
    plt.figure(figsize=(10, 6))
    for country in top_5_countries['location'].unique():
        country_data = top_5_countries[top_5_countries['location'] == country]
        plt.plot(country_data['date'], country_data['total_vaccinations'],linestyle='-', marker='o', label=country)

    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    # Add legend
    plt.legend()
    # Add grid
    plt.grid(True)
    # Show the plot
    plt.savefig('lineplot.png')
    plt.show()
  

# Generating a Bar Stacked plot 

def create_stackedplot(vaccination,x_label,y_label,legend,title):
    
    """
Creates a stacked bar plot for COVID-19 vaccination data.

Parameters:
vaccination (pandas.DataFrame): A DataFrame containing COVID-19 vaccination data.
x_label (str): The label for the x-axis.
y_label (str): The label for the y-axis.
legend (list): The list of labels for the legend.
title (str): The title of the plot.

Returns:
None, Bar stacked plot.
"""
    
    # group data by country and select the latest vaccination data
    top_15 = vaccination.groupby('location')['people_vaccinated', 'people_fully_vaccinated'].max().sort_values('people_fully_vaccinated', ascending=False).head(15)

    # create the stacked bar chart
    top_15.plot(kind='bar', stacked=True)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend(legend)
    plt.savefig('Stackedbarplot.png')
    plt.show()
    
    

# Generating Histogram Plot

def create_histogram(titanic, x_label, y_label, title, bins=20, color='blue', edgecolor='black', alpha=0.5):
    
    """
Creates a histogram plot of the 'Age' column of the titanic dataset.
    Parameters:

titanic : pandas DataFrame
    A pandas DataFrame containing the titanic dataset.
x_label : str
    Label for the x-axis of the plot.
y_label : str
    Label for the y-axis of the plot.
title : str
    Title of the plot.
bins : int, optional (default=20)
    Number of bins to use for the histogram.
color : str, optional (default='blue')
    Color of the bars in the histogram.
edgecolor : str, optional (default='black')
    Color of the edges of the bars in the histogram.
alpha : float, optional (default=0.5)
    Opacity of the bars in the histogram.

Returns:
--------
None, A histogram plot.
"""
    
    plt.hist(titanic['Age'], bins=bins, color=color, edgecolor=edgecolor, alpha=alpha)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel(x_label, fontsize=12, fontweight='bold')
    plt.ylabel(y_label, fontsize=12, fontweight='bold')
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', alpha=0.75)
    plt.show()
    plt.savefig('histogram.png')

 

# Generating PIE plot

def create_pie_subplots(data):
    
    """
Creates a Figures with subplots. It creates three different plots, one is the Gender representation of Titanic Passenger,second is comparison ticket prices paid by male and female,and the last one is the survival rate of titanic between male and female.
    
    Parameters:
        
data : pandas DataFrame
    A pandas DataFrame containing the data to be plotted.

Returns:
None, Three Pie plots.
"""

    # Filter the data by sex
    sex_counts = data['Sex'].value_counts()

    # Calculate the ticket prices by sex
    grouped_df = data.groupby(['Sex'])['Fare'].sum().reset_index()

    # Calculate the number of passengers who survived and didn't survive
    survived_counts = data['Survived'].value_counts()

    # Create a subplot with three pie charts
    fig, axs = plt.subplots(1, 3, figsize=(10, 5))

    # Plot the first pie chart for male and female passengers
    labels = ['Male', 'Female']
    sizes = [sex_counts['male'], sex_counts['female']]
    colors = ['green', 'red']
    explode = (0.1, 0)  # explode the first slice
    axs[0].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    axs[0].set_title('Proportion of Male and Female Passengers')
    axs[0].legend(labels, loc='best')

    # Plot the second pie chart for ticket prices by sex
    labels = grouped_df['Sex']
    sizes = grouped_df['Fare']
    colors = ['lightblue', 'grey']
    explode = (0.1, 0)  # explode the first slice
    axs[1].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    axs[1].set_title('Ticket Prices by Sex')
    axs[1].legend(labels, loc='best')

    # Create a pie chart for survival rate
    labels = ['Did not survive', 'Survived']
    sizes = [survived_counts[0], survived_counts[1]]
    colors = ['purple', 'orange']
    explode = (0.1, 0)  # explode the first slice
    axs[2].pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    axs[2].set_title('Titanic Survival Rate')
    axs[2].legend(labels, loc='best')

    # Show the plot
    plt.savefig('Pie.png')
    plt.show()
    
    


#Calling all the Functions
create_line_plot((vaccination),"Date","Total Vaccination","COVID-19 VACCINATION BY COUNTRY(TOP-5)")
create_stackedplot(vaccination, 'Country', 'Number of People Vaccinated', ['At least one dose', 'Fully vaccinated'], 'Vaccination Status of Top 15 Countriesdefine')
create_histogram(titanic, 'Age', 'Count', 'Age Distribution on Titanic')
create_pie_subplots(titanic)

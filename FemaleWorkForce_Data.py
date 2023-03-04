import pandas as pd
import matplotlib.pyplot as plt
# Read in the data
data = pd.read_csv(r'C:\Users\pruth\OneDrive - University of Hertfordshire\Desktop\2nd final.py')
def plot_line_graph(df):
    # Select the top 6 countries by average percentage
    top_countries = df.sort_values(by='Average Percentage', ascending=False).head(6)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Loop through the top countries and plot their data as a line graph
    for country in top_countries['Country Name']:
        ax.plot(range(2002, 2022), top_countries.loc[top_countries['Country Name'] == country, '2002':'2021'].values[0], label=country)

    # Add axis labels and a legend
    ax.set_xlabel('Year')
    ax.set_ylabel('Employment to population ratio, 15+, female (%)')
    ax.set_title('Top 6 countries by average percentage')
    ax.legend()
    
    plt.show()


def plot_pie_chart(df):
    # Select the top 6 countries by average percentage
    top_countries = df.sort_values(by='Average Percentage', ascending=False).head(6)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 8))

    # Plot the pie chart
    ax.pie(top_countries['Average Percentage'], labels=top_countries['Country Name'], autopct='%1.1f%%', shadow=True)

    # Add a title
    ax.set_title('Top 6 countries by Average Percentage')
    
    plt.show()
    
def plot_bar_graph(df):
    # Select the top 6 countries by employment to population ratio in 2021
    top_countries = df[['Country Name', '2021']].sort_values(by='2021', ascending=False).head(6)

    # Set up the plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the bar graph
    ax.bar(top_countries['Country Name'], top_countries['2021'])

    # Add axis labels and a title
    ax.set_xlabel('Country')
    ax.set_ylabel('Employment to population ratio, 15+, female (%)')
    ax.set_title('Top 6 countries by employment to population ratio in 2021')
    
    plt.show()


# Plot the line graph
plot_line_graph(data)

# Plot the pie chart
plot_pie_chart(data)

# Plot the bar graph
plot_bar_graph(data)

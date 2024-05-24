import pandas as pd

# Load the data from the CSV file
file_path = "country_vaccination_stats.csv"
df = pd.read_csv(file_path)

# Function to fill missing data
def fill_missing_vaccinations(df):
    # Create a copy of the dataframe to avoid modifying the original data
    df_filled = df.copy()
    
    # Group by country and apply the minimum function to the daily_vaccinations column, ignoring NaN values
    min_vaccinations_per_country = df_filled.groupby('country')['daily_vaccinations'].transform('min')
    
    # Fill NaN values with the minimum vaccination number per country
    df_filled['daily_vaccinations'] = df_filled['daily_vaccinations'].fillna(min_vaccinations_per_country)
    
    # For countries with no valid vaccination number, fill with 0
    df_filled['daily_vaccinations'] = df_filled['daily_vaccinations'].fillna(0)
    
    return df_filled

# Apply the function to the dataframe
df_filled = fill_missing_vaccinations(df)

# Function to list the top-3 countries with the highest median daily vaccination numbers
def top_3_countries_by_median_vaccination(df_filled):
    # Calculate the median daily vaccinations for each country
    median_vaccinations = df_filled.groupby('country')['daily_vaccinations'].median()
    
    # Sort the countries by median daily vaccinations in descending order
    top_3_countries = median_vaccinations.sort_values(ascending=False).head(3)
    
    return top_3_countries

# Apply the function to the filled dataframe
top_3_countries = top_3_countries_by_median_vaccination(df_filled)

print("Top 3 countries with the highest median daily vaccination numbers:")
print(top_3_countries)

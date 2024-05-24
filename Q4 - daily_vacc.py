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

# Save the updated dataframe to a new CSV file
output_path = "filled_country_vaccination_stats.csv"
df_filled.to_csv(output_path, index=False)

print(f"Filled data saved to {output_path}")

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

# Load the CSV file into a DataFrame (adjust the file path as necessary)
file_path = '/Users/ICON/Downloads/addresses.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Ensure the CSV has columns 'Latitude' and 'Longitude' (or adjust column names if necessary)
# Extract the latitude and longitude as a numpy array
coordinates = df[['Latitude', 'Longitude']].values

# List of addresses (optional, if you want to print addresses later)
addresses = df['Address'].tolist()

# Number of zones (clusters) you want to create
n_zones = 7  # Adjust this as needed

# Apply KMeans clustering
kmeans = KMeans(n_clusters=n_zones, random_state=42)
kmeans.fit(coordinates)

# Get the cluster centers (which represent the zone centers)
zone_centers = kmeans.cluster_centers_

# Get the zone assignments for each address (which zone each address belongs to)
zone_assignments = kmeans.labels_

# Create a DataFrame to view the results
zones = pd.DataFrame({
    'Address': addresses,
    'Latitude': df['Latitude'],
    'Longitude': df['Longitude'],
    'Zone': zone_assignments
})

# Display the results
print(zones)

# Optionally: Print the cluster centers (representing the zone centers)
print("\nZone Centers (Latitude, Longitude):")
print(zone_centers)

# Save the results to a CSV file
output_file = '/Users/ICON/Downloads/clustered_addresses.csv'  # Adjust this path as needed
zones.to_csv(output_file, index=False)

print(f"\nClustered data saved to '{output_file}'")

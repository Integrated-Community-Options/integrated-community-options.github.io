import pandas as pd
import numpy as np
from geopy.distance import geodesic

# Load the CSV file into a DataFrame (adjust the file path as necessary)
file_path = '/Users/ICON/Downloads/addresses_zones.csv'  # Replace with your actual file path
df = pd.read_csv(file_path)

# Ensure the CSV has columns 'Latitude' and 'Longitude' (or adjust column names if necessary)

# Predefined zone centers (Latitude, Longitude, Zone name)
zones = [
    {'lat': 34.08875342, 'lon': -117.75989543, 'zone': 'Zone 0'},
    {'lat': 34.13325125, 'lon': -118.0498095, 'zone': 'Zone 1'},
    {'lat': 34.2145622, 'lon': -118.2722638, 'zone': 'Zone 2'},
    {'lat': 34.08010269, 'lon': -117.93141915, 'zone': 'Zone 3'},
    {'lat': 34.10135763, 'lon': -118.27443229, 'zone': 'Zone 4'},
    {'lat': 34.17574353, 'lon': -118.14936753, 'zone': 'Zone 5'},
    {'lat': 33.987361, 'lon': -117.8536475, 'zone': 'Zone 6'}
]

# Function to calculate the nearest zone for a given address
def assign_zone(address_lat, address_lon, zone_centers):
    closest_zone = None
    min_distance = float('inf')  # Start with a very large number to find the minimum

    for zone in zone_centers:
        zone_coords = (zone['lat'], zone['lon'])
        address_coords = (address_lat, address_lon)
        
        # Calculate the distance using geodesic (Haversine formula)
        distance = geodesic(address_coords, zone_coords).meters
        
        # If this zone is closer, update the closest zone
        if distance < min_distance:
            min_distance = distance
            closest_zone = zone['zone']
    
    return closest_zone

# Apply the zone assignment for each address
df['Assigned Zone'] = df.apply(
    lambda row: assign_zone(row['Latitude'], row['Longitude'], zones),
    axis=1
)

# Display the updated DataFrame with assigned zones
print(df[['Address', 'Latitude', 'Longitude', 'Assigned Zone']])

# Save the results to a CSV file
output_file = '/Users/ICON/Downloads/assigned_zones.csv'  # Adjust this path as needed
df.to_csv(output_file, index=False)

print(f"\nAssigned zones saved to '{output_file}'")

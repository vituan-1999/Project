# Analyze California city distribution
from typing import Tuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import data 
cities = pd.read_csv("california_cities.csv")
latd, longd = cities["latd"], cities["longd"]
pop, size = cities["population_total"], cities["area_total_km2"]

# plot graph
plt.style.use("seaborn-notebook")
plt.figure(figsize=(7,7))
img = plt.scatter(latd, 
                  longd, 
                  c=np.log10(pop),  # pop is so large => use log10 to get smaller value 
                  s=size)
plt.axis("equal")
plt.title("California cities: Population and Area distribution")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.colorbar(label="log$_{10}$ (Population)")
plt.clim(2,6)   # limit the color bar value

# graph legend
area_range = [50, 100, 300, 500]
for area in area_range:
    plt.scatter([], [], s=area, c='k', label=str(area) + "km$^2$")
plt.legend(labelspacing=1, title="City area")
plt.show()

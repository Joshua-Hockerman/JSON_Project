import json

infile = open("eq_data_1_day_m1.json", "r")
outfile = open("readable_eq_data.json", "w")

eq_data = json.load(
    infile
)  # converting the contents of that json into a dictionary for manipulation in Python

json.dump(eq_data, outfile, indent=4)

magnitude = []
latitude = []
longitude = []

for n in range(len(eq_data["features"])):
    magnitude.append(eq_data["features"][n]["properties"]["mag"])
    latitude.append(eq_data["features"][n]["geometry"]["coordinates"][0])
    longitude.append(eq_data["features"][n]["geometry"]["coordinates"][1])

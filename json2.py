from plotly import offline
from plotly.graph_objs import Scattergeo, Layout
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
hover_text = []

for n in range(len(eq_data["features"])):
    magnitude.append(eq_data["features"][n]["properties"]["mag"])
    longitude.append(eq_data["features"][n]["geometry"]["coordinates"][0])
    latitude.append(eq_data["features"][n]["geometry"]["coordinates"][1])
    hover_text.append(eq_data["features"][n]["properties"]["title"])

print(magnitude[:5])
print(latitude[:5])
print(longitude[:5])
print(hover_text[:5])

data = [
    {
        "type": "scattergeo",
        "lon": longitude,
        "lat": latitude,
        "text": hover_text,
        "marker": {
            "size": [5 * i for i in magnitude],
            "color": magnitude,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]

my_layout = Layout(title="Global Earthquake 1 Day")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="globalearthquake1day.html")

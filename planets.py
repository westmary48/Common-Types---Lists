planet_list = ["Mercury", "Mars"]

print(planet_list)

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.append("Pluto")


planet_list.insert(1, "Venus")

planet_list.insert(2, "Venus")

print(planet_list)

rocky_planets = slice(0, 4, 1)

print(planet_list[rocky_planets])

del planet_list[8]


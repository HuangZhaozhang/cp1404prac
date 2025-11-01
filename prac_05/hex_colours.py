"""
CP1404/CF5632 Practical
Hex colour codes lookup program
"""

# Define a constant dictionary of colour names and their hex codes
HEX_COLOURS = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUA": "#00ffff",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BISQUE": "#ffe4c4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#ffebcd",
    "BLUE": "#0000ff"
}
# Iterate through the dictionary and print all colour names and codes
for code, name in HEX_COLOURS.items():
    print(f"{code} corresponds to {name}")

# Allow users to input colour names for querying
colour_name = input("Enter colour name: ").upper()
while colour_name != "":
    try:
        print(f"{colour_name} : {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").upper()
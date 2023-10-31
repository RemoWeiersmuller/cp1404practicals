COLOR_TO_HEXADECIMAL = {'AliceBlue': '#0048ba', 'AntiqueWhite': '#faebd7', 'Barn Red': '#7c0a02', 'Bisque1': '#ffe4c4',
                        'Blue Green': '#0d98ba', 'Buff': '#f0dc82', 'Burgundy': '#800020', 'CadetBlue': '#5f9ea0',
                        'Camel': '#c19a6b', 'Carmine': '#960018'}

color_dict = {key.lower(): value for key, value in COLOR_TO_HEXADECIMAL.items()}
color = input('Enter your color to get hexadecimal: ')

while color != '':
    color_lower = color.lower()
    print(color, "is", color_dict.get(color_lower, "not found"))
    color = input('Enter your color to get hexadecimal: ')
print('farewell')




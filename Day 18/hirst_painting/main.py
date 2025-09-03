import colorgram


colors = colorgram.extract('image.jpg', 30)
"""
print(colors[0])
print(colors[0].rgb)
print(colors[0].hsl)
print(colors[0].proportion)
"""
"""
rgb_colors = []
for rgb_color in colors:
    red = rgb_color.rgb.r
    green = rgb_color.rgb.g
    blue = rgb_color.rgb.b
    new_color = (red, green, blue)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
color_list = [(252, 251, 248), (159, 180, 190), (219, 173, 125), (132, 74, 55), (52, 102, 151), (246, 233, 237), (118, 82, 93), (179, 140, 151), (161, 104, 151), (246, 251, 247), (44, 48, 67), (127, 173, 115), (84, 96, 182), (66, 11, 29), (239, 242, 247), (82, 133, 108), (230, 189, 139), (53, 62, 77), (193, 91, 74), (113, 45, 58), (94, 142, 119), (70, 66, 54), (183, 187, 205), (67, 61, 50), (207, 182, 191), (216, 181, 173), (178, 201, 177), (77, 59, 53), (174, 199, 203), (56, 66, 69)]

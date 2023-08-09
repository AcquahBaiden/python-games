import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 30)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s


rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)
colors_list = [(199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (240, 246, 251), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153)]
################################################
#                Configuration
################################################
# Template CSV file, which to use
# Columns need to be as follows:
# any, x, y, index
template_file = ".\OwOBoard.csv"

# Layout
# Every line in the layout object corresponds to a matrix
# the numbers represent the x and y offsets from the origin
# unit should be the same as the csv input file eg. millimeters
layout = [
    (00, 30), #mouth upper
    (30, 30),
    (60, 30),
    (15, 55), #nose
    (30, 0),  #mouth lower
    (60, 0),
    (90, 0),
]

# Final Object Name
final_name = "OwOBoardPixelMatrixCombined"

################################################

output_file_name = "" + final_name + ".h"
with open(template_file, 'r') as file:
    data = file.read()
    f = open(output_file_name, "w")
    f.write("#pragma once\n\n")

    x = []
    y = []
    #generate the pixel position lines
    for matrix in layout:
        lines = data.splitlines()
        for line in lines:
            split = line.split(",")
            x.append(float(split[1]) + matrix[0])
            y.append(float(split[2]) + matrix[1])

    #write file header
    f.write("Vector2D " + final_name + "[" + str(len(x)) + "] = {\n")
    #write pixel position lines
    for i, line in enumerate(x):
        if i < len(x) - 1:
            f.write("\t Vector2D(" + f'{x[i]:.2f}' + "f," + f'{y[i]:.2f}' + "f),\n")
        else:
            f.write("\t Vector2D(" + f'{x[i]:.2f}' + "f," + f'{y[i]:.2f}' + "f)\n};\n")    
    f.close()
import bpy


for line_number, line in enumerate(open(r'D:/PROJECT PHASE 2/CSV Data/test.csv')):
    columns = line.rstrip().split('\t')      
    print(columns)
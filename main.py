"""
Reading File
"""
file = open('input_data.txt','r')

line = file.read()

file.close()

print(line)


"""
Writing File
"""
data_out = input('Please enter some text to store > ')

file = open('output_data.txt','w')

file.write(data_out)

file.close()


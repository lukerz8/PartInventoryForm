import sys
#TODO: handle [,], ['], ["] and strange characters in input file

# Print Instructions
readme = open('readme.txt', 'r')
for line in readme:
	print(line.strip('\n'))
readme.close();

# Get input filename
while(1):
	finName = input('Enter input filename (ex. in.csv): ')

	# Try to open this file
	try:
		print('Opening file...')
		fin = open('input/' + finName, 'r')
		print('Done.\n')
		break
	# If fail, retry get file name
	except:
		print('File not found!')

# If success, check column names
print("Checking header names...")
headerNames = ['partid', 'quantity', 'category', 'partname']
header = fin.readline().strip('\n').split(',')

for i in range(4):
	print(header[i].lower() + " = " + headerNames[i])
	if header[i].lower() == headerNames[i]:
		print("true\n")
	# If bad headers, print error and exit
	else:
		print("false!\n\n please fix this. Exiting.\n\n")
		fin.close()
		sys.exit(-1)

# If good headers, get output filename
# TODO: create error checking here
fout = open('kits/' + input('Enter kit name without spaces (ex. ev3)') + '.json', 'w')

# Run conversion, printing output
# Print top of out file
fout.write('{"parts": [\n')

# Print first line (without leading ',\n') #TODO: find a better way to do this
temp = fin.readline().strip('\n').split(',')
fout.write('{{"partNum":"{}", "count":"{}", "cat":"{}", "desc":"{}"}}'
			.format(temp[0], temp[1], temp[2], temp[3]))
print(line) #debug

for line in fin:
	line = line.strip('\n').split(',')
	#print(line) #debug
	fout.write(',\n{{"partNum":"{}", "count":"{}", "cat":"{}", "desc":"{}"}}'
				.format(line[0], line[1], line[2], line[3]))

fin.close()
fout.write("\n]}")
fout.close()

# Print done, more instructions, exit
print('\n\nDone!')

#TODO: print other instructions here?

sys.exit(0)

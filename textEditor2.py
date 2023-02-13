import argparse, os

textFile = "null"

def loader(fileName):
	if os.path.exists(fileName):
		textFile = open(fileName, "r")
		os.system("clear")
		#print(textFile.read())
		data = textFile.read().split("\n")
		data = data[:-1]
		lineNum = 1
		for lines in data:
			print(f"{lineNum}.  {data[lineNum - 1]}")
			lineNum += 1
		textFile.close()
		textFile = open(fileName, "a")
	else:
		#textFile = open(fileName, "w")
		#textFile.close()
		print("Unrecognized file.")
		print("Perhaps you didn't include the extension?")
		print("\nDefaulting to a temporary file.")
		textFile = open("temp.txt", "w")
		fileName = "temp.txt"
	
	#textFile = open(fileName, "r")
	#os.system("clear")
	#print(textFile.read())
	#textFile.close()

def argsParser():
	parser = argparse.ArgumentParser()

	parser.add_argument("-f", "--fileName", help = "takes a file name, including the extension, and automatically loads it into the editor")

	global fileName
	global args
	args = parser.parse_args()

	if args.fileName:
		print(f"Showing file name: {args.fileName}")
		fileName = args.fileName
		print(fileName)
		loader(args.fileName)
	else:
		fileName = "temp.txt"
		global textFile
		textFile = open("temp.txt", "w")

def lineSaver(textFile, text):
	with open(fileName, "a") as textFile:
		textFile.write(text + '\n')

def fileSaver(textFile):
	#if os.path.exists(textFile):
	with open(fileName, "a") as textFile:
		textFile.close()
		loader(fileName)
	#else:
	#	print("Error.")

def fileSaveAs(fileName, destination):
	#Opening the current file in read mode
	#then copying all the lines into a data list.
	textFile = open(fileName, "r") 
	data = textFile.readlines()
	textFile.close()
	#Opening the destination file in write mode.
	#Then using a for loop to copy over all indexes in data
	#to the destination file.
	textFile = open(destination, "w")
	#print(data[1])
	for lines in data:
	#	print(lines)
		textFile.write(lines)
	textFile.close()
	#Opening initial file in append mode.
	#Printing that it all worked. *Hopefully.
	textFile = open(fileName, "a")
	print("File saved properly.")

argsParser()

#TODO: Delete temp.txt when closing editor with :q
#TODO: Add more ':' options.
#TODO: Add ability to go up and down lines
#		Likely by using :u and :d or :z and :x
#		Would also need to add in line numbers and also a command that would edit allow editing of specific lines.

#tempFile = open("temp.txt", "w")
while (True):
	print(fileName)
	text = input()
	if (text == ":q"):
		#Make prompt here for user to save unsaved work.
		with open(fileName, "a") as textFile:
			textFile.close()
		#if (textFile == "temp.txt"):
		#	if os.path(file):
		#		os.remove(file)
		exit()
	elif (text == ":o"):
		#Opening a file
		#Make another prompt for user to save unsaved work.
		fileName = input("Enter file name with the file's extension: ")
		loader(fileName)
	elif (text == ":s"):
		#Saves current file by closing it, then reopening it.
		fileSaver(textFile)
	elif (text == ":sa"):
		#Saves current file to another by using readlines and copying the data
		#to a specified file.
		destination = input("Enter the file you want to save the current file to.")
		with open(fileName, "a") as textFile:
			textFile.close()
			fileSaveAs(fileName, destination)
	elif (text == ":"):
		pass
	elif (text == ":h"):
		print("Help section:")
		print("\tExample: \n\t\tcommand name  ;  short description  ;  available parameters  ;  long description\n")
		print("\t:h  ;  help  ;  Opens this help dialogue.")
		print("\t:o  ;  open  ;  fileName  ;  Opens a file located at the specified file name.")
		print("\t:s  ;  save  ;  Saves the current open file.")
		print("\t:sa  ;  save as  ;  destination  ;  Saves the current open file to the file specified in destination. Will overwrite existing data within the destination file.")
	else:
		lineSaver(textFile, text)
		fileSaver(textFile)

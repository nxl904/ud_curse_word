from urllib.request import urlopen

def read_text():
	input_file = open(r"C:\Udacity\curse_word\check.txt")
	contents_of_file = input_file.read()
	print(contents_of_file)
	input_file.close()
	check_profanity(contents_of_file)



def check_profanity (text_to_check): 
	connection = urlopen("http://www.wdylike.appspot.com/?q= ".format(id))
	output = str(connection.read())
	print (output)
	connection.close()
	if "true" in output: 
		print("No curse words in your document")
	elif "false" in output:
		print("There is a curse word in your document!")
	else:
		print("Document didn't scan properly")


read_text()
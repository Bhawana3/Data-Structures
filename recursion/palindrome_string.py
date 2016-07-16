# find if the string is palindrome recursively

def ispalindrome(string):
	if len(string) == 0 or len(string) == 1:
		return True
	elif string[0] == string[len(string)-1]:
		return ispalindrome(string[1:len(string)-1])
	return False

if __name__ == "__main__":
	print "Menu : "
	print "1 - Find if the string is palindrome or not"
	n = raw_input('Enter 1 : ')
	while True:
		if n == '1':
			string = raw_input("Enter any string to know if it's palindrome or not : ")
			print ispalindrome(string)
		else:
			print "Invalid option choosen."
			break
		n = raw_input('Enter 1 : ')
		 

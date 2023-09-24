def somefunc():
	print("smth")

if __name__ == "__main__":
	while (True):
		try:
			a, b, c = map(float, input("enter coeefs: ").split())
		except:
			print("incorrect input, enter coeefs as a b c: ")
			continue
		else:
			break
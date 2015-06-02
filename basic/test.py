def main():
	d = {'a':3, 'b':1, 'c':4, 'd':0}
	print d
	s = sorted(d, key=d.get, reverse = True)
	print s
	print d.get	
if __name__ == '__main__':
  main()

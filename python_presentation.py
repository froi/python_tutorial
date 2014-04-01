import python_ascii
import playing_w_date_time

def what_is_python():
	print "What is Python?"
	raw_input()

	print "\tSnake?"
	raw_input()

	print "\tMonty Python?"
	raw_input()

	print "\tPython is an interpreted, object-oriented, high-level programming language with dynamic semantics."
	raw_input()

	print "\tInterpreted?"
	raw_input()

	print "\t\tYou write a statement it executes it."
	raw_input()

	print 'you@comp$ python'
	print '>>> '
	raw_input()

def python_syntax():
	print "Python syntax"
	raw_input()

	print "\tHello World...Nah!" 
	raw_input()

	python_ascii.hello_python()
	raw_input()

	print '\tI imported a simple script that just prints Hello Python in some novice ascii art. Let\'s see that code!'
	raw_input()

	with open('python_ascii.py', 'r') as f:
		print f.read()
	raw_input()

	print 'Variables'
	print '''
		our_var = "Hello Pythonistas!"
		our_var= 9
	'''
	raw_input()
	
	print 'Statements and Whitespace'
	raw_input()
	
	print '\tThis is a statement: a = 23'
	print '\tThis is also a statement if a:'
	raw_input()
	
	print '\tWhitespace matters!!!'
	raw_input()
	
	print '''
		if a:'
		x="BAM!"

		You'll get an error:
			IndentationError: expected an indented block
	'''
	raw_input()
	
	print '''
		if a:'
			x="BAM!"

		This is correct!!
	'''
	raw_input()

	print '''
		def my_method():
		a = 4
		b = 5

		BOOM! Same problem as above...
	'''
	raw_input()
	
	print '''
		def my_method():
			a = 4
			b = 5

		Now that's better!
	'''
	raw_input()

	print '\tif a:'
	raw_input()
	
	print 'Comments'
	raw_input()
	
	print '\tSingle line: # This is a comment.'
	raw_input()
	
	print '''Multiline: 
	\'\'\' 
		This is also a comment, but only if it's not the first line in a method, class, or module.
	\'\'\' 
	'''
	raw_input()

def python_data_types():
	print 'Data types:'
	raw_input()

	print '''
		String: '', 'Python', "UPR"
		Integer: 0, -9, 123456
		floats: 9.4, 0.40
		booleans: True or False
	'''
	raw_input()

def python_math():
	print 'Math'
	raw_input()
	print '\tAddition: 2+2 = %s' % str(2+2)
	raw_input()
	print '\tSubtraction: 1-2 = %s' % str(1-2)
	raw_input()
	print '\tMultiplication 2*2 = %s' % str(2*2)
	raw_input()
	print '\tDivision 2/2 = %s' % str(2/2)
	raw_input()
	print '\tExponents 2 ** 2 = %s' % str(2**2)
	raw_input()
	print '\tModulo 10 % 2 = ', str(10%2)
	raw_input()

def python_strings():
	print 'Strings and Console Output'
	raw_input()

	print '\tsimple_string = "Hello I am a simple string!"'
	raw_input()
	
	print '''
		Escaping
			simple_string2 = 'Hello I\'m alse a simple string!'
	'''
	raw_input()
	
	print '\tstrings by offset'
	print '\t\t"Python"[3] -> ', 'Python'[3]
	raw_input()

	print '\t\tWhat would be the output for this "Monty Python"[6]'
	raw_input()
	
	print 'Monty Python'[6]
	raw_input()

	print 'Some basic global methods'
	raw_input()

	print 'len()'
	print '\tlen("supercalifragilisticexpialidocioua") -> ', len('supercalifragilisticexpialidocioua')
	print 'len can also take as arguments other data types and structures', 
	raw_input()

	print 'upper() - dot notation is used with this methods because it only applies to strings!'
	print '\t"best method evar!!!!".upper() -> ', "best method evar!!!!".upper()
	raw_input()
	print 'lower() - dot notation is used with this methods because it only applies to strings!'
	print '\t"NO, THIS IS THE BEST METHOD EVARRRR!!!!".lower() -> ', "NO, THIS IS THE BEST METHOD EVARRRR!!!!".lower()
	raw_input()
	print 'str()'
	print '\tConvert something into a string'
	print '\tprint 2 + 2 -> ', 2 + 2
	raw_input()
	try:
		print '\tprint str(2) + 2 -> ', str(2) + 2
	except: 
		print 'TypeError: cannot concatenate \'str\' and \'int\' objects'
	print '\tprint str(2) + str(2) -> ', str(2) + str(2)
	raw_input()
	print 'print'
	raw_input()
	print '\tprint "prPIG is awesome!"'
	print '\tthe_awesomeness = "prPIG is awesome!"'
	print '\tprint the_awesomeness'
	raw_input()
	print 'String concatenation'
	raw_input()
	print '\tprint "And now with magic " + "we concatenate" + "the different strings!"'
	print 'What went wrong?'
	raw_input()
	print '\tString formatting with %'
	print '\t\tkiller_rabbit_caerbannog = "rabbit"'
	print '\t\tsilly = "silly sod!"'
	print '\t\tcrap_pants = "crapped my pats"'
	print '\t\tprint "Where behind the %s?" % killer_rabbit_caerbannog'
	print '\t\tprint "Nay! Ti\'s the %s" % killer_rabbit_caerbannog'
	print' \t\tprint "You %s I nearly %s I was so scared!" % silly, crap_pants'
	raw_input()

def python_imports():
	print 'imports'
	raw_input()
	print '\timport foo'
	print '\timport foo.bar'
	raw_input()
	print '\tfrom foo import bar -> imports the object bar from the foo module'
	raw_input()
	print '\tfrom foo import bar, baz -> imports objects bar and bas from the foo module'
	raw_input()
	print '\tfrom foo import * -> imports all objects in foo lib'
	raw_input()
	print '\tfrom foo import bar as fizz -> import bar from foo with the fizz alias'
	raw_input()
	print '\tfrom .foo import bar -> import object bar from foo module in a modified search path'
	raw_input()
	print '\tfoo = __import__("foo") -> import foo module dynamically. Must be assigned to a var in order to use it\'s properties and methods'
	raw_input()
	print '\treload(foo) -> reloads the foo module. Useful if you\'re editing the module.'
	raw_input()

def python_date_time():
	print 'Date and Time'
	raw_input()
	print playing_w_date_time.print_date_parts()
	raw_input()
	print playing_w_date_time.print_date()
	raw_input()
	print playing_w_date_time.print_date_time()
	raw_input()

def python_conditionals():
	print 'Conditionals'
	raw_input()
	print '\tcomparators'
	print '\t\tequals: =='
	print '\t\tnot equals: !='
	print '\t\tgreater than: >'
	print '\t\tlesser than: <'
	print '\t\tgreater or equal: >='
	print '\t\tlesser or equal: <='
	raw_input()
	print '\t\tE.g.'
	print '\t\t\ta = 0'
	print '\t\t\tb = 1'
	print '\t\t\ta == 0 -> True'
	print '\t\t\tb == 2 -> False'
	print '\t\t\tif b > 0 :'
	print '\t\t\t\tprint a/b'
	print '\t\t\ta = 100'
	print '\t\t\tprint_val_a = True'
	print '\t\t\tif print_val_a :'
	print '\t\t\t\tprint a'
	print '\t\t\telse:'
	print '\t\t\t\tprint "JA JA. No te digo na!"'
	raw_input()

def python_control_flow():
	print '\tif else elif'
	raw_input()
	
	print '\t\tif True :'
	print '\t\t\tsomething'
	print '\t\telse:'
	print '\t\t\tsomething'
	raw_input()
	
	print '\t\tnum = 0'
	print '\t\t\tif num == 5:'
	print '\t\t\tsomething'
	print '\t\telif num > 2:'
	print '\t\t\tsomething else'
	print '\t\telse :'
	print '\t\t\toh well'
	raw_input()

	print '\ttruth table:'
	raw_input()

	print '\t\tTrue and True is True'
	print '\t\tTrue and False is False'
	print '\t\tFalse and True is False'
	print '\t\tFalse and False is False'
	raw_input()

	print '\t\tTrue or True is True'
	print '\t\tTrue or False is True'
	print '\t\tFalse or True is True'
	print '\t\tFalse or False is False'
	raw_input()

	print '\t\tNot True is False'
	print '\t\tNot False is True'
	raw_input()

	print '\tAnd'
	print '\t\tnumber1 = 5'
	print '\t\tnumber2 = 20'
	print '\t\tnumberChoice = 7'
	print '\t\tif numberChoice >= number1 and numberChoice <= number2 :'
	print '\t\t\tprint "Good choice."'
	print '\t\telse:'
	print '\t\t\tprint "Boo. Wrong choice!"'
	raw_input()

	print '\tOr'
	print '\t\tcolor1 = "red"'
	print '\t\tcolor2 = "blue"'
	print '\t\tcolorChoice = "red"'
	print '\t\tif colorChoice >= color1 or colorChoice <= color2 :'
	print '\t\t\tprint "Good choice."'
	print '\t\telse:'
	print '\t\t\tprint "Boo. Wrong choice!"'
	raw_input()

	print '\tNot'
	print '\t\tnum = 9'
	print '\t\tif not num > 10:'
	print '\t\t\tprint "I see what you did there."'
	raw_input()

def python_functions():
	print 'Functions'
	raw_input()

	print '\twhat is a function?'
	print '\t\ta piece of code that is given an identifier (name) to be called later on'
	raw_input()

	print '\tdef hello():'
	print '\t\tprint "Hey Hey Hey!"'
	print '\thello()'
	raw_input()

	print '\tdef hello2(name):'
	print '\t\tprint "Why hello there %s" % name'
	print '\thello2()'
	raw_input()

	print '\tdef add(num1, num2, num 3):'
	print '\t\treturn num1 + num2 + num3'
	print '\tadd(1,2,3)'
	raw_input()

def python_data_structs():
	print 'Data Structures: Tuple, List, and Dictionary'
	raw_input()

	print '''
		Tuples
			This is a Tuple: ('Python', 'Ruby', 'Jave', 'C/C++', 'C#')
			Tuples look a lot like list but they are immutable. Also notice that a tuple is surronded by parentheses.
	'''
	raw_input()

	print ''''
		Lists:
			list1 = []
			list2 = [3,5,6,7,8,1,2,3]
			list3 = ["Python", "Rattlesnake", "Boa", "Rabbit", "Black Mamba"]
	'''
	list1 = []
	list2 = [3,5,6,7,8,1,2,3]
	list3 = ["Python", "Rattlesnake", "Boa", "Rabbit", "Black Mamba"]
	raw_input()

	print '\t\tNavigating list:'
	raw_input()

	print '\t\tindexes start at 0'
	raw_input()

	print '\t\tprint list2[6] -> ', list2[6]
	raw_input()

	print '\t\tuseful actions with lists:'
	raw_input()

	print '\t\tlen(list2) -> ', str(len(list2))
	raw_input()

	print '''
			slicing:
				list3[start:finish]
	'''
	raw_input()

	print '\t\t\t# from the second index to the fifth'
	print '\t\t\tprint list3[1:4] -> ', list3[1:4]
	raw_input()

	print '\t\t\t# from the second index to the last'
	print '\t\t\tprint list3[1:] -> ', list3[1:]
	raw_input()

	print '\t\t\t# from the first index to the fourth'
	print '\t\t\tprint list3[:3] -> ', list3[:3]
	raw_input()

	print '\t\t\t# exercise: what happens if you put a negative number in the slice?'
	print '\t\t\tprint list3[:-2]'
	print '\t\t\tprint list3[-2:]'
	print '\t\t\tprint list3[-3:-1]'
	raw_input()

	print '\t\t\tlist3[:-2] -> ', list3[:-2]
	print '\t\t\tlist3[-2:] -> ', list3[-2:]
	print '\t\t\tlist3[-3:-1] -> ', list3[-3:-1]
	raw_input()

	print '\t\tsearching in a list:'
	print '\t\t\tlist3.index("Boa")'
	raw_input()

	print '\t\tinserting into a list:'
	print '\t\t\tlist3.insert(2, "culebra")'
	raw_input()

	print '\t\tappending into a list:'
	print '\t\t\tlist3.append("vieques")'
	raw_input()

	print '\t\tgoing through a list:'
	print '\t\t\tfor idx in list3:'
	print '\t\t\t\tprint list[idx]'
	raw_input()

	print '\t\tsorting a list'
	print '\t\t\t list3.sort()'
	raw_input()

	print '\t\tremoving from a list:'
	print '\t\t\tlist3.pop() -> removes the last item in a list'
	print '\t\t\tlist3.remove("Boa") -> searches the list for the string and eliminates it.'
	raw_input()

	print '''
		Dictionaries
			dict1 = {}
			dict2 = {'Python': 'Awesomeness', 'Java': 'At least no pointers', 'C++': 'I hate pointers.'}'
			dict3 = {'First': 123, 'Second': 456, 'Third': 789}'
	'''
	dict1 = {}
	dict2 = {'Python': 'Awesomeness', 'Java': 'At least no pointers', 'C++': 'I hate pointers'}
	dict3 = {'First': 123, 'Second': 456, 'Third': 789}
	raw_input()

	print '\t\tLooping though dictionaries'
	print '''
			This will return a tuple of (key, value)
			for k, v in dict2.iteritems():
				print 'key: %s, value: %s' % (k, v)
	'''
	raw_input()

	for k, v in dict2.iteritems():
		print '\t\tkey: %s, value: %s' % (k, v)
	raw_input()

	print '''
			Adding a new item to a dict.
				dict2['Cobol'] = 'Not funny'
				or
				dict2.update({'Ruby': 'Not as good but meh'})
	'''
	dict2['Cobol'] = 'Not funny'
	dict2.update({'Ruby': 'Not as good but meh'})
	raw_input()

	print '\t\tLets iterate over the list after the inserts.'
	raw_input()

	for k, v in dict2.iteritems():
		print '\t\tkey: %s, value: %s' % (k, v)
	raw_input()

	print '''
			Getting a value for a specific key.
			dict3.get('key')
	'''
	raw_input()

	print '\t\tSo dict3.get(\'Second\') -> ', dict3.get('Second')
	raw_input()

	print '''
			Removing an item pair form a dictionary
			dict3.pop('key'): will remove the key and return the value.
	'''
	raw_input()

	print '\t\tSo: dict3.pop(\'Third\') -> ', dict3.pop('Third')
	raw_input()

	print '''
			Other dictionary methods:

			dict3.iterkeys(): return a dictionary iterator with all keys in dict3
			dict3.itervalues(): return a dictionary iterator with all values in dict3
			dict3.keys(): return a list of all keys in dict3
			dict3.values(): return a list of all values in dict3
	'''
	raw_input()

def python_loops():
	print 'Loops'
	print '''
		For loops:
		for x in range(1,10):
			pass
	'''
	raw_input()

	print '''
		while loops
		while <condition>:
			pass
	'''
	raw_input()

def python_input_output():
	print 'File input and Output'
	raw_input()

	print '''
		Opening a file:
			tmp_file = open('/home/user/file.txt')
		This will give you a file object.
	'''
	raw_input()

	print '''
		Opening a file and printing out all it's content:
			
			with open('/home/user/file.txt', 'r') as f:
				print f.read()

		The with statement will handle all garbage collection for you and close the file when finished.
	'''
	raw_input()

	print '''
		Writing to a file is just as easy:
			f = open('somefile.txt', 'w')
			f.write('What up!!!!')
			f.flush() -> used if you want to write to the file while keeping the file open.
			or
			f.close() -> implicitly calls flush and closes file object
	'''
	raw_input()

	print '\tFor a more complete explanation go to: https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files'
	raw_input()

def python_important_links():
	print '''
	A few important links
		http://www.python.org
		http://www.codecademy.com
		http://learnpython.org
		http://www.twitter.com/pr_pig
	'''
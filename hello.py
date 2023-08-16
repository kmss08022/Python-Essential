
#2. 
 #Control flow
    

    #for loop : lists are iterable
    #while loop: doesn't iterate over items, but keeps looping until condition is false
    a = 0
while a < 5:
     print(a)
     a= a+1




class Dog:
    def __init__(self): #initizailtion function, self is specific instance of dog class
       self.name = 'Rover'
       self.legs = 4

    def speak(self):
        print(self.name + 'says: BaRK')

    myDog = Dog('Rover')
    dog2= Dog('fluffy')
 

class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 4
    
    def speak(self):
        print(self.name + 'Bark')
    
    myDog.speak()

class Dog:
    def __init__(self, name):
        self.name = name
        self.age = 4

myDog = Dog('kazi')
     

#functions

def multiplyByThree(val):
    return 3 * val
    
multiplyByThree(4)


a = [1,2,3,4]

def appenFour(myList):
    myList.append(4)

appendFour(a)

#Classes and Objects
    Class Dog:
        def __init__(self, name):
            self.name = name
            self.legs = 4
            
        def speak(self):
        print(self.name + ' says: Bark!')
    
        
my_Dog = Dog('Kazi')
my_Dog.speak()



#Solution: factorial
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    i = 0
    f = 1
    while i < num:
        i = i+1
        f=f*i

return f

def factorial(num):
    if type(num) is not int:
        return None


    i = 0
    f = 1


    
   



#3 
myList = [1,2]

f'My number is: {5}'


#3 Challenge: Sense of direction



def __init__(self, canvas):
    self.direction = [0,1]
    


def setDegrees(self, degrees):
    radians = (degrees/180) * math.pi
    self.direction = [math.sin(radians), -math.cos(radians)]
    
    def up(self)
        self.direction = [0,-1]
        self.forward()
     
     
scribe = TerminalScribe(canvas)

        
        # Other types of numbers
        
        
    def drawSquare(self, size):
        i=0
        while i < size:
            self.right()
            i = i+1
            
            
#Create function that multiplies number by 3
    def multiple3(val)
    return self * 3
    



#Chapter 4: Basic data structures
#Challenge: Write a function "encodeString" that will encode a string like 'AAAAABBBBAAA' 
    #as a list ot tuples: [{()'A', 5), ('B', 4)}]
def encodeString(stringVal):
  encodedList = []
  prevChar = stringVal[0]
  count = 0

  for char in stringVal:
       if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
       count = count + 1

    encodedList.append((prevChar, count))
  return encodedList

       

def decodeString(encodedList):
  pass


def encodeString(stringVal):
  
  pass

def decodeString(encodedList):
  pass


  ##solution:
#we want to loop through the stringVal that is being passes into stringVal
#along the way we want to keep track of three things
#encoded list that ultimately gets returned from the function
#keep track of previous character, and when character has changed, 
#       and added to inside the loop
# if the current character doesnt match the prev char, we know we need to stop, 
    #and add something to the encoded list
#lastly, we have the count. This starts at 0 and keeps track of how many characters 
    #we've gone through without seeing any change
#as we loop through, if the prev char is not equal to current char, we've seen a change

  def encodeString(stringVal): 
       encodedList = [] 
       prevChar = stringVal[0] 
       count = 0
#we want to loop through the stringVal that is being passes into stringVal
for char in stringVal:
  if prevChar != char:
    encodedList.append((prevChar, count))
    count = 0
prevChar = char
count = count + 1


encodedList.append((prevChar, count))
return encodedList
  
def decodeString(encodedList):
  decodedStr=''
  for item in encodedList:
       decodedStr = decodedStr + item[0] * item[1]
    return decodedStr


#we want to loop through the stringVal that is being passes into encodeString
#along the way we want to keep track of three things
 def encodeString(stringVal): 
       encodedList = [] #ultimately gets returned from the function, and gets added to in loop
       prevChar = stringVal[0] #keep track of previous character, and when character has changed, 
#       and added to inside the loop
       count = 0 #lastly, we have the count. This starts at 0 and keeps track of how many characters 
    #we've gone through without seeing any change

#we want to loop through the stringVal that is being passes into stringVal
#as we loop through, if the prev char is not equal to current char, we've seen a change
for char in stringVal:
  if prevChar != char:
    encodedList.append((prevChar, count)) #add to list and set count back to 0
    count = 0 #set the count back to 0, then keep looping through
prevChar = char
count = count + 1


encodedList.append((prevChar, count))
return encodedList
  
def decodeString(encodedList):
  decodedStr=''
  for item in encodedList:
       decodedStr = decodedStr + item[0] * item[1]
    return decodedStr
    

    
#Chapter 5: Control Flow
  
  #if and Else
  for n in range(1,101):
    if n % 15 ==0:
        print('FizzBuzz')
    else  
  
  #while loop
  
  wait_until = datetime.now().second + 2
  
  while datetime.now().second != wait_until:
    print('still waiting')
  print(f'We are at {wait_until} seconds!')
  
    ##continue

  
   #For Loops

for item in myList:
    print(item)
    
    
#Solution Finding Primes Faster

def allPrimesUpTo(num):
    pass

def allprimesUpTo(num):
    primes = [2]
    for number in range(3, num):
        sqrtNum = number**0.5
        for factor in primes:
            if number % factor == 0:
                #not prime
                break
            if factor > sqrtNum:
                #it's prime!
                primes.append(number)
                break
            return primes





###6 Anatomy of Functions

def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation =='multiply':
        return num1 * num2
        
performOperation(2,3,'sum')

def performOperatino(num1, num2, operation='sum')

def performOperation(*args)
    print(args)
    
performOperation(1,2,3)


#######################7 Classes and Objects

class Dog:
    legs = 4
    def __init__(self, name):
    self.name = name
    #self.legs = 4
    
    def speak(self):
        print(self.name + ' says: Bark')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)


#Inheritance

    ## Solution: extending the messenger


 #######################8 Errors and exceptions


 
 #########10 working with files
    # Opening, reading, writing files
        #Opening Files
        f = open('10_01_file.txt', 'r')
        for line in f.readlines():
            print(line)
    
f = open('10_01_file.txt', 'r')
  
f.readline()

    #Writing to files
    f = open('10_01_output.txt', 'w')
    print(f)

        f.write('Lines')
        f.write('Line 2')

        f.close() #required for it to write

    #Appending
    f = open('10_01_output.txt', 'a')
f.write('Line 3\n')
f.write('Line 4\n')
f.close()

    #close function with the with statement
    with open('10_01_output.txt', 'a') as f:
        f.write('some stuff\n')
        f.write('some other stuff\n')


with open('10?02_us.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)







    #challenge: ASCII art Compression
    
    
    
 #########11 Packaging Python
    #command line arguments

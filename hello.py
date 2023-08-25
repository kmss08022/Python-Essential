# %% https://www.youtube.com/watch?v=5lpk1b3SJP0&t=449s

import json

jsonString = '{"a": "apple", "b": "bear", "c": "cat"}'
json.loads(jsonString)
# %%
#4 basic data structures

    #list structures

# myList = [1,2,3,4,5]
# [2*item for item in myList]

# myList = list(range(100))
# filteredList = [item for item in myList if item % 10 == 0]


# animalList = [('a', 'aardvark'), ('b', 'bear')]
# print(animalList)

# animals = {key: value for key, value in animalList}
# print(animals)

#%%
import pandas as pd

#dataDF = pd.read_excel(rf'Z:\files\srcfiles\kafka\data_extract_engine\telco_churn.csv')

df = pd.read_csv(rf'Z:\files\srcfiles\kafka\data_extract_engine\telco_churn.csv')

data[tuple(x) for x in df.values]
# %%

#Get User Input
def performOperation():
    num1 = int(input("num1: "))
    num2 = int(input("num2: "))

    sum = num1 + num2

    print("the sum is:")
    print(sum)
   

        
performOperation()

# %%
#3 challenge converting hex to decimal
hexNumbers = {
    '0': 0, '1': 1,
    'A': 10, 'B': 11
}

def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
        

    if len(hexNum) == 3:
        return hexNumbers[hexNum[0]] * 256 + hexNumbers[hexNum[1]] * 16 + hexNumbers[hexNum[2]]
    


# %% 
# Solution 2 Challenge.

def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    exponent = 0
    decimalValue = 0
    for char in hexNum[::-1]:
        decimalValue = decimalValue + hexNumbers[char] * (16**exponent)
        exponent = exponent + 1

    return decimalValue

hexToDec('3C0')

# %%

#9 multithreading
import threading
import time

def longSquare(num):
    time.sleep(1)
    return num**2

[longSquare(n) for n in range(0,5)]

















def performOperation(num1, num2, operation):
    if operation == 'sum':
        return num1 + num2
    if operation =='multiply':
        return num1 * num2
        
performOperation(2,3,'sum')





# %% #7 static and instance methods
class WordSet:
    def __init__(self):
        self.words = set()

    def addText(self, text):
        text = WordSet.cleanText(text)
        for word in text.split():
            self.words.add(word)

    def cleanText(self, text):
        text = text.replace('!', '').replace('.', '').replace('\'', '')
        return text.lower()

wordSet = WordSet()
wordSet.addText('Hi, I\'m Ryan! Here is a sentence I want to add')
wordSet.addText('Here is another sentence I want to add.')

print(wordSet.words)



# %% Anatomy of a class

#instance attributes
class Dog:
    def __init__(self, name):
        self.name = name
        self.legs = 4

    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.legs)
# %%
#static attributes:unchanging with each instance of the class (make legs an attribute of the class itself)

class Dog:

    _legs = 4
    def __init__(self, name):
        self.name = name
    
    def getLegs():
        return Dog._legs

    def speak(self):
        print(self.name + ' says: Bark!')

myDog = Dog('Rover')
print(myDog.name)
print(myDog.getLegs())

# %% Inheritance

class Dog:
    _legs = 4
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self.name + ' says: Bark!')
    
    def getLegs(Dog):
        def speak(self):

class Chihuahua(Dog):
    def speak(self):
        print(f'{self.name} says: yap yap yap')

    def wagTail(self):
        print('Vigorous wagging')

myDog = Dog('Rover')
myDog.speak()

# %% Extending built-in classes using super()
myList = list()

class UniqueList(list):

    def __init__(self):
        super().__init__()
        self.someProperty = 'Unique List!'


    def append(self, item):
        if item in self:
            return
        super().append(item) #use super()

uniqueList = UniqueList()
uniqueList.append(1)
uniqueList.append(1)

print(uniqueList)

# %%

#7 challenge: extending the messenger
## Extending the Messenger

# Create a class "SaveMessages" that extends the Messenger class that does the following things:

# - Add any messages it receives to a list, along with the time the message was received
# - Use the provided "getCurrentTime" function so that the received message time is a string
# - Contains a method called "printMessages" that prints all collected messages when it's called.

# You might also consider clearing the message list when "printMessages" is called. 


from datetime import datetime

def getCurrentTime():
    return datetime.now().strftime("%m-%d-%Y %H:%M:%S")


class Messenger:
    def __init__(self, listeners=[]):
        self.listeners = listeners
    
    def send(self, message):
        for listener in self.listeners:
            listener.receive(message)

    def receive(self, message):
        # Must be implemented by extending classes
        pass


class SaveMessages(Messenger):
    # Your code here!
    pass


# Run this cell after you've written your solution
listener = SaveMessages()

sender = Messenger([listener])

sender.send('Hello, there! This is the first message')


# Run this cell after you've written your solution
sender.send('Oh hi! This is the second message!')


###Solution###




#1. Python is an interpreted language: An interpreter reads it and executes it immediately.
#   compiled into bytecode (.pyc) -> then this .pyc will be excecutes by Python Virtual Machine 
#
#2. Memory Management:
#   Python uses Automatic Garbage Collection. It means, automatically allocates memory when the object is
#   createdcreated and frees the memory when the objects are not longer needed.  
#
#3. Data Structures:
#    * List       => Ordered collections, stacks           => O(n)  => ex: a = [1, 2, 3]  => arr.append() = arr[1], arr[2] = 99, arr.pop(), arr.remove(20), del arr[0]
#    * Set        => Unique iterms                         => O(1)  => ex: a = {1, 2, 3}  => arr.add(), arr.remove(), arr.discard(), arr.pop()
#    * Dictionary => Key-Value pair                        => O(1)  => ex: a = {"n": 1}   => arr["a"] = 1, arr["a"], arr.get("a"), arr["a"] = 99, arr.pop("a"), del arr["a"]
#    * Deque      => Efficient queues(fast appends/pops)   => O(1)  => ex: a = 
#    * Tuple                                               =>       => ex: a = (1, 2, 3)  => arr[1], update and delete are not allowed.
#    * Stack      =>                                       =>       =>                    => stack.append(), stack[-1], stack.pop()
#    * Queue      =>                                       =>       =>                    => q.append(), q[0], q.popleft()
#    * Heap/Priority Queue  =>                             =>       =>                    => heap[], heapq.heappush(heap, 5), heapq.heappop(heap)
#    * Linked List
#
#
#
#    Data Structure     |     Ordered?           |             Example           |       Mutable?
#----------------------------------------------------------------------------------------------------------
#         List          |        Yes             |          [1, 2, 3]            |         Yes
#         Tuple         |        Yes             |          (1, 2, 3)            |            No
#         String        |        Yes             |          "Nithin"             |            No
#         Range         |        Yes             |          range(5)             |            No
#         Dict          |        Yes             |          {"a": 1, "b": 2}     |         Yes
#         Set           |        No              |         {1, 2, 3}             |         Yes
#         Frozenset     |        No              |         frozenset({1, 2, 3})  |            No
#
#4. Itertools provides fast, memory efficient looping construct without manual nested loops.
#    import itertools
#    from itertools import combinations
#    from itertools import count
#    
#5. Class
#
#class Dog:
#    def __init__(self, name, breed):
#        self.name = name
#        self.breed = breed
#
#    def bark(self):
#        return f"{self.name} says woof!"
#
#my_dog = Dog("huliya", "stree-dog")
#print(my_dog.bark())
#
#
#6. OOPs
#
#Inheritance:
#-----------
#    This allows the child to derive attributes and methods from another class. It promotes code resuability.
#
#class Animal:
#    def xyz(self):
#        print("This is Animal class")
#
#class Cat(Animal):
#    def speak(self):
#        print("Meow")
#
#kitty = Cat()
#kitty.speak()
#kitty.xyz()
#
#Encapsulation:
#-------------
#    This is about hiding the internal state of an object and requiring all interaction to happen through methods. In python, we use a single or double underscore (__ or _) to sigal that a variable is private
#
#class BankAccount:
#    def __init__(self, balance):
#        self.__balance = balance  # Private Attribute
#
#    def deposit(self, amount):
#        if amount > 0:
#            self.__balance += amount
#
#    def get_balance(self):
#        return self.__balance
#
#
#acc = BankAccount(100)
#acc1 = BankAccount(100)
#
#acc.deposit(350)
#print(acc.get_balance())
#print(acc1.get_balance())
#
#
#Polymorphism:
#------------
#    It means many forms. 
#
#
#Abstraction:
#-----------
#    Abstraction hides complex implementation details and only shows the necessary features of an object. We use the abs module for this.
#
#
#from abc import ABC, abstractmethod
#
#class Shape(ABC):
#    @abstractmethod
#    def area(self):
#        pass
#
#class Square(Shape):
#    def __init__(self, side):
#        self.side = side
#    def area(self):
#        return self.side * self.side
#
#s = Square()
#
#Class Example:
#-------------
#class Book:
#    def __init__(self, title, author):
#        self.title = title
#        self.author = author
#
#class Library:
#    def __init__(self):
#        self.books = []
#
#    def add_book(self, book):
#        self.books.append(book)
#        print(f"Added: {book.title}")
#
#    def show_books(self):
#        for book in self.books:
#            print(f"- {book.title} by {book.author}")
#
#
#b1 = Book("Nayi Neralu", "S.L Bhairappa")
#myLib = Library()
#
#print(myLib.show_books())
#myLib.add_book(b1)
#myLib.show_books()
#
#
#7. Threading
#-------------
#Because of Global Interpreter Lock(GIL) python doesnt actually run the code at the same millisecond on multiple CPU cores.
#Instead they "take runs" very quickly. This makes the threading perfect for I/O bound tasks but less ideal for CPU bound taks.
#
#
#import threading
#import time
#
#def worker_task(name):
#    print(f"Thread {name} started")
#    time.sleep(2)
#    print(f"Thread {name} ended")
#
#my_thread_1 = threading.Thread(target=worker_task, args=("A",))
#my_thread_2 = threading.Thread(target=worker_task, args=("B",))
#my_thread_3 = threading.Thread(target=worker_task, args=("C",))
#my_thread_4 = threading.Thread(target=worker_task, args=("D",))
#
#my_thread_1.start()
#my_thread_2.start()
#my_thread_3.start()
#my_thread_4.start()
#
#for i in range(10):
#    print(i)
#
#my_thread_1.join()
#
#print("Main program complete.")
#
#my_thread_2.join()
#my_thread_3.join()
#my_thread_4.join()
#
#
#import threading 
#import time
#
#account_balance = 100
#balance_lock = threading.Lock()
#
#def deposit(amount):
#    global account_balance
#
#    with balance_lock:
#        local_copy = account_balance
#        local_copy += amount
#        time.sleep(0.1)
#        account_balance = local_copy
#
##t1 = threading.Thread(target=deposit, args=(1,))
##t2 = threading.Thread(target=deposit, args=(1,))
##t3 = threading.Thread(target=deposit, args=(1,))
##t4 = threading.Thread(target=deposit, args=(1,))
#
##t1.start()
##t2.start()
##t3.start()
##t4.start()
#
##t1.join()
##t2.join()
##t3.join()
##t4.join()
#
#threads = []
#
#for i in range(10):
#    t = threading.Thread(target=deposit, args=(1,))
#    threads.append(t)
#    t.start()
#
#for t in threads:
#    t.join()
#
#print(f"Final balance is: {account_balance}")
#
#from concurrent.futures import ThreadPoolExecutor
#import time
#
#def worker_task(name):
#    print(f"Thread {name} is started")
#    time.sleep(2)
#    print(f"Thread {name} is ended")
#
#with ThreadPoolExecutor(max_workers=4) as executor:
#    f1 = executor.submit(worker_task, "A") 
#    f2 = executor.submit(worker_task, "B") 
#    f3 = executor.submit(worker_task, "C") 
#    f4 = executor.submit(worker_task, "D") 
#
#    print(f1.result())
#    print(f2.result())
#    print(f3.result())
#    print(f4.result())
#
#8. Data Engineering (Python context)
#------------------------------------
#
#
#9. Multi Proccessing
#--------------------
#Each CPU cores gets its own python interpreter and its own memory space, effectively bypassing GIL.
#
#
#import multiprocessing
#import os
#
#def heavy_math(name):
#    print(f"Process {name} (ID: {os.getpid()}) is calculating...")
#    result = sum(i*i for i in range(10**7))
#    print(f"Process {name} finished.")
#
#if __name__ == "__main__":
#    p1 = multiprocessing.Process(target=heavy_math, args=("A",))
#    p2 = multiprocessing.Process(target=heavy_math, args=("B",))
#    p3 = multiprocessing.Process(target=heavy_math, args=("C",))
#
#    p1.start()
#    p2.start()
#    p3.start()
#
#    p1.join()
#    p2.join()
#    p3.join()
#
## multiprocessing.Queue
## multiprocessing.Pool
#
#10. SQL
#-------
#
#i. SELECT:
#SELECT * FROM Employee;
#SELECT Name, Salary FROM Employee;
#
#ii. WHERE
#SELECT Name FROM Employee
#WHERE Salary > 50000;
#
#iii. ORDER BY
#SELECT Name, Salary FROM Employee
#ORDER BY Salary DESC;
#
#iv. LIMIT
#SELECT Name FROM Employee
#ORDER BY Salary DESC
#LIMIT 5;
#
#
#JOINs:
#i. INNER JOIN
#SELECT Orders.Order_ID, Customers.Customer_Name
#FROM Orders
#INNER JOIN Customers ON Orders.Order_ID = Customers.Customer_ID;
#
#ii. LEFT JOIN
#SELECT Users.Name, Orders.Item
#FROM Users LEFTJOIN Orders
#ON Users.User_ID = Orders.User_ID;
#
#iii. RIGHT JOIN
#SELECT Users.Name, Orders.Item
#FROM Users RIGHTJOIN Orders
#ON Users.User_ID = Orders.User_ID;
#
#iv. FULL OUTER JOIN
#SELECT Users.Name, Orders.Item
#FROM Users OUTER JOIN Orders
#ON Users.User_ID = Orders.User_ID;
#
#v. CROSS JOIN: Creates cartissian products of all the rows
#
#SELECT DISTINCT ContryCode FROM City;
#SELECT * FROM City ORDER BY Population ASC; (DESC)
#SELECT * FROM City WHERE Population BETWEEN 5000 AND 10000;
#SELECT * FROM City WHERE ContryCode IN ('USA', 'JPN', 'IN');
#SELECT * FROM City WHERE Name LIKE 'NEW%';
#SELECT * FROM City WHERE Populatin IS NULL;
#SELECT COUNT(*) FROM City;
#SELECT SUM(Population) FROM City; (AVG, MAX, MIN)
#
#SELECT CountryCode, COUNT(*) AS city_count
#FROM City
#GROUP BY ContryCode;
#
#SELECT CountryCode, COUNT(*) AS city_count
#FROM City
#GROUP BY CountryCode
#HAVING COUNT(*) > 1;
#
#Assume tables:
#    City(id, name, country_id)
#    Country(id, country_name)
#
#SELECT City.name, Country.country_name
#FROM City INNER JOIN Country
#ON City.country_id = Country.id; (Similarly for LEFT JOIN and RIGHT JOIN)
#
#SELECT *
#FROM City FULL JOIN Country
#ON City.country_id = Country.id;
#
#SELECT A.name B.name
#FROM City A, City B
#WHERE A.Population > B.Population
#
#SELECT * FROM City
#WHERE Population > (
#    SELECT AVG(Population) FROM City
#);
#
#SELECT avg_pop
#FROM (SELECT AVG(Population) AS avg_pop FROM City) t;
#
#INSERT INTO City VALUES (1, 'Bengaluru', 'IN', 8000000):
#UPDATE CITY SET Population = 9000000 WHERE name = 'Bengaluru';
#DELETE FROM City WHERE name = 'Bengaluru';
#
#CREATE TABLE City(
#    id INT PRIMARY KEY,
#    name VARCHAR(50),
#    CountryCode CHAR(3),
#    population INT
#);
#
#DROP TABLE City;
#ALTER TABLE City ADD area INT;
#ALTER TABLE City DROP area;
#
#CREATE TABLE Country(
#    id INT PRIMARY KEY,
#    name VARCHAR(50)
#)
#
#SELECT name,
#CASE
#    WHEN Population > 10000 THEN 'Large_City'
#    ELSE 'Small_City'
#END As City_Type
#FROM City;
#
#WITH big_cities AS (
#    SELECT * FROM City WHERE population > 100000
#)
#SELECT * FROM big_cities;
#
#
#SELF JOIN
#---------
#ex: Employee Table
#| id | name  | manager_id |
#| -- | ----- | ---------- |
#| 1  | Alice | NULL       |
#| 2  | Bob   | 1          |
#| 3  | Carol | 1          |
#| 4  | Dave  | 2          |
#
#SELECT E.name AS employee M.name AS manager
#FROM Employee E
#JOIN Employee M
#ON E.manager_id = M.id;
#
#Output:
#| employee | manager |
#| -------- | ------- |
#| Bob      | Alice   |
#| Carol    | Alice   |
#| Dave     | Bob     |
#
#
#11. File handling
#------------------
#file = open("file path/file.txt", "w")
#file.write("Hello World!!")
#file.close()
#
#modes:
#    r -> read mode -> throws error if doesnt exists
#    w -> write mode -> creates if doesnt exists and overwrites if exists.
#    a -> append mode -> adds data to the end of the file without deleting the current data.
#    r+ ->   read/write mode -> allows you to both read and write from/to the same file.
#
#with open("file path/file.txt", "r") as file:
#    content = file.read()
#    print(content)
#
#with open("file path/file.txt", "r") as file:
#    for line in file:
#        print(line.strip()) # strip removes the new line character
#
#
#import os
#if os.path.exists("path/file.txt"):
#    with open("file path/file.txt", "r") as file:
#        for line in file:
#            print(line.strip())
#else:
#    print("File not found!")
#
#
#import json
#
#user_config = {
#    "model": "RandomForest",
#    "params": {"n_estimators": 100, "depth": ₹0}
#}
#
#with open("file path/config.json", "w") as f:
#    json.dum(user_config, f, indent=4)
#
#with open("file path/file.json", "r") as f:
#    loaded_data = json.load(f)
#
#print(loaded_data["model"])
#
#
#import pandas as pd
#
#data = {'Product': ['A', 'B'], 'Price': [1200, 800]}
#df = pd.DataFrame(data)
#
#df.describe() # Gives count, mean, max, min, std
#
#
#
#12. try-catch
#--------------
#
#try:
#    file = open("file_path/file.txt", "r")
#except FileNotFoundError:
#    print("File doesnt exists!")
#else:
#    print("File found successfully!")
#finally:
#    print("Always runs!!")
#
#
#13. AI hackathon: Driver Profiling
#----------------------------------
#Silhouette Score: It essentially measures how similar an object is to its own cluster(cohesion) compare to other cluster(separation)
#+1 -> Belongs to current cluster
#0  -> On Decision boundary
#-1 -> Belongs to other cluster
#
#Winzorization:  Clips extreme values(1st and 99th percentile). This prevents a single "extreme" drive from skewing the entire cluster structure. 
#
#OneHotEncoder: Converts categorical data(Train_Type, Region etc..) into binary format that algorithm can process.
#
#
#13. DNN
#--------
#DNN's primary job is to take complex data (such as image, text) and find patterns.
#To learn non-linear, complex relatinships.
#
#Key Component:
#    * Input Layer => Recieves the raw data
#    * Hidden Layer => Deep part of the deep learning. These layers extract features.
#    * Output Layer => Provides the final guess.
#
#Weight and Biases:
#    * A weight determines how much importance to give to a specific input.
#    * A Bias helps shifts the activation threshold.
#
#Activatin Function:
#    Like ReLu or Sigmoid, these decides if a "neuron" should fire. They allow the network to learn non-linear, complex relationships.
#
#How it learns:
#    * Forward Propagation => Data flows from input to output.
#    * Loss Function => The network checks its answer against the ground truth. The difference is "error".
#    * Back Propagation => Using an algorithm called Gradient Descent, the network works backward from the error to adjust the weights and biases to make the error smaller next time.
#
#    
#    * Perceptron (The Artificial Neuron):
#        Limitation: A signle neuron is a linear model. It can only learn decision boundary that are stright lines or hyperplane.
#    * Deep Feed Forward Neural Network:
#        These networks consist of multiple layers of neurons - an input layer, one or more hidden layer and an output layer.
#
#
#
#14. RL
#------
#RL is a paradigma where an agent(AI) learns to behave in an environment by taking an action and receiving an reward.
#
#    * An agent
#    * An environment
#    * State(s)
#    * Action(a)
#    * Reward(r)
#
#Key concepts:
#    * Policy(pi): The agent's strategy or rulebook for picking action based on the current state.
#    * Value function(v): The agent's estrimate of long term total reward it can get from a certain state.
#    * Q-Learning: 
#
#    MAB: Decision making:
#        * Concept:
#            This is the simplest form of RL, where agent repeatedly choose between k different actions to find which one gives the best reward.
#        * Requirement:
#            This introduces us to the fundamental Exploration vs Exploitation trade-off.
#        * Limitation: This is non-associative, which means it assumes only one state. It doesnt not handle the situation where the best action depends on the current state.
#        * Soltion:
#            Transitioning into Markov-Decision-Process(MDP) and Monte-Carlo-Methods(MCM) solve this by introducing multiple states and transitions.
#    
#    Monte-Carlo Methods (Learning from experience):
#        * Concept:
#            These methods learns from complete episodes of experience. By averaging the rewards received after visiting the state.
#        * Limitation:
#            It is computationally inefficient for large problems. Every state must be learned saperately, and it requires completing a full episode before any learning happens.
#        * Solution: Bootstrapping and Function Approximation.
#
#    Value Function Approximation:
#        * Concept:
#            Instead of giant table(Tabular learning) to store every state's value, we use a parameterized fucntion (like a neural network) to approximate values.
#        * Requirement:
#            If an agent learns that one state is "bad", it can infer that a similar looking states are also bad without visiting them.
#        * Soltion:
#            Policy Gradient Methods
#
#    Policy Gradients vs Actor-Critic(Direct Control):
#        * Actor learns the policy and the critic learns the value function to tell the actor how good the actions were.
#
#    Policy => This is an agent's strategy or brain. Its a mapping from states to actions. A rule book that tells the agent what to do in any given situation.
#    Value Function => This is an agent's prediction of future success. It answers: "If im in this state, how much total reward can i expect to get from here untill the end."
#    Overfitting => The model memorizes the training data but fails on new data.
#    Vanishing Gradient => In deep networks, updates becomes too small for the model to learn. Therefore use ReLu activation function instead of Tanh/Signmoid activation fucntion.
#    
#14. ML:
#-------
#Machine Learning is a way of building a system that learns patterns from data instead of being explicitely programmed, and use those patterns to make predictions and decisions.
#
#Confusion Matrix:
#                      |      Predicted Possitive        |      Predicted Negative      |
#    ------------------------------------------------------------------------------------
#                      |                                 |                              |
#       Actual True    |              TP                 |            FN                | 
#                      |                                 |                              |
#    ------------------------------------------------------------------------------------
#                      |                                 |                              |
#       Actual False   |              FP                 |            TN                |
#                      |                                 |                              |
#   ------------------------------------------------------------------------------------
#
#        FP -> Type-I error
#        FN -> Type-II error
#
#        Accuracy  =  (TP+TN) / (TP+TN+FP+FN) =>
#        Precision =  TP / (TP+FP)           => Use when FP are costly
#        Recall    =  TP / (TP+FN)           => Use when FN are costly
#        F1-Score  =  2 * (Precision * Recall / Precision + Recall)
#
#
#
#High Bias -> Because of poor assumption -> results into underfitting
#High Variance -> Because of over sensitivity to training data -> results into Overfitting
#
#Ensemble Learning: 
#    * Bagging: Train models independently on random samples and average their predictions -> Reduces Variance.
#    * Boosting: Train models sequentially -> Reduces Bias
#
#Normalization:
#    If the features are on different scale, large values dominates thats why noramalization is required to give equal importance to every features.
#Standardization:
#    Helps in faster gradient descent
#


"""
def f() -> int: return 10
def f() -> float: return 10.2
def f() -> complex: return 2+3j
def f() -> bool: return True
def f() -> str: return 'hello'


def f() -> list: return [1, 2, 3]
def f() -> tuple: return (1, 2, 3)
def f() -> set: return {1, 2, 3}
def f() -> dict: return {"a": 1}

def f(a: int, b: float, c: complex, d: bool, e: str): pass
def f(a: list,
      b: tuple,
      c: set,
      d: dict,
      e: frozenset): pass

Slicing:
-------
    Synatx: sequence[start : stop : step]

    seq[i:j]      -> slices from i to j-1
    seq[:j]       -> slices from 0 to j-1
    seq[i:]       -> slices from i to end
    seq[:]        -> full copy

    seq[::2]      -> every second element
    seq[1:10:3]   -> every 3rd element from 1 to 9
    seq[-n:]      -> last 'n' elements
    seq[:-n]      -> all except lat 'n' elements
    seq[-5:-2]    -> middle using negative
    
    seq[::1]      -> full copy
    seq[::-1]     -> reverse entire sequence
    seq[8:2:-1]   -> reverse middle part
    seq[:2:-1]    -> reverse from end


    lst[1:3] = [10, 20]     -> replace
    lst[2:2] = [99]         -> insert
    lst[1:3] = []           -> delete
"""



# Programs

def reverseString(s: str) -> str:
    chars = list(s)

    left = 0
    right = len(chars) - 1


    while(left <= right):
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)

#print(reverseString("Nithin"))

#chars = list("Nithin")
#chars.reverse()
#print("".join(chars))


def getMinMax(a, n):
    mini = a[0]
    maxi = a[0]

    for i in a:
        if mini > i: mini = i
        if maxi < i: maxi = i
#    for i in range(n):
#        if mini > a[i]: mini = a[i]
#        if maxi < a[i]: maxi = a[i]

    return (mini, maxi)

arr = [3, 2, 1, 56, 10000, 167]
result = getMinMax(arr, 6)
#print(f"mini = {result[0]} and maxi = {result[1]}")


import heapq

def Smallest(arr):
    min_heap = []
    for a in arr:
        heapq.heappush(min_heap, -a)

    return min_heap

def Biggest(arr):
    max_heap = []
    for a in arr:
        heapq.heappush(max_heap, a)

    return max_heap

def kthSmallest(arr, k):
    max_heap = []
    for i in range(k):
        heapq.heappush(max_heap, -arr[i])
    for i in range(k, len(arr)):
        if -arr[i] > max_heap[0]:
            heapq.heapreplace(max_heap, -arr[i])

    return -max_heap[0]

def kthBiggest(arr, k):
    min_heap = []
    for i in range(k):
        heapq.heappush(min_heap, arr[i])
    for i in range(k, len(arr)):
        if arr [i] > min_heap[0]:
            heapq.heapreplace(min_heap, arr[i])

    return min_heap[0]



arr = [4, 5, 9,8,7, 2, 3]
#arr.sort()
#print("Sorted Array: ", arr)
#heapq.heapify(arr)
#print(arr)
print(Smallest(arr))
print(Biggest(arr))


print("1st Smallest: ", kthSmallest(arr, 1))
print("2nd Smallest: ", kthSmallest(arr, 2))
print("3rd Smallest: ", kthSmallest(arr, 3))
print("4th Smallest: ", kthSmallest(arr, 4))
print("5th Smallest: ", kthSmallest(arr, 5))
print("6th Smallest: ", kthSmallest(arr, 6))
print("7th Smallest: ", kthSmallest(arr, 7))

print("1st Biggest: ", kthBiggest(arr, 1))
print("2nd Biggest: ", kthBiggest(arr, 2))
print("3rd Biggest: ", kthBiggest(arr, 3))
print("4th Biggest: ", kthBiggest(arr, 4))
print("5th Biggest: ", kthBiggest(arr, 5))
print("6th Biggest: ", kthBiggest(arr, 6))
print("7th Biggest: ", kthBiggest(arr, 7))



"""
lst = [] or 
lst = list()
lst.append(10)
lst.extend([4, 5, 6])
lst.isert(2, 99)
lst.remove(3)
lst.pop()
lst.pop(2)
lst.clear()
lst.count()
lst.reverse()

s = set()
s = {1, 3, 4, 4}
s.add(4)
s.update([5, 6, 7])
s.remove(3)
s.discard(3)
s.pop()
s.clear()

d = {} or 
d = dict()
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)
d["a"]
d.get("a")
d["a"] = 99
d.update({"a": 100})
d.pop("a")
d.popitem()
del d["b"]
d.clear()
d.keys()
d.values()
d.items()

t = () or 
t = tuple()
t = (1, 2, 3)
t.count(2)
t.index(3)
t1, t2, t3 = (1, 2, 3)
len(t)
max(t)
min(t)
sum(t)

"""

def isValid(s: str) -> bool:
    stack = []
    mapping = {
            ")": "(",
            "}": "{",
            "]": "[",
            }

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


"""Singly Linked List"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def reversell(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        self.head = prev

    def display(self):
        current = self.head

        while(current):
            print(current.data, end=" --> ")
            current = current.next
        print(None)


ll = LinkedList()
ll.append(9)
ll.append(5)
ll.append(6)
ll.append(2)
ll.append(0)
ll.append(8)
ll.display()
ll.reversell()
ll.display()




"""Doubly Linked List"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Add node to the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        new_node.prev = curr  # Link the new node back to the current last node

    # Print forwards
    def display_forward(self):
        curr = self.head
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.next
        print("None")

    # Print backwards (starting from the last node)
    def display_backward(self):
        curr = self.head
        if not curr: return
        
        # 1. Go to the end
        while curr.next:
            curr = curr.next
            
        # 2. Walk backwards using .prev
        while curr:
            print(curr.data, end=" <-> ")
            curr = curr.prev
        print("None")


dll = DoublyLinkedList()
dll.append(1)
dll.append(3)
dll.append(5)
dll.append(7)
dll.append(2)
dll.append(4)
dll.append(6)
dll.display_forward()
dll.display_backward()



"""Binary Tree"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, data=None):
        self.root = Node(None)

    def insert(self, data):
        if self.root.data is None:
            self.root.data = data
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, curr, data):
        if data < curr.data:
            if curr.left is None:
                curr.left = Node(data)
            else:
                self._insert_recursive(curr.left, data)
        elif data > curr.data:
            if curr.right is None:
                curr.right = Node(data)
            else:
                self._insert_recursive(curr.right, data)

    def display_inorder(self, node):
        if node and node.data is not None:
            self.display_inorder(node.left)
            print(node.data, end=" ")
            self.display_inorder(node.right)

    def get_height(self, node):
        if node is None or node.data is None:
            return 0

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        return max(left_height, right_height) + 1


bst = BinaryTree()

# Notice the tree exists but data is None
print(f"Initial root data: {bst.root.data}") 

# Insert values
numbers = [15, 10, 20, 8, 12, 17, 25]
for n in numbers:
    bst.insert(n)

print("In-order Traversal (Sorted):", end=" ")
bst.display_inorder(bst.root)
print(f"\nTree Height: {bst.get_height(bst.root)}")

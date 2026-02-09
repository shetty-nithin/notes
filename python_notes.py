"""
1. Python is an interpreted language: An interpreter reads it and executes it immediately.
   compiled into bytecode (.pyc) -> then this .pyc will be excecutes by Python Virtual Machine 

2. Memory Management:
   Python uses Automatic Garbage Collection. It means, automatically allocates memory when the object is
   createdcreated and frees the memory when the objects are not longer needed.  

3. Data Structures:
    * List       => Ordered collections, stacks           => O(n)  => ex: a = [1, 2, 3]  => arr.append(), arr[1], arr[2] = 99, arr.pop(), arr.remove(20), del arr[0]
    * Set        => Unique iterms                         => O(1)  => ex: a = {1, 2, 3}  => arr.add(), arr.remove(), arr.discard(), arr.pop()
    * Dictionary => Key-Value pair                        => O(1)  => ex: a = {"n": 1}   => arr["a"] = 1, arr["a"], arr.get("a"), arr["a"] = 99, arr.pop("a"), del arr["a"]
    * Deque      => Efficient queues(fast appends/pops)   => O(1)  => ex: a = 
    * Tuple                                               =>       => ex: a = (1, 2, 3)  => arr[1], update and delete are not allowed.
    * Stack      =>                                       =>       =>                    => stack.append(), stack[-1], stack.pop()
    * Queue      =>                                       =>       =>                    => q.append(), q[0], q.popleft()
    * Heap/Priority Queue  =>                             =>       =>                    => heap[], heapq.heappush(heap, 5), heapq.heappop(heap)
    * Linked List



    Data Structure     |     Ordered?           |             Example           |       Mutable?
----------------------------------------------------------------------------------------------------------
         List          |        Yes             |          [1, 2, 3]            |         Yes
         Tuple         |        Yes             |          (1, 2, 3)            |            No
         String        |        Yes             |          "Nithin"             |            No
         Range         |        Yes             |          range(5)             |            No
         Dict          |        Yes             |          {"a": 1, "b": 2}     |         Yes
         Set           |        No              |         {1, 2, 3}             |         Yes
         Frozenset     |        No              |         frozenset({1, 2, 3})  |            No

4. Itertools provides fast, memory efficient looping construct without manual nested loops.
    import itertools
    from itertools import combinations
    from itertools import count
    
5. Class

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("huliya", "stree-dog")
print(my_dog.bark())


6. OOPs

Inheritance:
-----------
    This allows the child to derive attributes and methods from another class. It promotes code resuability.

class Animal:
    def xyz(self):
        print("This is Animal class")

class Cat(Animal):
    def speak(self):
        print("Meow")

kitty = Cat()
kitty.speak()
kitty.xyz()

Encapsulation:
-------------
    This is about hiding the internal state of an object and requiring all interaction to happen through methods. In python, we use a single or double underscore (__ or _) to sigal that a variable is private

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private Attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(100)
acc1 = BankAccount(100)

acc.deposit(350)
print(acc.get_balance())
print(acc1.get_balance())


Polymorphism:
------------
    It means many forms. 


Abstraction:
-----------
    Abstraction hides complex implementation details and only shows the necessary features of an object. We use the abs module for this.


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

s = Square()

Class Example:
-------------
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def show_books(self):
        for book in self.books:
            print(f"- {book.title} by {book.author}")


b1 = Book("Nayi Neralu", "S.L Bhairappa")
myLib = Library()

print(myLib.show_books())
myLib.add_book(b1)
myLib.show_books()


7. Threading
-------------
Because of Global Interpreter Lock(GIL) python doesnt actually run the code at the same millisecond on multiple CPU cores.
Instead they "take runs" very quickly. This makes the threading perfect for I/O bound tasks but less ideal for CPU bound taks.


import threading
import time

def worker_task(name):
    print(f"Thread {name} started")
    time.sleep(2)
    print(f"Thread {name} ended")

my_thread_1 = threading.Thread(target=worker_task, args=("A",))
my_thread_2 = threading.Thread(target=worker_task, args=("B",))
my_thread_3 = threading.Thread(target=worker_task, args=("C",))
my_thread_4 = threading.Thread(target=worker_task, args=("D",))

my_thread_1.start()
my_thread_2.start()
my_thread_3.start()
my_thread_4.start()

for i in range(10):
    print(i)

my_thread_1.join()

print("Main program complete.")

my_thread_2.join()
my_thread_3.join()
my_thread_4.join()


import threading 
import time

account_balance = 100
balance_lock = threading.Lock()

def deposit(amount):
    global account_balance

    with balance_lock:
        local_copy = account_balance
        local_copy += amount
        time.sleep(0.1)
        account_balance = local_copy

#t1 = threading.Thread(target=deposit, args=(1,))
#t2 = threading.Thread(target=deposit, args=(1,))
#t3 = threading.Thread(target=deposit, args=(1,))
#t4 = threading.Thread(target=deposit, args=(1,))

#t1.start()
#t2.start()
#t3.start()
#t4.start()

#t1.join()
#t2.join()
#t3.join()
#t4.join()

threads = []

for i in range(10):
    t = threading.Thread(target=deposit, args=(1,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final balance is: {account_balance}")

from concurrent.futures import ThreadPoolExecutor
import time

def worker_task(name):
    print(f"Thread {name} is started")
    time.sleep(2)
    print(f"Thread {name} is ended")

with ThreadPoolExecutor(max_workers=4) as executor:
    f1 = executor.submit(worker_task, "A") 
    f2 = executor.submit(worker_task, "B") 
    f3 = executor.submit(worker_task, "C") 
    f4 = executor.submit(worker_task, "D") 

    print(f1.result())
    print(f2.result())
    print(f3.result())
    print(f4.result())

8. Data Engineering (Python context)
------------------------------------


9. Multi Proccessing
--------------------
Each CPU cores gets its own python interpreter and its own memory space, effectively bypassing GIL.


import multiprocessing
import os

def heavy_math(name):
    print(f"Process {name} (ID: {os.getpid()}) is calculating...")
    result = sum(i*i for i in range(10**7))
    print(f"Process {name} finished.")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=heavy_math, args=("A",))
    p2 = multiprocessing.Process(target=heavy_math, args=("B",))
    p3 = multiprocessing.Process(target=heavy_math, args=("C",))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

# multiprocessing.Queue
# multiprocessing.Pool

10. SQL
-------

i. SELECT:
SELECT * FROM Employee;
SELECT Name, Salary FROM Employee;

ii. WHERE
SELECT Name FROM Employee
WHERE Salary > 50000;

iii. ORDER BY
SELECT Name, Salary FROM Employee
ORDER BY Salary DESC;

iv. LIMIT
SELECT Name FROM Employee
ORDER BY Salary DESC
LIMIT 5;


JOINs:
i. INNER JOIN
SELECT Orders.Order_ID, Customers.Customer_Name
FROM Orders
INNER JOIN Customers ON Orders.Order_ID = Customers.Customer_ID;

ii. LEFT JOIN
SELECT Users.Name, Orders.Item
FROM Users LEFTJOIN Orders
ON Users.User_ID = Orders.User_ID;

iii. RIGHT JOIN
SELECT Users.Name, Orders.Item
FROM Users RIGHTJOIN Orders
ON Users.User_ID = Orders.User_ID;

iv. FULL OUTER JOIN
SELECT Users.Name, Orders.Item
FROM Users OUTER JOIN Orders
ON Users.User_ID = Orders.User_ID;

v. CROSS JOIN: Creates cartissian products of all the rows

SELECT DISTINCT ContryCode FROM City;
SELECT * FROM City ORDER BY Population ASC; (DESC)
SELECT * FROM City WHERE Population BETWEEN 5000 AND 10000;
SELECT * FROM City WHERE ContryCode IN ('USA', 'JPN', 'IN');
SELECT * FROM City WHERE Name LIKE 'NEW%';
SELECT * FROM City WHERE Populatin IS NULL;
SELECT COUNT(*) FROM City;
SELECT SUM(Population) FROM City; (AVG, MAX, MIN)

SELECT CountryCode, COUNT(*) AS city_count
FROM City
GROUP BY ContryCode;

SELECT CountryCode, COUNT(*) AS city_count
FROM City
GROUP BY CountryCode
HAVING COUNT(*) > 1;

Assume tables:
    City(id, name, country_id)
    Country(id, country_name)

SELECT City.name, Country.country_name
FROM City INNER JOIN Country
ON City.country_id = Country.id; (Similarly for LEFT JOIN and RIGHT JOIN)

SELECT *
FROM City FULL JOIN Country
ON City.country_id = Country.id;

SELECT A.name B.name
FROM City A, City B
WHERE A.Population > B.Population

SELECT * FROM City
WHERE Population > (
    SELECT AVG(Population) FROM City
);

SELECT avg_pop
FROM (SELECT AVG(Population) AS avg_pop FROM City) t;

INSERT INTO City VALUES (1, 'Bengaluru', 'IN', 8000000):
UPDATE CITY SET Population = 9000000 WHERE name = 'Bengaluru';
DELETE FROM City WHERE name = 'Bengaluru';

CREATE TABLE City(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    CountryCode CHAR(3),
    population INT
);

DROP TABLE City;
ALTER TABLE City ADD area INT;
ALTER TABLE City DROP area;

CREATE TABLE Country(
    id INT PRIMARY KEY,
    name VARCHAR(50)
)

SELECT name,
CASE
    WHEN Population > 10000 THEN 'Large_City'
    ELSE 'Small_City'
END As City_Type
FROM City;

WITH big_cities AS (
    SELECT * FROM City WHERE population > 100000
)
SELECT * FROM big_cities;


SELF JOIN
---------
ex: Employee Table
| id | name  | manager_id |
| -- | ----- | ---------- |
| 1  | Alice | NULL       |
| 2  | Bob   | 1          |
| 3  | Carol | 1          |
| 4  | Dave  | 2          |

SELECT E.name AS employee M.name AS manager
FROM Employee E
JOIN Employee M
ON E.manager_id = M.id;

Output:
| employee | manager |
| -------- | ------- |
| Bob      | Alice   |
| Carol    | Alice   |
| Dave     | Bob     |


11. File handling
------------------
file = open("file path/file.txt", "w")
file.write("Hello World!!")
file.close()

modes:
    r -> read mode -> throws error if doesnt exists
    w -> write mode -> creates if doesnt exists and overwrites if exists.
    a -> append mode -> adds data to the end of the file without deleting the current data.
    r+ ->   read/write mode -> allows you to both read and write from/to the same file.

with open("file path/file.txt", "r") as file:
    content = file.read()
    print(content)

with open("file path/file.txt", "r") as file:
    for line in file:
        print(line.strip()) # strip removes the new line character


import os
if os.path.exists("path/file.txt"):
    with open("file path/file.txt", "r") as file:
        for line in file:
            print(line.strip())
else:
    print("File not found!")


import json

user_config = {
    "model": "RandomForest",
    "params": {"n_estimators": 100, "depth": ₹0}
}

with open("file path/config.json", "w") as f:
    json.dum(user_config, f, indent=4)

with open("file path/file.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data["model"])


import pandas as pd

data = {'Product': ['A', 'B'], 'Price': [1200, 800]}
df = pd.DataFrame(data)

df.describe() # Gives count, mean, max, min, std



12. try-catch
--------------

try:
    file = open("file_path/file.txt", "r")
except FileNotFoundError:
    print("File doesnt exists!")
else:
    print("File found successfully!")
finally:
    print("Always runs!!")










"""


1. Difference between the C struct and C++ strct
   C : 
        i. Only data members are allowed, it cannot have the member function.
        ii. Cannot have static members.
        iii. Cannot have constructor inside the structure.
        iv. Direct initialization of data members are not possible.
        v. Writing a 'struct' keyword is neccessary to declare the structure type variable.
        vi. It does not have access modifiers. 
        vii. Only pointers to structure are allowed.
        viii. SizeOf operator will generate 0 for an empty structure.
        ix. Data hiding is not possible.

   C++ :
        i. It can hold both data member and member functions.
        ii. Can have static members.
        iii. Constructor can be created inside the structure.
        iv. Direct initialization of data members are possible.
        v. 'struct' keyword is not neccessary.
        vi. This supports access modifiers.
        vii. Can have both pointers and reference to the structure.
        viii. SizeOf operator will generate 1 for an empty structure.
        ix. Data hiding is possible.

    Both in C and C++, members of the structure have "public" visibility by default.


1. Difference between the structure and class in C++.
    Class : 
        i. Member of a class are "private" by default. 
        ii. It declares by using the keyword "Class"
        iii. It is normally used for data abstraction and further inheritance.

    Structure : 
        i. "public" by default.
        ii. It declares by using the "struct" keyword.
        iii. It is normally used for grouping of data.


3. OOP :
    The main aim of th OOPs is to bind together the data and functions
    that operate on them so that no other part of the code can access this
    data except that function.

    Characteristics of an object oriented programming language:
    1. Class
    2. Object
    3. Encapsulation
    4. Abstraction
    5. Polymorphism
    6. Inheritance
    7. Dynamic Binding
    8. Message Passing

    Encapsulation : 
            In normal terms, Encapsulation is defined as 
    wrapping up of data and information under a single unit. In OOPs,
    encapsulation is defined as binding together the  data and member
    functions that manipulates these data members. 
    Encapsulation also leads to data abstraction or hiding. Using of 
    encapsulation also hides the data.

    Abstraction :
            Abstraction means displaying only essential information
    and hiding the details. Data abstraction refers to providing the
    only essential information about the data to the outside world,
    hiding the background details or implementation.
        i. Abstraction using Class :
            We can implement abstraction in C++ using classes. The
    class can helps us to group the data members and member functions
    using available access modifiers. A class can decide which data
    member will be visible to the outside world and which is not.
        ii. Abstraction in Header files :
            For example pow(). 

    Polymorphism : 
            The word polymorphism means having many forms. A person
    at the same time can have different characteristics. Like a man at 
    the same time is a father, a husband, an employee. So the same 
    person possess the different behaviour in different situation.
    This is called polymorphism.
    C++ supports operator overloading and function overloading.
        i. Operator Overloading :
            The process of making an operator to exhibit different
            behaviours in different instances is known as operator overloading.
        ii. Function Overloading :
            Function overloading is using single function name to perform
            different types of tasks

        Types of Polymorphism :
        i.  Compile Time Polymorphism
            a. Function Overloading
            b. Operator Overloading
        ii. Run Time Polymorphism
            a. Virtual Functions

        Functions can be overloaded by changing the number of arguments or/and
        chaging the type of arguments. 
        Functions cannot be overloaded if the return types are different.

        C++ has the ability to provide the operator with a special meaning
        for a data type, this ability is known as Operator Overloading.

        Overloading v/s Overriding:
            Overriding is achieved at run time. It is the redefinition of
        base class function in its derived class with same signature i.e.,
        return type and parameters.

        Virtual Function :
            A virtual function is a member function that is declared
        in the base class using the keyword virtual and is re-defined(overriden)
        in the derived class.

        Dynamic Binding :
                In Dynamic binding, the code to be executed in response
        to function call is decided at runtime. C++ has virtual functions
        to suppor this.

    Inheritance :
            The capability of a class to derive properties and characteristics
    of another class is called inheritance. (sub class <-- super class)
    A derived class does not inherit access of private data members.
        1. class ABC : private XYZ {}            //private derivation
        2. class ABC : public XYZ {}            //public derivation
        3. class ABC : protected XYZ {}            //protected derivation
        4. class ABC: XYZ {}                    //private derivation by default

        When a base class is privately inherited by the derived class, public
    members of the base class becomes the private members of the derived class.
    Therfore the public members of the base class can only be accessed
    by the member functions of the derived class. They are inaccessible
    to the object of the derived class.
        When the base class is publicly inherited by the derived class,
    public members of the base class also become the public members of
    the derived class. Therfore the public members of the base class are
    accessible by the object of the derived class as well as by the member
    functions of the derived class. 

    Modes of Inheritance: There are 3 modes of inheritance.
        Public Mode: 
            If we derive a subclass from a public base class. Then the
            public member of the base class will become public in the 
            derived class and protected members of the base class will
            become protected in the derived class.
        Protected Mode: 
            If we derive a subclass from a Protected base class. Then 
            both public members and protected members of the base class
            will become protected in the derived class.
        Private Mode: 
            If we derive a subclass from a Private base class. Then 
            both public members and protected members of the base 
            class will become Private in the derived class. 
        
        Note: The private members in the base class cannot be 
              directly accessed in the derived class
    
    Types Of Inheritance:-
        1. Single inheritance :
                In single inheritance, a class is allowed to inherit 
                from only one class. i.e. one subclass is inherited by 
                one base class only.
        2. Multilevel inheritance :
                Multiple Inheritance is a feature of C++ where a 
                class can inherit from more than one class. i.e 
                one subclass is inherited from more than one base class.
        3. Multiple inheritance :
                In this type of inheritance, a derived class is 
                created from another derived class.
        4. Hierarchical inheritance :
                In this type of inheritance, more than one subclass is 
                inherited from a single base class. i.e. more than one 
                derived class is created from a single base class.
        5. Hybrid inheritance :
                Hybrid Inheritance is implemented by combining more than 
                one type of inheritance. For example: Combining 
                Hierarchical inheritance and Multiple Inheritance. 
        6. Multipath inheritance :
                This is a A special case of hybrid inheritance.
                A derived class with two base classes and these two 
                base classes have one common base class is called 
                multipath inheritance.
                There are 2 Ways to Avoid this Ambiguity:
                    i. Avoiding ambiguity using the scope resolution operator
                    ii. Avoiding ambiguity using the virtual base class

    Message Passing: 
            Objects communicate with one another by sending and 
    receiving information to each other. A message for an object is 
    a request for execution of a procedure and therefore will 
    invoke a function in the receiving object that generates the 
    desired results. Message passing involves specifying the name 
    of the object, the name of the function and the information to 
    be sent.


    Stream : 
            In C++, there are number of stream classes for defining
    various streams related with files and for doing input-output operations.
    All these classes are defined in the file "iostream.h".
             Heirarchy of Stream
             --------------------

            ----------ios-----------
            |          |            |
        istream     streambuf     ostream
            |__________|____________|
                       |
                    iostream


    Data Types : 
            All variables use data type during declaration to restrict
    the type of data to be stored.
        i. Primary or Built-in or Fundamentals data type
        ii. Derived data types
        iii. User-defined data types

       Primary                  Derived            User-defined
       -------                  -------            ------------ 
       Integer                  Function            Class
       Character                Array               Structure
       Boolean                  Pointer             Union
       Floating Point           Reference           Enum
       Double Floating Point                        Typedef
       Void
       Wide Character

    Data type modifiers are used with built-in data types to modify the
    length of data that a particular data type can hold.
    Signed       Unsigned        Long        Short
    ------       --------        ----        -----
    Integer      Integer         Integer     Integer
    Char         Char            Char        Char
    Long-Prefix  Short-Prefix

    Macro Constants : INT_MAX, INT_MIN, SHRT_MAX, SHRT_MIN, etc...

Dynamic Memory Allocation in C : 
    DMA means changing the size of the data structure during the runtime.

    4 functions are :
        malloc(), calloc(), free() and realloc() --> <stdlib.h>

        malloc() : 
            The malloc or memory allocation method in C is used to
        dynamically allocate a signle large block of memory with the 
        specified size. It returns a pointer of type void which can be
        cast into a pointer of any form. It doesnt initialize the memory
        at execution time. So that it has initialized each block with the
        default garbage value initially.
            Syntax : ptr = (cast-type*) malloc(byte-size)
            example : ptr = (int*) malloc(100*sizeof(int))

        calloc() : 
            calloc or contiguous allocation method in C is used to dynamically
        allocate the specified number of blocks of memory of the specified
        type. It is very much similar to malloc() bu has 2 different points
        and these are : 
            i. It initializes each block with a default value 0.
            ii. It has 2 parameters or arguments as compare to malloc()

            Syntax : (cast-type*) calloc(n, element-size)
            example : (float*) calloc(25, sizeof(float))

        free() :
            free method in C is used to dynamically de-allocate the memory.
        The memory allocated using function malloc() and calloc() is not de-allocated
        on their own. Hence the free() method is used.
            Syntax : free(ptr)

        realloc() :
            realloc or re-allocation method in C is used to dynamically 
        change the memory allocation of a previously allocated memory. In
        other words, if the memory previously allocated with the help of
        malloc() or calloc() is insuffiecient, realloc can be used to
        dynamically re-allocated memory. 
            Syntax : prt = realloc(ptr, newSize)
            
    
Dynamic Memory Allocation in C++ : 
    i. Static memory allocation can only be done on stack whereas dynamic
memory allocation can be done on both stack and heap. 
    ii. DMA in C/C++ refers to performig memory allocation manually by a programmer.
    iii. For dynamically allocated memory like “int *p = new int[10]”, it is the 
programmer’s responsibility to deallocate memory when no longer 
needed. If the programmer doesn’t deallocate memory, it causes a 
memory leak (memory is not deallocated until the program terminates). 
    example : int *p = new int[10];
              delete[] p;

DMA of 2D array : 
    void main(){
        int **p;
        int nr, nc, r, c;

        p = new int*[nr];
        for(r=0; r<nr; r++){
            p[r] = new int[nc];
        }

        delete p;
    }

Reference Data Types : 
    When a variable is declared as a reference, it becomes an alternative
name for an existing variable. A variable can be declared as a reference
by putting '&' in the declaration.
    Example : 
        function swapfun(int& a, int& b){
            int temp = a;
            a = b;
            b = temp;
        }
        int main(){
            swapfun(a, b)
        }
        function
    Application :
        i. Modify the passed parameter in the function
        ii. Can avoid a copy of large structures.
        iii. In for each loop to modify all the objects
             example ; for(int& x : vectr){
                            x = x + 5;
                       }
        iv. For each loop to avoid the copy of objects.

Reference v/s Pointers : 
    Both reference and pointers can be used to change the local variables
of one function inside another function. Both of them can also be used
to save copying of big objects when passed as arguments to functions or
returned from functions, to get efficiency gain. Despite the above similarities
there are the following differences between the reference and pointers.

    i. A pointer can be declared as void, but a reference cannot be void.
        example : 
            int a = 10;   
            void* aa = &a;    // it is valid
            void& ar = a;     // it is not valid 

    ii. The pointer variable has n-level/multiple levels of indirections i.e.,
        single-pointer, double-pointer, triple-pointer. Wherease, the reference
        variable has only one level of indirection. 

    iii. Reference variable cannot be updated.
    iv.  Reference variable is an internal pointer.
    v.   Declaration of reference variable is preceded with the '&' symbol

References are less powerful than pointers : 
    i. Once the reference is created, it cannot be later made to reference to
    another object. It cannot be reset. 
    ii. Reference cannot be NULL. Pointers are often made NULL.
    iii. A reference must be initialized when declared.

    Due to above restriction, reference cannot be used in C++ for 
    implementing the data structures like Linked List, Tree etc....

    But in Java, reference doesn't have the above restriction, and hence
    can be used to implement all those data structures.

References are safer and easier to use.

Constructor in C++ : 
    i. Both constructor and destructor should be declared in the "public" area.
    ii. They dont have return type.
    iii. If we do not specify a constructor, C++ compiler generated a
         default constructor for object (expects no parameters and has an
         empty body)
    iv. Constructor can be declared virtual.
    v. Constructor cannot be inherited.

    There are 3 types of constructor:
    i. Default/zero-argument constructor
    ii. Parameterized (helps in overloading of a constructor)
    iii. Copy constructor

    Constructor can be declared inside or outside the class
    Syntax : 
        <class name> (list of parameters){} ---> inside the class
        <class name>::<class name> (list of parameters){} ---> outside the class

    Copy Constructor : 
        A copy constructor is a member function that initializes an object
    using another object of the same class. 
    example :
        class Sample {
            private:
                int id;
            public:
                void init(int x){
                    id = x;
                }
                Sample(Sample &t){
                    id = t.id;
                }
                void display(){
                    cout << "ID = " << id << endl;
                }
        }

        int main(){
            Sample obj1;
            obj1.init(10);

            Sample obj2(obj1);
            obj2.display();
            return 0;
        }

Destructor in C++ :
    i. Destructor destroys the class object created by the contructor.
    ii. Destructor has the same name as their class name preceded by a tilde(~) sybol.
    iii. Cannot be overloaded
    iv. Not required any argument and doesnot returns anything.
    v. It is automatically called when the object goes out of scope.
    vi. Destructor releases memory space occupied by the objects generated
        by the constructor.
    vii. In destructor, objects are destroyed in the reverse of object
         creation.
    viii. Cannot be declared as static and const.

    Syntax : 
        ~ <class name> (){} ---> inside the class
        <class name>:: ~ <class name> (){} ---> outside the class


Friend Function :
    i. Friend function declaration should be conducted inside the class
    with the keyword "friend".
    ii. Definition should write outside the class without the "friend" keyword.
    iii. Friend function can be introduced to any number of classes.
    iv. Friend functions are having objects as arguments.
    v. It should be invoked normally like other functions.
    vi. This function can be declared anywhere in the class (public, protected and private).
        Example : 
            class One{
                public:
                    void geta(){}
                    friend void biggest(One t1, Two t2); 
            } 
            class Two{
                public:
                    void getb(){}
                    friend void biggest(One t1, Two t2);
            }

            void biggest(One t1, Two t2){}

            int main(){
                One t1;
                Two t2;
                t1.geta();
                t2.getb();
                biggest(t1, t2);
            }

    Advantages : 
        i. Able to access the members without the need of inheritance.
        ii. Acts as a bridge between 2 classes by accessing their private data.
        iii. Can declare in any part of the class (private, protected or public).
    Disadvantages : 
        i. Can access the private data of the class from outside the calss, it violates
        the law of data hiding.
        ii. Cannot do any run time polymorphism.

Friend Class : 
    Friend function is a non-member function of a class and it has the 
access only to the private data of that class. 
    To access the whole data of a class from another class, we use friend class.
    Example : 
        #include <iostream>
        using namespace std;
        
        class GFG {
            private:
                int private_variable;
            protected:
                int protected_variable;
            public:
                GFG(){
                    private_variable = 10;
                    protected_variable = 99;
                }
            
                // friend class declaration
                friend class F;
        };

        class F {
            public:
                void display(){};
        }

        int main(){}


Static Data Member in C++ (SDM) : 
    i. When a class contains a normal data member, then each object of this 
       class constains one instance of this data members.
    ii. Wherease, when a class contains a static data member, then this will
        will become class member not an object memeber. That means, the static
        data member is same for all the objects of this calss.
    iii. SDMs are initialized with the value 0 automatically.
    iv. SDM should be declared inside the class using the keyword "static"
        and defined outside the class using the syntax as below.
        syntax : data_type class_name :: data_member = value
        example : int Test :: a = 10;
    v. SDM should be under public area.
    vi. We use SDM to maintain the relationship between various object of this class.

Static Member Function in C++ (SMF) : 
    i. SMF are designed to operate the SDMs. And it does not work on
    non static data members.
    ii. SMF never associates with "this" keyword.
    iii. SMF is associates with both the class and object name.
    iv. SMF cannot be CONST/VIRTUSL/VOLATILE.
    v. No need to call with object name.

Const data member in a class : 
    const data member should be initialized inside the constructor.
Const member function in a class : 
    Constant member functions are those functions that are denied
    permission to change the values of the data members of their
    class. To make a member function constant, the keyword “const”
    is appended to the function prototype and also to the function
    definition header.
        The idea of const function is not to allow them to modify the
    object on which they are called. It is recommended practice to make
    as many functions const as possible so that accidental changes to
    objects are avoided.


Pure Virtual Function & Abstract Classes in C++ : 
    Sometimes implementation of all function cannot be provided in a base
class because we don’t know the implementation. Such a class is called abstract class.
    For example an Animal class doesn’t have implementation of move()
(assuming that all animals move), but all animals must know how to move.
We cannot create objects of abstract classes.

    A pure virtual function (or abstract function) in C++ is a virtual function
for which we can have implementation, But we must override that function in the
derived class, otherwise the derived class will also become abstract class.
    PVF is declared in the base class but the definition will be in the 
derived class. It is also called as do nothing function.
    example : 
        class Shapes {
            public:
                virtual float findArea() = 0;
        }

        class Triangle : public Shapes{
            public:
                float findArea(){
                    return 0.5*w*h;
                }
        }
        class Square : public Shapes{
            public:
                float findArea(){
                    return h*w;
                }
        }

And there is no virtual constructor, only virtual destructor are present.

Local Classes : 
Generally classes are declared outside the function and at the top, they are 
called as Global classes. We can use this type of classes in any function.
But local is a class, which is declared and defined inside a function.
    i. A local class name can only be used locally i.e., inside the function and not outside it.
    ii. The methods of a local class must be defined inside it only.
    iii. A local class can have static functions but, not static data members.
    

Template or Generic : 
    Defining saveral functions with the same name by changing the 
number of or type of arguments are called as function overloading.
The only benifit of function overloading is function names are identical.
But the size of the programs are not reduced. Templates are used to
solve this issue.
    Template are of 2 types :
        i. Function Template
        ii. Class Template
        
    The advantages of Generic Programming are
        i. Code Reusability
        ii. Avoid Function Overloading
        iii. Once written it can be used for multiple times and cases.
    
    example : 
        template <typename T>
        T myMax(T x, T y){
            return (x > y) ? x : y;
        }

        int main(){
            cout << myMax(1, 5) << endl;
            cout << myMax(4.5, 8) << endl;
            return 0;
        }

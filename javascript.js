//------------------------------------------------------------------------------------
//                      PART - 1
//------------------------------------------------------------------------------------

/*
1. Explain js is dynamic language?
    The data types of the variable can change during the runtime.
    ex : let x = 10;
            x = "string";
            x = true;

2. How does js determines the data type?
    js determines the data type depending the value assigned during the runtime.

3. "typeOf" is used to determine the data type of a variable.

4. Different data types
    8 types : 
        1. Primitive data types
            i.   String
            ii.  Number
            iii. Null
            iv.  Undefined
            v.   Boolean
            vi.  Big int
            vii. Symbol
        2. Object data types
            i.   Object

5. Explaing Undefined data type
    It means variable has been declared but no value is assigned to it.

6. What is NULL?
    Its a data type, which indicates intentional absence of data.

7. Differentiate between NULL and Undefined
    Undefined : Variable has been declared but value has not been assigned.
    Null : Null indicates absence of data. It is neither empty nor zero.

8. Explain js hoisting.
    Its a mechanism where variable and function declaration are moved to the
    top of the scope, before the execution of the code.
    (Value will not be moved to the top. Undefined will be assinged to the varible)

9. Explain Global variables.
    Global variables are accessible to throughout the webpage or the document.
    Disadvantage : Hard to debug and its buggy.

10. What happens when we declare the variable without the "var" keyword?
    Variable becomes global variable. 

11. What is the use of "use strict" keyword?
    It checks if the variable is defined using the "var" keyword or "let" keyword.
    Otherwise it throws an error.

12. How to avoid global variable issues?
    i. We can put the global variables in a proper namespace
        ex : var myGlobal = {};
             myGlobal.firstvariable = "test";
             myGlobal.secondvariable = 0;

    ii. Using closure.
        ex : var myGlobal = (function(){
                var connectionString = "test";
                function GetConnection(){
                    return connectionString;
                }
                return {
                    GetConnection
                }
             })();
             var str = myGlobal.GetConenction();

13. What are Closures and Why do we need closure?
    Closures are stateful function. They are function inside the function.
    And it makes the normal function statefull.

    Ex : 
    // every time the function is called value will start from 0.
    function SimpleFunction(){
        var x = 0;
        console.log(x);
        x++;
    }
    SimpleFunction(); // 0;
    SimpleFunction(); // 0;

    // But in the case of Closure, we can hold the reference.
    function ClosureFunction(){
        var x = 0;
        function Increment(){
            console.log(x);
            x++;
        }
        return {
            Increment;
        }
            }
    var ref = ClosureFunction();
    ref.ClosureFunction(); // 0
    ref.ClosureFunction(); // 1
    ref.ClosureFunction(); // 2

    Use :
        1. To creates self cotained modules -> self contained state
           We can avoid global varaibles

        2. Data Abstraction
           Ex : 
            function ClosureFunction(){
                var x;

                function Increment(){}
                function GetXValue(){}
                function init(){}

                return {
                    Increment,
                    GetXValue
                }
            }

            var ref = ClosureFunction();
            ref.Increment(); // ok
            ref.GetXValue(); // ok
            ref.init(); // error

14. What is IIFE?
    - Immediately Invoked Function Expression.
    - Ananymous function
    - It gets called as soon as the function is declared.
        ex : (function(){
                //do something
             })();
    - Any kind of variable inside the function is local to the function.

15. What is the use of IIFE? What is the name collision in global scope?
    and Explain IIFE vs Normal Function.
    Name collision : 
            When we have the same varaible name or method name in the same context defined.
            ex : 
                var init = 0;
                init();
            explanation : At line number 1, it is declared as a number and 
                          At line number 2, it is using as a function. An error will be thrown.

    IIFE : To solve the name collision problem we can make use of the iffe.

    Difference between IIFE and Normal Function : 
        i. No name collission in IIFE. 

16. Explain the design patterns? Which is the most used designed pattern in js?
    i.  Singleton
    ii. Mediator pattern etc...

    Most used design patter in js : 
        Module Design Pattern or Module Revealing Pattern
        Reason :
            - It helps in creating self contained independent component.
            - Provides Encapsulation and Abstraction
        Explanation : 
            - It is a combination of IIFE and Closure
            - IIFE helps in creating logical namespaces, which further organises our code
              and makes it structured and organised.
            - Closure helps in inplementing good encapsulation. (what is to be shown and what is to be hidden)
    
        Ex : 
            var custNameSpace = (function(){
                function customer(){};
                function customerInvoice(){};
                function customerValidation(){};

                return {
                    customer,
                    customerInvoice 
                    // this is the reason we called it as 
                    //Module Revealing Patter. Here revealing the functions
                }
            })();

            var cust = new custNameSpace.customer(); // it will work
            var cust = new custNameSpace.customerValidation(); // it will throw an error

17. What are the different ways to create js object?
    There are 4 ways of creating js object :
        i.   Using literal
        ii.  Object.create(current object)
        iii. Constructor way / function way
        iv.  Using ES6 syntax : class name {}

18. How can we do Inheritance in javascript?
    What is prototype in javascript?
    Explain Prototype chaining?

    i. Inheritance in js is done by "Prototype" object. 
       This is object Inheritance unlike class inheritance in other languages.
       ex : 
            function employee(){}
            function manager(){
                this.Cabin = "";
                this.DoWork = function(){
                    alert("Manager team");
                }
            }
            var emp = new employee();
            manager.prototype = emp; // this means manager inherites from employee
            manager.prototype = new employee() // another way to inherit from employee to manager function

    ii. Prototype object works like a linkedlist, that means if the property is not 
        present in the current object, it will go up the prototype chain and so on.
        This is called Prototype Chaining.

19. Explain "let" keyword.
    It helps in creating block level scoped variables.

20. Are variables with the "let" keyword hoisted?
    "let" keywords are hoisted but will not be initialised with the default "undefined" value
    If we use the variable before the assigning the value, then it will throw an "ReferenceError".

21. Explain Temporal Dead Zone.
    - It is the period or the state of the variable, when the varaibles are named 
    in the memory but not declared and initialized with the value.
    - During this period if we try to access the value, we will get an "ReferenceError".

22. Whats the difference between declaring the variable with the "var" vs "let"?
    1. Scope : 
            var : Variable declared by the "var" keyword are scope to the immediate function body.
            let : Variable declared by the "let" keyword are scope to the immediate enclosing block.
    2. The way variables are initialized : 
            var : Value will be initialized with default "undefined".
            let : Value will not be initialized with any value.

23. Tricky Question around Concatenation
    var d = "10";
    var d1 = "10";
    console.log(d + d1) => 1010

    var i = 10;
    var i1 = 10;
    console.log(i + i1) => 20
    console.log(i + i1 + "4") => 204
*/





//------------------------------------------------------------------------------------
//                      PART - 2
//------------------------------------------------------------------------------------

/*
1. Data Types of the variable can change during the runtime. Thats why we call it as Dynamic Programming.
2. Data Types in JS
	Primitive
	i. string
	ii. number
	iii. null
	iv. undefined
	v. bool
	vi. big
	vii. symbol

	Non-Primitive
	i. Object

3. What is undefined?
	A variable has been declared, but havent assigned any value.
4. Null is an intensional absence of data.
5. Java Script Hoisting
	It is mechanism, where variable and function declaration are 
	move to the top of the scope before the code executes.
	
6. Global variables : Which is accessilbe throughout the page. 
			    It can make code very hard to debug.
7. What if we declare a varialbe without the "var" keyword?
	Variable becomes Golbal.
8. What is the use of "use strict" keyword?
	It checks if the variable is defined using the var keyword or 
	let keyword. It throws if not.
9. How to Global variable in the project?
	We cannot avoid Global variable, we can avoid Global variables.
	i. We can put GV in a proper common namespace.
		ex: var global = {};
		    global.one = ...
		    global.tow = ...
	ii. Create a closure and apply module pattern
		
10. What is Closure?
	Closures are statefull function. Its a function inside a function.
	And it makes normal function stateful.
	ex: 
	function SimpleFunction(){
		var x = 0;
		x++;
	}
	function ClosureFunction(){
		var x = 0;
		function Increment(){
			x++;
		}
		function GetValue(){
			return x;
		}
		function init(){

		}
		init();
		return {
			Increment,
			GetValue
		}
	}

	SimpleFunction();
	SimpleFunction();
	// in both of the above cases value of the x = 1;
	// because it doesnt remeber the state of the x;

	var ref = ClosureFunction(); // holding the reference
	ref.Increment(); // x = 1
	ref.Increment(); // x = 2

11. What is the need of Closure?
	The only goal of closure is to Create	
		i. self contained functions
		ii. self contained code
		iii. self contained module.
	And when we create self contained, we have self contained state,
	this means it helps us to avoid global varibles.
	And also it helps in exposing what we want to expose.(abstraction)

12. What is IIFE?
	IIFE : Immediately Invoked Function Expression
	Its an anonymous function.
	ex:
		(function(){

		})();
13. What is the use of IIFE, What is name collision in global scope
	and IIFE vs Normal Function?
	
	i. Name Collision: It happens when we name the same function/
	variable name to more the one function/variable in the same
	context.

	ii. Use of IIFE : To avoid name collision.

14. What are design patterns?
	Design patterns are time tested architecture.
		i. Singleton pattern.
		ii. module design pattern(populare one):
			IIFE + Closure
			better code management because of IIFE and
			better encapsulation because of Closure

15. Ways of create a js object.
	i. Literal
		ex: var pat = {"a":"", "b":""};
			pat.Admit = function(){}
	
	ii. Object.create
		ex:	var patnew = Object.create(pat);
			patnew.age = 10;

	iii. Constructor Way
		ex:	function Patient(){
			this.name = "",
			this.address = "",
			ths.Admit = function(){}
		}

		var pat1 = new Patient();

	iv. ES6 Classes
		class PatientClass{
			constructor(name, address){
				this.name="",
				this.address=""
			}
		}
		var p = new PatientClass();

16. How to do Inheritance? What is prototype object?
	Explain prototype chaining.
	
	Inheritance in js is done by prototype object.
	we have object inheritance and not class inheritance 
	and happens through prototype object

	ex:
		function Employee(){
			this.name="",
			this.DoWork=function(){},
			this.attendence=function(){}
		}
		function Manager(){
			this.Cabin="",
			this.DoWork=function(){}
		}

		var emp = new Employee();
		Manager.prototype = emp // it means manager is a child of employee

		var man = new Manager();
		man.Name = "Shiv";
		man.attendence();
		man.DoWork();

	Every JS object has a prototype object.
	Prototype Object works like a linkedlist, thats why
	its called as Prototype Chaining.

17. Explain let keyword.
	It helps in creating block level scopped variable.

18. Var will be hoisted and initialized with the value "undefined".
	Let will be hoisted, but will not be assigned with any value.

19. Temporal Dead Zone.
	It is the period between when the variable is named in the 
	memory but not declared and initialized with the value
	and the initialization.

20. 
	var d = "10"
	var d1 = "10"
	console.log(d+d1) // 1010

	var i = 10;
	var i1 = 10;
	console.log(i+i1) // 20

	console.log(1+1+"4") // 24


---------------------------------
Namaste JS

1. Everything in JS executes inside the Execution context.
	Memory Component : variable and function will store in key value pair.
	This is also called as "Variable Environment"

	Code Component : Code will executes one line at a time.
	This is also known as "thread of execution"

2. JS is single synchronous threaded language:
	i. It means it can executes only one line at a time.
	ii. and it can go to the next line only when the completion of 
	current line

3. Lexical Environment: if the value is not present in the scope,
	it goes outside of the function find the value of the variable.

4. Function statement/declaration:
	function a(){};

   Function Expression:
	var a = function(){};

	Diff: Hoisting

5. Sending / recieving a function as a value is called as first class function.

6. Event loop, callstack, callback queue and micro

7. Higher order function : Function which takes the function as a parameter.

*/
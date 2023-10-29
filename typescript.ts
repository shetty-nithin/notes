/*
Benefits:
    * Static Typing
    * Code Completion
    * Refactoring
    * Shorthand Notation
Drawbacks:
    * Compilation: Browser doesn't understand the .ts code.
                   .ts ---> compiler ---> .js (transpilation)
    * Discipline in coding

Installation:
    * npm i -g typescript (prefix with sudo if MacOS/Linux)

How to configure:
    * tsc --init
    * "rootDir": "./src"  => where .ts code present
    * "outDir": "./dist" => where .js files present
    * "removeComments": true => generated .js will not be having the comments from .ts code
    * "noEmitOnError": true => if there is an error in the .ts code, .js will not be generated

Type checking configuration:
    * "noImplicitAny": true (not recomended)
    * "noUnusedParameters": true
    * "noImplicitReturns": true
    * "noUnusedLocals": true
    *  "strictNullChecks": true (already "strict" is used. So no need of this)

To run:
    * tsc "filename" (without the tsconfig.json file)
    * tsc (with the tsconfig.json file)

To debug:
    * make changes in the tsconfig.json file
        - "sourceMap": true

    * Go to debug panel -> create launch.json file -> select node.js
    * launch.json file, add the below
        - "preLaunchTask": "tsc: build - tsconfig.json", just after the below line
        "program": "${workspaceFolder}/src/index.ts",
    * Place a break point and click on Launch Program.

Data Types:
    * Built-in
        - any
        - unknown
        - never
        - enum
        - tuple
*/

// Syntaxes with example:
//1
    let x1: number = 1;
//2 
    let x2: [number, string] = [1, "nithin"]; 
//3 
    enum Size {Small = 1, Medium, Large};
    let mySize: Size = Size.Medium;
//4
    function calculateTax(income: number, taxYear?: number, interest = 12): number{
        if(taxYear < 2022){
            return income*1.2;
        }
        return income*1.3;
    }
    calculateTax(1200);
//5
    let employee: {
        readonly id: number,
        name: string,
        retire: (date : Date) => void
    } = {
            id: 1,
            name: "Nithin",
            retire: (date: Date) => {
                console.log(date);
            }
        };
    
//6
    type Employee = {
        readonly id: number,
        name: string,
        retire: (date : Date) => void
    }
    let employee2: Employee = {
            id: 1,
            name: "Nithin",
            retire: (date: Date) => {
                console.log(date);
            }
        };

//7: Union Types
    function kgToLbs(weight: number | string){
        //Narrowing
        if(typeof(weight) === 'number'){
            return weight*2.2;
        }
        else {
            return parseInt(weight)*2.2;
        }
    }    

    kgToLbs(10);
    kgToLbs('10');

//8
    type Draggable = {
        drag: () => void
    };

    type Resizable = {
        resize: () => void
    };

    type UIWidget = Draggable & Resizable;
    let txtBox: UIWidget = {
        drag: () => {},
        resize: () => {},
    }

//9: literal (exact specifi)
    let quantity: 50|100 = 100;

//10
    type Quantity = 50|100;
    let quantity2: Quantity = 50;

//11: Nullable
    function greet(name: string | null){
        if(name){
            console.log(name.toUpperCase());
        }
    }
    greet(null);

//12
    type Customer = {
        birthday: Date
    };

    function getCustomer(id: number): Customer | null {
        return id === 0 ? null : {birthday: new Date()};
    }

    let customer = getCustomer(0);
    if(customer){
        console.log(customer.birthday);
    }
    // or we can use the "Optional Property Access Operator"
    console.log(customer?.birthday);



/* --------Converting JS to TS -----------------

1. Change the file name from .js to .ts
2. run "tsc --init" to create a tsconfig.json file
3. Set strict to false for now.
4. Run "tsc"
5. Change the outDir to different folder such as "dist"
6. Set strict to true
7. Run "tsc"
8. Change the syntax from 
    const express = require("express");
    to
    import express from "express";
9. Chnage the syntax from
    module.exports = routes
    to
    export default router

    or

    module.exports = {};
    to
    export default {};

    or make it
    export const User = () => {}


10. import {Request, Response, NextFunction}
    (req, res, next) to (req: Request, res: Response, next:NextFuntion)

11. While passing the data from middleware to next function, we usually append the data
    to the req object as "req.userId = user.id";
    This throws an error, because the type of the req will no longer be "Request".

    Solution 1: we can create a new function which extends the properties from "Request"
    interface UpdatedRequest extends Request {
        userId: string
    }

    Solution 2: req.headers["userId"] = user.id;

Converting to TS from react.js is little difficult. We can make use of Vite bootstrap

*/

/* ----- Mono Repos



*/

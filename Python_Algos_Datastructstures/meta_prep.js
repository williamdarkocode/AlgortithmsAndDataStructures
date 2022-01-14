/*
    - What does apply function do
    - Given 2 dom treems check if node in A is also in B
    - what does call function do
    - diff between call function and apply function
    - diff between map and forEach
    - what is 'this' keyword
    - what is closure
    - var vs const vs let
        - var statement declares function-scoped or globally scoped variables

    - DOM tree
    - write emitter class
    - object prototypes
    - es6 promises
    - es6 maps vs objects
    - es6 sets over arrays
    - function that deeply flattens array
*/

/*
    * Diff between forEach and map
        - forEach and map both iterate over iterables, but map returns a new iterable/array with the results, while forEach does
        any changes in place. Also map does not execute the provided funtion on array elements without values.

    * Promise
        - Promises are objects that represent the eventual completion or failure of an asynchronous operation
        - Promises are essentially returned objects to which you attach callbacks instead of passing callbacks into a function
        - A promise is a PROXY for a value not necessarily known when the promise is created. It allows you to associate handlers with 
        async actions' eventual success value or failure reason. Allows async methods return values as if they were synchronous methods
        - Async method returns promise to supply the value at some point in the future
        - A Promise is in one of these states:
            pending: initial state, neither fulfilled nor rejected.
            fulfilled: meaning that the operation was completed successfully.
            rejected: meaning that the operation failed.


    * Closures
        - Allows for nesting functions, ie defining one function inside the scope of another. The nested functions are granted
        access to all the data inside the enclosing function, and all the data the enclosing function has access to.
        - Enclosing outer functions do not have access to the data inside the nested functions. Provides an encapsulation of the variables
        in the innter function

    * Hoisting
        -  A variable can appear to be used before its declared. Variables are processed before any code is executed:
            eg: x = 2;
                var x;
            is the same as:
                var x;
                x = 2;
        - function declarations can be hoisted, but only when declared with traditional function syntax, not variable function syntax.
            eg: foo();
                function foo() { console.log('foo'); } is a legal statement

    * Var
        - var statement declares gloablly scoped or function scoped variables
        - var declarations are processed before any code is executed (Hoisting), initial value is therefore undefined
        - scope of var declared variable is its current execution context. If its in a function, then its scope is function closure and
        functions declared in that function. If its defined outside closure, it's a global variable
        - Duplicate variable declarations with var will not tirgger error
        - can be accessed with this key word as they'll be part of global object
    
    * Let
        - variables declared or with let are block scoped
        - variables declared with let are only initialised to their values ones parser evaluates it

    * Const
        - variables declared or initialised with const are also block scoped
        - variables declared with const are read only thus cannot be reassigned
        - const on objects and arrays
            const arr = [2,3,4];
            arr = [1,2,3] is illegal. would return error
            arr.push(5) is a legal statement and won't return error

            const obj = {'name': 'william'}
            obj = {'name': 'fosher'} is illegal statement and will return error
            obj['name'] = 'max' is not illegal and would not return error

    * For in
        - For in loops are used to iterate over keys/properties of an object
    
    * For of
        - For of loops are used to iterate over iterables like arrays, maps, sets. For each element of the array.

    * Map
        - Map object is simple key/value map and its elements can be iterated over in order of insertion using for of loop
        eg: let myMap = new Map();
            myMap.set('name': 'fosher');
            myMap.get('name') ---> returns 'fosher'
            myMap.has('name') ---> returns True
            myMap.size() ---> returns 1 (the number of key/value pairs)
            myMap.delete('name') ---> deletes name key and corresponding value
            myMap.add('thisgy', 'fucks')
            mayMap.clear() ---> clears/deletes all values from the map

        - Using Map vs js object literal:
            - In object literals, keys can only be strings or symbols, but iwth Maps they can be anything (numbers, etc)
            - You can get the size of Map easily using size() function. But with object literal you need to keep track of object
            size manually
            - iteration of Maps is in order of insertion
            - Object literals have prototypes so they have default keys

    * Object prototypes
        - an object used as a template from which to get the initial properties for a new object.
        - any object can be associated as the prototype for another object, allowing the second obj to share the first's properties
        - all objs can inherit from another object (they aren't distinct entities)
        
        function Employee() {
            this.name = '';
            this.dept = 'general';
        }

        function Manager() {
            Employee.call(this);
            this.reports = [];
        }
        Manager.prototype = Object.create(Employee.prototype);
        Manager.prototype.constructor = Manager;

        function WorkerBee() {
            Employee.call(this);
            this.projects = [];
        }
        WorkerBee.prototype = Object.create(Employee.prototype);
        WorkerBee.prototype.constructor = WorkerBee;

    * Apply function
        - apply() calls function with given 'this' value, and arguments provided as array or array like object
        - Some uses:
            const array = ['a', 'b'];
            const elements = [0, 1, 2];
            array.push.apply(array, elements);
            console.info(array);

    * Call function
        - call() method calls a function with a given this value and arguments provided individually.
        - Some uses:
            - chaining constructors for an object
                function Product(name, price) {
                    this.name = name;
                    this.price = price;
                }

                function Food(name, price) {
                    Product.call(this, name, price); // ===> Food objects will now also be initialise Product object properties like name. 
                    this.category = 'food';
                }

                function Toy(name, price) {
                    Product.call(this, name, price);
                    this.category = 'toy';
                }
            
            - invoking functions by specifying context for 'this':
                function greet() {
                    const reply = [this.animal, 'typically sleep between', this.sleepDuration].join(' ');
                    console.log(reply);
                }

                const obj = {
                    animal: 'cats', sleepDuration: '12 and 16 hours'
                };

                greet.call(obj);  // cats typically sleep between 12 and 16 hours



*/  
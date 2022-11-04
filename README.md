# Python Data 8INF957

# Introduction
This project contains multiple python file explaining different OOP concepts. It also contains a file showing some simple feature of data analysis using the Pandas Module.


# Polymorphism
In this file, the concept of polymorphism is explored. It Contains a Person class, as well as a Teacher and Student Classes. this file also explore the method overloading/overriding.

## Polymorphism : Person Class
We show the concept by Creating a Person class containing basic information such as name, age and gender. We then create two subclasses : Teacher and Student. They both contains an ID

## Method overloading
This concept doesn't really exist in Python. To show it, we created a callme function, that takes any number of variables. We then make it do different things depending on the the type of the first variable given.

The closest we could get to actual overloading is using the typing module to add more function definitions using the @overload decorator. Sadly it is only a decorator, and you will still have only one actual implementation of the function, that needs to check for the type of the variables.

## Method overriding
This is a concept that is very similar to method overloading. We simply create a function in the parent class, and then override it in the child class. This is done by simply creating a function with the same name in the child class. In our exemple, it is achieved by the \_\_str\_\_ function that is overriden in the Teacher and Student classes, to add their ID to the string. This allow the main function to call the overriden function, when it is called on a Teacher or Student object.


# Generic
In this file, we explore the concept of generic. Once more, this isn't a concept that really exist in Python.

To work around that, we use the typing module use another concept called type hinting. This allows us to specify the type of the variables in a function, and then use it to check In the IDE if the type of the variable is correct. This can be done using TypeVar, as shown in the example file. This example uses this with two different ways, to have a Stack that is only supposed to contain Integers. In the IDE we tested it (IntelliJ), it would show an error/warning on the line if we tried to add a string to the stack.

# Modularity
In this file, we explore the concept of modularity. We create a file called "FiboModule.py" that contains a function that returns the nth number of the Fibonacci sequence. We then import this file in the "Modularity.py" file, and use the function after importing it. This shows how simply we can import modules in Python.

There is also another exemple with the "AddingModule.py" file, that shows other way to import modules to a file.

# Data Analysis
In this file, we use Python do make some simple data analysis. We used the Pandas module to work on a dataset (given in the TP) that contains informations about some Person. We then use the module to import our data into pandas's DataFrame, and then use it to do some simple analysis, such as only keeping the data of people that have "4" as their label.
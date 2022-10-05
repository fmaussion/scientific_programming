# Syllabus

German: *Lehrveranstaltungskonzept*. Please read it carefully at the beginning of the class, and return to it as often as necessary.


## Learning outcomes

This class aims at teaching **modern programming techniques** for (geo-)scientists. After completing the class, you will:
- be familiar with a modern and open-source programming language (Python) and its use for scientific applications
- be able to program in a structured, extendable and reproducible manner
- be able to read and write python programs of intermediate complexity, as well as python packages
- understand how numbers are handled by computers and be aware of numerical accuracy errors 
- be aware of simple performance considerations (vectorization)
- know how to write and run formal tests for your code (with pytest)
- be acquainted with various programming utility tools: IDEs, debugger
- be able to search for, understand, install and take advantage of existing packages and libraries available in the rich scientific Python ecosystem


```{admonition} Non-objectives of this class:

This class is not about learning data analysis, plotting or numerics. 
Nor is it about learning the details of the python packages you will 
use for the rest of your studies such as matplotlib, pandas, xarray, etc. 

My objective here is to provide you with a **solid foundational knowledge about core programming concepts**,
in order to to make of you an **independent learner**, 
able to expand and deepen your programming skills by yourself.

Don't worry: you will have ample time to play with fancy libraries in the other classes of the master curriculum.
```

## Prerequisites

The targeted audience for this lecture are **students at the master level with previous experience in programming**. No prior knowledge of python is required, but I'll assume that you are familiar with a similar language (Matlab, IDL, R...) and basic programming structures (loops, functions, conditional blocks...). 

Ideally you will have the programming level of a student having completed [my intro to programming class](https://fabienmaussion.info/intro_to_programming) in the BSc.
The first few weeks we will be catching up on the materials from the bachelor class, but quickly enough we will move towards more advanced topics.

## Organisation of the class

The class is taught in English. It is okay to ask questions in German as well!

This class follows the [flipped classroom](https://en.wikipedia.org/wiki/Flipped_classroom) model. You will acquire new knowledge at home by reading online materials (and watching videos when appropriate). We will then use the time together in class to discuss the materials and write code.

The semester is 15 weeks long. **Each week will always be organised as such**:
- On Fridays, you will receive instructions for the week to come (which materials to read/watch, and one homework assignment). You study them at home during the week.
- On Mondays (11:00-11:54), we meet to discuss the assignment solutions from the previous week (assignments are mandatory but not graded, see "Grading" below)
- On Tuesdays (10:15-11:45), we meet in class. We will start the hour with a short, individual online assessment, for you to check if you understood the new materials correctly. Based on your own assessment, you pick the topics and questions you would like to discuss in class. We work on the assignments together.
- On Fridays: start again!

During the semester, you can work either on your own computer (laptop) or on the working stations in the computer room.

```{important}
The class grants you 5 ECTS if successfully passed: in theory, this represents 8 to 10 hours work per week (not including holidays). For this course, it means that you will spend at least twice as much time doing homework than sitting in class.

I strongly recommend to work regularly for the class. Programming is quite different to other disciplines, and "doing nothing for a few months" cannot be replaced by a "no-sleep-48-hours-push" at the end of semester. Programming is a bit like learning how to ski or climb: it is best learned by doing, and you will notice that regular practice will make you better each week.
```

## Learning checklist

At the end of each lesson, there is a "learning checklist": go over it at the end of the lecture and see i you can check all the boxes. It's a good way for you to check if you are ready to go on, or if you still need to go back to some reading and learning!

## Grading 


Combined: mid-term exam (20%), end-term exam (50%), participation to practicals (0%), programming project (30%). A positive evaluation of the sum of both exams, the practicals and the project is necessary to pass the class.

1. The mid-term exam (open-book exam, 0H45, combinaison of muliple choice, essay and programming type of questions) will take place on **Tuesday 22.11.2022** from 10:15 to 11:00.
2. The end-term exam (open-book exam, 1H30, combinaison of muliple choice, essay and programming type of questions) will take place on **Tuesday 07.02.2023** from 10:15 to 12:00.
3. The practicals take place every other Monday. Participation and one group presentation (non graded) is required to pass the class.
4. The projects start in November (date pending) and will have to be returned before the Christmas holidays.

A positive evaluation of each of these elements is mandatory to pass the class!

**Weekly assignments**

Each week there will be an **assignment** (unless specified otherwise, e.g. during the group projects). These assignments can be worked through alone or in groups. Each week, I will ask **one volunteer group** to present their results to the rest of the class on the following week.

**Programming project**

In the middle of the semester, you will be given a programming project to realize over several weeks. Ideally, it will be a project that raises your interest. The grading will be explained once the project starts, but will be combined between an individual contribution (50%) within a group project (50%).

**Bonus points**

There will be bonus points for anyone pointing me to typos / mistakes / broken links / incomprehensible or difficult passages in the lecture notes. [Send me an email](https://fabienmaussion.infointro) or [open an issue](https://github.com/fmaussion/intro_to_programming/issues) on GitHub!

## Weekly lesson plan 

You will notice that there are 12 weekly units for a 15 weeks long semester: this is expected since (i) some weeks contain holidays, and (ii) I expect some changes to the schedule. 

- Week 01 - Terminal & Python primer 
    - Welcome! Motivation & syllabus
    - Installing python & Getting started with the command line
    - For python newcomers: some reading to do
- Week 02 - Python language fundamentals
    - Language fundamentals
- Week 03 - Variables scopes, modules, strings, good practices
    - Modules, import mechanism, namespaces, scope(s)
    - String formatting and file paths
    - Good practices, programming style and conventions
- Week 04 - Floating point arithmetics, Numpy basics
    - Introduction to numpy: why does numpy exist?
    - Number representation in computers
- Week 05 - Scientific Python
    - Arrays in numpy: indexing, ufuncs, broadcasting
    - The scientific python stack
- Week 06 - Revisions

**Mid-term exam**

- Week 07 - Testing
    - Errors, Exceptions and Warnings
    - Testing your code
- Week 08 - Python Packages and ClimVis project
    - Structure of a python package
    - Term project: the ClimVis package
- Week 09 - Code documentation
    - Documenting your code
- Week 10 - Object Oriented Programming I
    - Object Oriented Programming: introduction
- Week 11 - Object Oriented Programming II
    - Object Oriented Programming: inheritance
- Week 12 - Object Oriented Programming III
    - Object Oriented Programming: why?
- Week 13 - Data workflow
    - The scientific data analysis workflow

**End-term exam**

## Previous lectures

Here is a link to last year's lecture notes if you are curious: https://fabienmaussion.info/scipro_ws2021

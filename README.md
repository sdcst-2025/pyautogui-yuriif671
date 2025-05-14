## SDSS Computing Studies Python Assignment
### Assignment 030 Automation - Working with Time

Objectives:
* Use the time module to introduce delays in your program
* use the time.time() command to help keep track of elapsed time

Automation is becoming a huge deal, with robots replacing people doing menial tasks every day.  Robots can be quite sophisticated, and are often able to mimic the roles that humans once filled.

Today, we will be exploring the creation of a robot to play a simple game. The simplest games are clicker games, although some of these can become quite complicated.  In fact, a program can not only beat these games, but solve more open ended games that might not appear to be simple on the surface.

To create a robot to play the game, you really need to understand the sequences required to play the game.  There may be multiple screens; how do you navigate between them?  There may be times that your bot becomes out of sync. How do you detect problems and then have them fix themselves automatically?  These are questions that we will need to address when we create our robots.

We will also be making use of 2 built in modules and 1 installed module. Some of these modules have their oown dependencies that we will need to install manually

random
time
pyautogui
pillow (a pyautogui dependency)
opencv-python (a pyaugotui dependency)

Modules that are installed and required for a project are called **dependencies**. Often a project may have many, many dependencies.  This can impose a security risk if the developer is not trusted.

Pay close attention to today's example files, as they will be very important in understanding how the code structures work.

Pyautogui is a module written for python that incorporates a number of different tools together in one package.  We will be using it for automating tasks by looking for graphical elements on screen and then deciding what to do with them

A great source for finding the pyautogui documentation is https://pyautogui.readthedocs.io/en/latest/
This documentation page will help you install the module.

#### Import time commands ####
example0:
see how we can use the time() and sleep() methods in the time module


##### Task 0: Planning sequences of Events
Write down the sequence of events or actions that you will need to program
into your game.  You may want to check pauses if your game needs to wait
for actions to complete. You will be submitting this document as part of
your assessment.

##### Task 1: What does it do?
Open up the example0.py and example1.py
In your own words, explain what is happening in each program.  You can refer to
the line numbers in the files to help you reference parts of the program.

##### Task 2: Working with Time
Task 2
Basic Assignment:
Create a program to display 10 characters on screen, one at a time,
to the user.  They have to press that key to advance to the next character.
Tell the user how long it took them to press all 10 characters.

Alternately, you can select a random word from a list of words that you provide.
Have the user type in the word before the next word is selected.  This version
is easier because you can use the existing input() command that you are more
familiar with.

Your assignment should make appropriate use of functions to break the
code up into more manageable sections.  

Your assignment will be graded on the following criteria:

functionality (does it work the way it is intended)
modularity (is it broken up into functions to make your main block momre readable)
appropriate use of return values and input parameters

#### Task 3: Install pyautogui ####
Install modules directly to your user account.
This is often not the best approach as it installs the module globally to your computer rather than to a specific project. If you were a developer, you might install specific modules for specific projects to help you keep track of the dependences.
We will use the commands
```
py -m pip install <module_name> --user

or

pip install <module_name>
```
Install the following modules:
pyautogui
opencv-python
pillow

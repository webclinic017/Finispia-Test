# Finispia-Test
Getting started with Robot Framework
1.Install python version Python 2.7.16 from https://www.python.org/downloads/ (check version with python –version command)
2. Set Python in environment variables
3. Install robot framework with pip install robotframework command
4.Check version with robot –version command It should be Robot Framework 3.1.2
5. Download and install wxPython (wrapper) from https://sourceforge.net/projects/wxpython/files/wxPython/2.8.12.1/  click on  wxPython2.8-win64-unicode-2.8.12.1-py27.exe
6. Check the installation with pip freeze command wxPython==4.0.6 should be there
7. Install RIDE with pip install robotframework-ride command
8. Python libraries to install with pip install command:

selenium==3.141.0
robotframework-selenium2library==3.0.0
9.Install web drivers (chrome, firefox, …..) from here https://www.seleniumhq.org/download/
10. Add the path of the webdriver in environment variables

How to run the tests:
1.	Cd the project folder
2.	Run the command robot SuiteName.robot
3.	The command line option –report can change the report directory and name
How to run all the test suites:
1.	Run the command robot NameOfFolderThatContainsAllTestSuit

Important:
Before starting the tests : 1.browser  2.credentials  3.Url  variables should be checked. 
To change those variables open all the .robot files (all the test suites) in a text editor and simply change the variable

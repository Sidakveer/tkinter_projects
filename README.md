# tkinter_projects
This repository consists of projects made using **GUI tkinter** from the python in-built library and **pandas library** to manage data files.

## Miles_to_km
This is a simple project which displays a miles to km converter. The user inputs the value in miles and clicks on the calculate button, the program then 
calculates and returns the value in kilometres.

## pomodoro_timer
This is a basic timer we have build which follows a pomodoro technique which is a time management method developed by Francesco Cirillo in the late 1980s. 
It uses a timer to break work into intervals, in our program the work length is 25 minutes, separated by short breaks of 5 minutes each and after every 4 
work iterations the timer displays a long break of 20 minutes. The timer starts or resets depending on which of the buttons diplayed are pressed.

## password_manager
In this project we have build a password manager GUI which displays a small screen and asks for the user_input of the name of the website, email/username and the password they want to set. Apart from setting the password the program can generate a random password to be used by the user by clicking the generate password button which also copies the same password to the clipboard using the **pyperclip external module** and finally the user can click on add to save the information entered to a text file. Before the info gets appended to the .txt file the program gives a pop up **using the messagebox module of tkinter** to confirm the entry and proceeds accordingly.

## Flash_cards
The falsh card project is a fun graphical user interface which displays a card for the user to learn different french words. Each card automatically flips  
after 3 seconds and shows the translation in english of the respective word. There are two buttons for the user to click which tell the program whether the user knows the displayed french word or not if yes the word is removed from the list of words and is not displayed in the next iterations as the user has 
already memorised that word.

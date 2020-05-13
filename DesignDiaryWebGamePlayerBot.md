# Design Diary - Web-game Player Bot

My initial idea for my final project was to create a pygame car-racing game, but after more research and consideration
I decided that would be redundant. Instead of the game, I decided to pursue a different idea from earlier in the
semester: a bot that can play a web game, Webkinz, for my girlfriend. Since the primary focus of the game was on 
automating daily-reinforcement tasks to gain rewards, I was just intending to make it go through the various 
"wheels of chance" within the game which each get one free use-it-or-lose-it spin allocated daily to the user. The bot
would be able to redeem her free daily spins on the days she is swamped with school. I ended up achieving this goal
along with the goal of playing a game within Webkinz, Wacky Zingos Extreme, to earn money.

The first step was getting familiar with selenium, chromium, and pywin32; for reference I used these links:
*![Automate TINDER with Python tutorial](https://www.youtube.com/watch?v=lvFAuUcowT4)
*![Advanced Python Programming: Browser Automation with Selenium]( https://www.youtube.com/watch?v=GJjMjB3rkJM)
*![How to Build a Python Bot That Can Play Web Games](https://code.tutsplus.com/tutorials/how-to-build-a-python-bot-that-can-play-web-games--active-11117)

My first hurdle was enabling flash in the Chrome browser. This proved to be difficult because I was unable to find
a way to enable flash via Chromium args, so I decided to kluge it together. I decided to have the webdriver 
go to the Chrome settings page and switch the settings to enable Flash. This took a few hours by itself. I thought
it would be easy at first, but I found issues in my logic when I could not get the correct page/form option element
to switch to enable. This ended up being due to the option element being nested within several shadow-roots. I have
never heard of shadow roots until now, but I was able to get my code working by going-to and expanding each shadow
root until the parent root of the desired option, then I was able to directly identify the desired option element.

After this hurdle, I was able to easily log in to Webkinz, switch webpages, and proceed with the automation on the
Flash animation portion of the script. From this point forward, my script uses pywin32 and PIL to automate the
mouse clicks at the correct time at the correct coordinates on the screen for a given situation. It is hard-coded
in a way that it does not recognize the state of the menu screens. I just blindly assumes alerts/dialogs are open,
attempts to close them, and proceeds without closed-loop feedback. It uses this style of automation for the daily
activities (chance wheels to spin). 

Once the dailies are completed, the script proceeds to navigate to the Wacky Zingos Extreme game where it then uses
 a closed-loop feedback control structure for playing each of the five hits/at-bats for each game and then restarting
 the game to play again. After each at-bat, there is a game-generated swing-again alert which appears to have pseudo-
random placement on the screen within a range of coordinates. I was able to take multiple screenshots of these alert
 states and record the coordinates of these alerts. I took these coordinates and found a good range of screen coordinates
to click on in an attempt at closing the alert to proceed to the next at-bat. I was able make this closed-loop by having the
bot capture a segement of screen in the ready-to-swing state and compare this to whatever that same screen segment after each
click within the range of coordinates to determine whether the state changed to ready-to-swing after each click. If it
determines it has reset to the ready-to-swing state, the bot then proceeds to run the same loop again. This continues 
5 times and on the final state, it closes the end-game alert/dialog using similar rudimentary image recognition.

While creating the above bot and speeding up its execution, I noticed it was becoming more difficult to kill the program
since the bot took control of the mouse and focus for an infinite loop during Wacky Zingos Extreme. I tried a few different
things and realized that the only way to kill the bot like I desired was to have a separate thread listening for the ESC key.
This was the first time I learned about implementing threads, so it took me a while to research and develop my code to work
properly. It now runs one thread listening for the ESC and when triggered, executes os._exit() to kill the main thread (bot) from
a post-fork thread (key-listener) (I think that my understanding of how this works is correct since os.exit() didn't work properly).  
This took several more hours to figure out. I may want to add some other key-listening functionality like being able to pause/resume 
the bot's actions.

My last step is to create .exe files from this code for my girlfriend and her mom to run on their Windows 10 laptops without Python.

I easily spent 20-30 hours on this project and it was my favorite project of this semester. I am going to continue working on it
over the summer.

![WebgamePlayerBotDemo](https://github.com/rja45/Web-Game-Player-Bot---Python/blob/master/WebkinzBotDemo5.gif)






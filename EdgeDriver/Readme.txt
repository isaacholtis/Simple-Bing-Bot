This is the file that is used by selenium to interface with the browser. Selenium is better than webbrowser, as webbrowser just opens the link in your default webbrowser,
but selenium directly controls the browser. 
You need to add the msedgedriver.exe file to PATH in windows, to do that just search up a guide and you'll see how. That way you don't need to specify the exact path for 
that file in the code. 
The chrome driver thats in this folder is non-functional as far as I'm aware, because it is for chrome 8x, not chrome 98. The driver used has to be the same version number as 
whatever browser you want to use. In our code, we either need to detect what browser is the defualt for the system and use that, or just have the user install chrome, or msedge, or 
firefox, depending on what we want, and what is easiest to code for. 
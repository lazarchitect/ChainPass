ChainPass is a program that allows you to save your passwords and easily retrieve them. 
Once retrieved, the password is saved to your clipboard for easy pasting. You have 30 seconds to do so.

Here's how it works:
When you run app.py, you can choose add mode to create a new username/password combo.
Then, on subsequent runs, you can simply enter the username to retrieve the password.
There is also a delete mode, which, given a username, deletes the combo.
Finally, there is a special print mode which prints all the usernames and passwords to the console.

The Nitty Gritty:
next to app.py there is a database file called pw.txt.
For any function, the app opens the text file, which is in the format of a Python Dict, and reads it as such.
Keys are usernames, passwords are values.
The app uses the tkinter module to save text to the clipboard and the time module for time and sleep functionality.

Notes:
DO. NOT. EVER. SHARE OR UPLOAD YOUR PW.TXT. It contains your passwords in plaintext. 
This app is not designed to go on a server, network, shared computer, or anything else where someone besides you can see it.
This is simply a helpful script for home personal use. I am not liable for any misuse.

Fun stuff:
For easy use, create a shortcut file (simple .lnk file created with windows context menu) and name it something memorable (like ChainPass!)
I called mine Password Manager.
The reason for this is that you can now hit the Windows Key and type that name to quickly run the app wherever you are.
The whole point is ease of use.


print("What account?")
print("(Type \"add\" to create a new account/password entry or \"delete\" to remove one.)")
x = input(">> ")

if x == "print":
	with open("pw.txt", "r") as reader:
		fil = reader.read()
		fil = eval(fil)
		for i in fil:
			print ("\t", i, ":", fil[i])

elif x == "delete":
	name = input("What account to delete?\n>> ")
	fil = "bubbl21"
	
	with open("pw.txt", "r") as reader:
		fil = reader.read()
		# print("fil is", fil)
		fil = eval(fil)
		del fil[name]

	with open("pw.txt", "w") as writer:
		# print("writing", fil)
		writer.write(str(fil))

elif x == "add":
	
	name = input("What account to add?\n>> ")
	pw = input("Type the password:\n>> ")
	
	fil = "bubbl21"
	
	with open("pw.txt", "r") as reader:
		fil = reader.read()
		# print("fil is", fil)
		fil = eval(fil)
		fil[name] = pw

	with open("pw.txt", "w") as writer:
		# print("writing", fil)
		writer.write(str(fil))

else:
	from time import time, sleep
	f = open("pw.txt", "r").read() #f is a dict
	try:
		print("Password:", eval(f)[x])
		import tkinter
		r = tkinter.Tk()
		r.withdraw()
		r.clipboard_clear()
		r.clipboard_append(eval(f)[x])
		r.update() # now it stays on the clipboard after the window is closed
		# print(r.clipboard_get())
		print("copied to clipboard. You have 30 seconds.")
		start = time()
		while True:
			r.update_idletasks()
			r.update()
			if time() - start > 30:
				r.destroy()
				exit()


	except KeyError:

		print("No such account.")
		sleep(3)
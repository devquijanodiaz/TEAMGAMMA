import json
name = input("What's your name? ")
print("Hello " + name + ".")	
age = input("How old are you? ")
print(name + " is " + str(age) + " years old.")

# 'python3 -m pdb <filename.py>' this will open python Debuggger for the specified file

#The command 'next' will continue execution until the next line in the current function is reached or it returns

#The command 'step' executes the current line, but stops at the first possible occasion (either in a called function or on the next line in the current function)

#A breakpoint is an intentional stopping or pausing place in a program. The command 'break' takes as an argument the line number

#The “continue” command only stops when a breakpoint is encountered

#quit or exit to leave the debugger note that Leaving the debugger will clear your breakpoints.

#for bug 3. I can the program in pdb and used the continue command and noticed that the decrpyted message
# was decrypted. so i went back to the code and looked at the decrypting part of the code (line35-38) and found the error cypherkey shod of been decrpytkey in line 38

# I am stealing this

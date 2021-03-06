#importing os module to allow you to tun bash commands
import os
#displaying the curret working directory
os.system('ls')

#importing subprocess module. The subprocess.run() can take a lot of new arguments, but those additional arguments are optional
import subprocess

#Does the same thing is os.ssytem('ls')
subprocess.run(['ls'])

#the additional argument -l now lists the present working directory in long format
subprocess.run(['ls','-l','solution'])

#calling the uname command to get system information.
command='uname'

commandArgument='-a'

print(f'Gathering systen information with command: {command} {commandArgument}')

#actually running the command
subprocess.run([command,commandArgument])


command='ps'
commandArgument='-x'
# outping to screen Gathering active process information with the command=ps and commandArgument=-x
print(f'Gathering active process information with command : {command} {commandArgument}')
subprocess.run([command,commandArgument])

#Subprocess.run() is better than os.system(). For saftey: Developers often pass an input string os.sytem() without checking the actual commands. 
#Malicious users can pass in a string some stuff. Seperate process: subprocess.run() is implemented by a class called popen that is exceuted as a seperate.
#Additional functionality: Because subprocess.run() is realy the Popen class, it has new useful methods like poll(), wait(), and terminate()

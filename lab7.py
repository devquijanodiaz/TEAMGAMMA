# importing the module os using the import command
import os

# from the os module (os.system) use the ls bash command ('ls') to print the directories in the present working directory
os.system("ls")

# importing the module subprocess using the import command
import subprocess

# from the subprocess module (subprocess.run) use the ls bash command ('ls') to print the directories in the present working directory
subprocess.run(["ls"])

command='uname'

commandArgument='a'

print(f'Gathering systen information with command: {command} {commandArgument}')

subprocess.run([command,commandArgument])

command='ps'

commandArgument='-x'

# outping to screen Gathering active process information with the command=ps and commandArgument=-x
print(f'Gathering active process information with command : {command} {commandArgument}')

subprocess.run([command,commandArgument])

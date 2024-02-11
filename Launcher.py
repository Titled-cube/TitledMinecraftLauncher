#Titled Studio Production
#Version 1.0.3

#MINECRAFT. NOT APPROVED OR AFFILIATED WITH MOJANG OR MICROSOFT
#NOT MOJANG AB


print("MINECRAFT. NOT APPROVED OR AFFILIATED WITH MOJANG OR MICROSOFT")
print("NOT MOJANG AB\n \n \n")

eula = input("You are using a pirate launcher. So then you will want to upgrade to the official version of MINECRAFT. Have a good game!")

#importing
import minecraft_launcher_lib
import subprocess
import time

#create a directory

minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory().replace('minecraft', 'Cube Launcher ✮ ')

time.sleep(2)

print('made by: Titled Studio ✮')
#splash
time.sleep(0.9)
print("████████╗██╗████████╗██╗░░░░░███████╗██████╗░  ░██████╗████████╗██╗░░░██╗██████╗░██╗░█████╗")
time.sleep(0.9)
print("╚══██╔══╝██║╚══██╔══╝██║░░░░░██╔════╝██╔══██╗  ██╔════╝╚══██╔══╝██║░░░██║██╔══██╗██║██╔══██╗")
time.sleep(0.9)
print("   ██║░░░██║░░░██║░░░██║░░░░░█████╗░░██║░░██║  ╚█████╗░░░░██║░░░██║░░░██║██║░░██║██║██║░░██║")
time.sleep(0.9)
print("   ██║░░░██║░░░██║░░░██║░░░░░██╔══╝░░██║░░██║  ░╚═══██╗░░░██║░░░██║░░░██║██║░░██║██║██║░░██║")
time.sleep(0.9)
print("   ██║░░░██║░░░██║░░░███████╗███████╗██████╔╝  ██████╔╝░░░██║░░░╚██████╔╝██████╔╝██║╚█████╔╝")
time.sleep(0.9)
print("   ╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚═════╝░  ╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚═╝░╚════╝░")
time.sleep(0.9)


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=printEnd)
    if iteration == total:
        print()

def maximum(max_value, value):
    max_value[0] = value
#print ask
version = input('Select version: ')
username = input('username: ')
#load - print icon
print('=======================================================================================')

max_value = [0]

callback = {
        "setStatus": lambda text: print(text, end='r'),
        "setProgress": lambda value: printProgressBar(value, max_value[0]),
        "setMax": lambda value: maximum(max_value, value)
}
#downolad minecraft
minecraft_launcher_lib.install.install_minecraft_version(versionid=version, minecraft_directory=minecraft_directory, callback=callback)

options = {
    'username': username,
}
#open game
subprocess.call(minecraft_launcher_lib.command.get_minecraft_command(version=version, minecraft_directory=minecraft_directory, options=options))


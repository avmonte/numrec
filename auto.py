from os import system, listdir

for i in listdir("original/"):
	system(f"python3 main.py original/{i}")

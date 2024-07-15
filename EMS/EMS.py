import os
from datetime import datetime

# clear screen function
def clr(): os.system('cls')

# absolute file path
path = os.path.dirname(__file__)

# read and write data
data = '' # common data
def read_f_file(): 
	with open(path + '\\EMS.data', 'r') as rf:
		data = rf.readlines()

def write_t_file(content): 
	with open(path + '\\EMS.data', 'w') as wf:
		wf.writelines(data)

def menu():
	data = read_f_file()
	clr()
	print("Expensive management system:\n")
	print("1) Enter your expenses")
	print("2) Check your daily expensed")
	print("3) Check your weekly expensed")
	print("4) Check your quarterly expensed")
	print("5) Check your monthly expensed")
	print("6) Check your yearly expensed")

def add_expense():
	day = input()
	sep = sorted(set(day))[0]
	try:
		res = bool(datetime.strptime(day, f"%d{sep}%m{sep}%Y"))
	except:
		res = False
	if not res:
		input("Your typing is invalid, please press enter and try again ....")
		return
	
	typ = input("Enter your expensed type")

	day = day.split(sep)

add_expense()
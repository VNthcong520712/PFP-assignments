# 1-clear monitor
import os, string
def cls(): os.system("cls")
# 1-end clear monitor


# 2-open file, read and write
# read file
def rea():
	with open(os.path.dirname(__file__)+"\\GMS.data", "r") as rd:
		ot = rd.readlines()
		return ot # return file as list, split each line
# write file	
def wri(inp):
	with open(os.path.dirname(__file__)+"\\GMS.data", "w") as wr:
		wr.writelines(inp)
# 2-end read write


# 3-split each element in io_data to each component
def decode():
	global table_data
	table_data = rea() # variable store data as a list
	for x in range(len(table_data)): # x loop through the data to get each line
		_ = []
		c = table_data[x].split('"') 
		for y in range(len(c)): # split each component
			if len(c[y]) >= 3:
				if ", " in c[y]:
					c[y] = [float(z) for z in c[y].split(", ")]
				_.append(c[y])
		table_data[x] = _ # update to table_data to easy to handle
# 3-end split


# 4-find special id
def find(clid=-1, stid=-1, name = -1):
	out = []
	if len(table_data) > 0:
		for x in range(len(table_data)):
			if clid != -1 and stid != -1:
				if clid in table_data[x] and stid in table_data[x]:
					if name == -1:
						out.append(x)
					elif name in table_data[x]:
						out.append(x)
			elif clid != -1:
				if clid in table_data[x]:
					out.append(x)
			elif stid != -1:
				if stid in table_data[x]:
					if name == -1:
						out.append(x)
					elif name in table_data[x]:
						out.append(x)
	return out if out else -1
# 4-end find


# 5-write to the original file
def merge(position = -1, optional = 0):	
	pos = len(table_data) -1 if position == -1 else position # two option, -1 to add and other natural numbers to update
	read = rea()
	up = ''
	if optional:
		read.pop(pos)
	else:
		for el in table_data[pos]: # loop through value that is changed
			try:
				el.isalnum() # if it is a list (for grade)
				up += ('"' + str(el) + '" ')
			except:
				el = str(el)
				ln = len(el)
				up += ('"' + el[1:ln-1] + '" ')
		up += "\n" # variable change data
		if position == - 1:
			read.append(up)
		else:
			read[pos] = up
	wri(read) # write back to the file
	print("Done!")
# 5-end write


# main function

# 6-menu
def menu():
	cls()
	decode()

	print("GRADING MANAGEMENT SYSTEM")
	print("=========================")
	print("1) Add new a student's grade")
	print("2) Update a student's grade")
	print("3) Delete a student's grade")
	print("4) Calculate the average grade of a given class")
	print("5) Calculate the average grade of a given student")
	print("6) Find and list the grades of a given student in the tabular format")
	print("7) Find and list the grades of a given class in the tabular format")
	print("0) Exit\n")
# 6-end menu


# 7-input value that is needed for some functions
def typing(classid = 0, id = 0, name = 0, grade = 0):
	out = []
	# get input, check, and format
	try: 
		if classid: 
			cl = input("Type class ID: ").strip()
			for i in cl: 
				if not i.isalnum() and i not in ["_", "*"]:
					raise
			out.append(cl)

		if id:
			id = input("Type student ID: ")
			if not (id[:2].isalpha() and id[2:].isnumeric() and len(id) == 8): raise("Invalid")
			id = id[:2].upper() + id[2:]
			out.append(id)

		if name:
			na = input("Type name: ")
			na = na.strip().title()
			out.append(na)

		if grade:
			gr = []
			for x in input("Type grade include space (workshop progress assignment practical final): ").split():
				ln = len(gr)
				x = int(x) if x.isnumeric() else float(x)
				if 0 <= x <= 10 and ln <= 4:					
					gr.append(x)
				else:
					raise("Invalid")
			for i in range(4-ln):
				gr.append(0)
			out.append(gr)
	except:
		print("\nYour typing is invalid !!")
		return -1 # if invalid typed
	return out # return the needed values
# 7-end input


# 8-calculate student's grade
def cal_student(grade = 0):
	if grade:
		result = 0.1*(grade[0]+grade[1]+grade[2] + 4*grade[3] + 3*grade[4])
		return result
	else:
		print("Calculate average grade of student\n")
		id = typing(id=1)[0]
		info = find(stid=id)
		if info != -1:
			sum = 0
			for i in info:
				sum += table_data[i][3][5]
			print(f"{sum/len(info):.2f}")
			return
		print("ID is not found !!")
		return -1
# 8-end calculate


# 9-add new grade
def add_grade():
	print("Add new grade:\n")
	data = typing(1,1,1,1)
	if find(data[0], data[1]) != -1: # so bao danh va lop da co
		print(f"\nYour information is existed with name: {table_data[find(data[0], data[1])[0]][2]} !!")
	elif find(data[0]) == -1: # chua co lop 1 
		if find(stid=data[1]) != -1: # da co so bao danh voi ten x
			if find(stid=data[1], name=data[2]) == -1: # so bao danh va ten nhap vao khac voi file
				print("\nThe ID or name wrong !!")
			else: # so bao danh va ten nhap vao giong voi file
				final = cal_student(data[3])
				sta = 'Passed' if final >= 5 and data[3][4] >= 4 and data[3][2] > 0 and data[3][1] > 0 and data[3][0] > 0 else 'Failed'
		else: # khong co so bao danh
			final = cal_student(data[3])
			sta = 'Passed' if final >= 5 and data[3][4] >= 4 and data[3][2] > 0 and data[3][1] > 0 and data[3][0] > 0 else 'Failed'
	else: # da co lop 1 nhung chua co sbd trong lop do
		if find(stid=data[1]) != -1: # da co so bao danh voi ten x
			if find(stid=data[1], name=data[2]) == -1: # so bao danh va ten nhap vao khac voi file
				print("The ID or name wrong !!")
			else: # so bao danh va ten nhap vao giong voi file
				final = cal_student(data[3])
				sta = 'Passed' if final >= 5 and data[3][4] >= 4 and data[3][2] > 0 and data[3][1] > 0 and data[3][0] > 0 else 'Failed'
		else: # khong co so bao danh
			final = cal_student(data[3])
			sta = 'Passed' if final >= 5 and data[3][4] >= 4 and data[3][2] > 0 and data[3][1] > 0 and data[3][0] > 0 else 'Failed'
	data[3].append(final)
	data.append(sta)
	table_data.append(data)
	merge()
# 9-end add


# 10-update existed data
def update_grade():
	print("Update presented grade:\n")
	classid, id, grade = typing(classid = 1, id=1, grade=1)
	ind = find(classid,id)
	if ind == -1:
		print("\nThis data is not existed !!")
	else:
		final = cal_student(grade)
		sta = 'Passed' if final >= 5 and grade[4] >= 4 and grade[2] > 0 and grade[1] > 0 and grade[0] > 0 else 'Failed'
		ver = input(f'Do you want to change the grade of {table_data[find(classid, id)[0]][2]} (Y/N):')
		if ver.lower() == 'y':
			grade.append(final)
			table_data[ind[0]][3] = grade
			table_data[ind[0]][4] = sta
			merge(ind[0])
		elif ver.lower() == 'n':
			return
		else:
			print('\nInvalid !!')
			raise
# 10-end update


# 11-delete student's grade
def delete_grade():
	print("Delete an existed grade:\n")
	classid, id= typing(classid = 1, id=1)
	ind = find(classid,id)
	if ind == -1:
		print("\nThis data is not existed !!")
	else:
		ver = input(f'Do you want to delete the grade of {table_data[find(classid, id)[0]][2]} (Y/N):')
		if ver.lower() == 'y':
			table_data.pop(ind[0])
			merge(ind[0], 1)
		elif ver.lower() == 'n':
			return
		else:
			print('\nInvalid !!')
			raise
# 11-end delete


# 12-cal class greade
def cal_class():
	print("Calculate the avegrade grade of the class\n")
	classid= typing(1)[0]
	mems = find(classid)
	if mems != -1:
		sum = 0
		for i in mems:
			sum += table_data[i][3][5]
		print(f"{sum/len(mems):.2f}")
		return
	print("ID is not found !!")
	return -1
# 12-end cal


# 13-find student
def find_stu():
	print("Find class an grade of a student\n")
	id = typing(id=1)[0]
	cla = find(stid=id)
	if cla != -1:
		print("-"*84+"\n|   class name   | Workshop | Progress test | Practical exam | Final exam | Status |")
		form = "| {:<14} | {} | {} | {} | {} | {} |"
		for x in cla:
			pri = []
			pri.append(table_data[x][0] + ' '*(10 - len(table_data[x][0])))
			for gr in range(len(table_data[x][3])-1):
				if gr != 2:
					score = table_data[x][3][gr]
					score = str(int(score) if int(score) - score == 0 else score)
					pri.append(score)
			pri.append(table_data[x][4])
			print(form.format(pri[0], pri[1].center(8), pri[2].center(13), pri[3].center(14), pri[4].center(10), pri[5]))
		print("-"*84)
	else:
		print("Your typing is invalid !!")
# 13-end find


# 14-find grades of class
def find_cla():
	print("Find class an list students' grade\n")
	clsid = typing(1)[0]
	stus = find(clsid)
	if stus != -1:
		print("-"*113+f"\n| Student ID | {'Student name'.center(30)} | Workshop | Progress test | Practical exam | Final exam | Status |")
		form = "| {} | {} | {} | {} | {} | {} | {} |"
		for x in stus:
			pri = []
			pri.append(table_data[x][1])
			pri.append(table_data[x][2])
			for gr in range(len(table_data[x][3])-1):
				if gr != 2:
					score = table_data[x][3][gr]
					score = str(int(score) if int(score) - score == 0 else score)
					pri.append(score)
			pri.append(table_data[x][4])
			print(form.format(pri[0].ljust(10), pri[1].ljust(30), pri[2].center(8), pri[3].center(13), pri[4].center(14), pri[5].center(10), pri[6]))
		print("-"*113)
	else:
		print("Your typing is invalid !!")
# 14-end find

# main-execute code			
funs = [quit, add_grade, update_grade, delete_grade, cal_class, cal_student, find_stu, find_cla]
while True: 
	menu()
	try: 
		choice = int(input("Enter your choice: "))
		if choice == 0: 
			break
		elif 1 <= choice <= 7:
			cls()
			funs[choice]()
			_ = input("\nPress enter to return to main menu ")
		else:
			_ = input("Your choice is not available. Enter any key to try again.")
	except:
		_ = input("Enter any key to try again.")
# main-end exe
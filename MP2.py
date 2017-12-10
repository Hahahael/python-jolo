def add_student(database, ref):
	temp_dict = {}
	key = raw_input("Enter student number of student (ex: 201509321):\n>>>")
	temp_dict[ref[0]] = raw_input("Enter first name of student (ex: Jean Louie):\n>>>").title()
	temp_dict[ref[1]] = raw_input("Enter last name of student (ex: Victor):\n>>>").title()
	temp_dict[ref[2]] = raw_input("Enter middle name of student (ex: Aguilar):\n>>>").title()
	temp_dict[ref[3]] = raw_input("Enter suffix of student (ex: IV | 'n/a' if not applicable):\n>>>")
	temp_dict[ref[4]] = raw_input("Enter sex of student (M/F):\n>>>").title()
	temp_dict[ref[5]] = raw_input("Enter birthday of student in MMDDYY (ex: 102998):\n>>>")
	temp_dict[ref[6]] = raw_input("Enter course of student (ex: BS Industrial Engineering):\n>>>")
	database[key] = temp_dict
	return database

def edit_student(database):
	SD = search_student(database)
	temp_info = database[SD]
	temp_info["sex"] = (raw_input("Enter new sex of student (M/F):\n>>>"))
	temp_info["bday"] = (str(int(input("Enter new birthday of student in MMDDYY (ex: 102998):\n>>>"))))
	temp_info["course"] = (raw_input("Enter new course of student (ex: BS Industrial Engineering):\n>>>"))
	database[SD] = temp_info
	return database

def search_student(database):
	sn = raw_input("Enter student number to search (ex: 201509321): ")
	for i in database:
		if i == sn:
			return i

def add_faculty(database, ref):
	temp_dict = {}
	key = raw_input("Enter faculty number (ex: 201509321):\n>>>")
	temp_dict[ref[0]] = raw_input("Enter first name of faculty (ex: Rose Ann):\n>>>")
	temp_dict[ref[1]] = raw_input("Enter last name of faculty (ex: Zuniga):\n>>>")
	temp_dict[ref[2]] = raw_input("Enter middle name of faculty (ex: Sale):\n>>>")
	temp_dict[ref[3]] = raw_input("Enter suffix of faculty (ex: IV | 'n/a' if not applicable):\n>>>")
	temp_dict[ref[4]] = raw_input("Enter sex of faculty (M/F):\n>>>")
	temp_dict[ref[5]] = raw_input("Enter birthday of faculty in MMDDYY (ex: 102998):\n>>>")
	temp_dict[ref[6]] = raw_input("Enter college of faculty (ex: College of Engineering):\n>>>")
	temp_dict[ref[7]] = raw_input("Enter department of faculty (ex: Computer Science): \n>>>")
	database[key] = temp_dict
	return database

def edit_faculty(database):
	FD = search_faculty(database)
	temp_info = database[FD]
	temp_info["sex"] = (raw_input("Enter sex of faculty (M/F):\n>>>"))
	temp_info["bday"] = (str(int(input("Enter birthday of faculty in MMDDYY (ex: 102998):\n>>>"))))
	temp_info["college"] = (raw_input("Enter college of faculty (ex: College of Engineering):\n>>>"))
	temp_info["dept"] = (raw_input("Enter department of faculty (ex: Computer Science):\n>>>"))
	database[FD] = temp_info
	return database

def search_faculty(database):
	fn = raw_input("Enter faculty number to search (ex: 201509321): ")
	for i in database:
		if i == fn:
			return i
	
def add_subject(database, ref):
	temp_dict = {}
	key = raw_input("Enter subject number (ex: 52987):\n>>>")
	temp_dict[ref[0]] = raw_input("Enter subject code (ex: ES 26):\n>>>")
	temp_dict[ref[1]] = raw_input("Enter subject title (ex: Introduction to Computer Programming):\n>>>")
	temp_dict[ref[2]] = raw_input("Enter subject effectivity year (ex: 2016-2017):\n>>>")
	temp_dict[ref[3]] = raw_input("Enter subject status (active/inactive):\n>>>")
	database[key] = temp_dict
	return database

def edit_subject(database):
	UD = search_subject(database)
	temp_info = database[UD]
	temp_info["code"] = (raw_input("Enter subject code (ex: ES 26):\n>>>"))
	temp_info["title"] = (raw_input("Enter subject title (ex: Introduction to Computer Programming):\n>>>"))
	temp_info["e_year"] = (raw_input("Enter subject effectivity year (ex: 2016-2017):\n>>>"))
	temp_info["status"] = (raw_input("Enter subject status (active/inactive):\n>>>"))
	database[UD] = temp_info
	return database

def search_subject(database):
	subn = raw_input("Enter subject number to search (ex: 52987): ")
	for i in database:
		if subn == i:
			return i

# ^ add more security features
	
def assign_grade(database):
	s_no = search_subject(database)
	database[s_no][raw_input("Student number (ex: 201509321): ")] = float(input("Enter grade: "))
	return database
	
def enlist_student(database):
	s_no = search_subject(database)
	database[s_no][raw_input("Student number (ex: 201509321): ")] = "GRADE"
	print database
	return database

def assign_faculty(database):
	s_no = search_subject(database)
	database[s_no].append(raw_input("Faculty number (ex: 201509321): "))
	print database
	return database
	
def remove_student(database):
	s_no = search_subject(database)
	student = raw_input("Student number (ex: 201509321): ")
	for i in database[s_no]:
		if i == student:
			database[s_no].pop(student, None)
			break
	return database

def remove_faculty(database):
	s_no = search_subject(database)
	faculty = raw_input("Faculty number (ex: 201509321): ")
	for i in database[s_no]:
		if i == faculty:
			database[s_no].remove(faculty)
			break
	return database

def read_file( file, ref ):
	ctr = 0 
	ctr2 = 0
	database = {}
	for line in file:
		dnary = {}
		line = line.split("\n")
		line = line[0].split(",")
		key = line[0]
		for i in range(1,len(line)):
			dnary[ref[ctr]] = str(line[i])
			ctr = ctr + 1
		database[key] = dnary
		ctr = 0
		ctr2 = ctr2 + 1
	return database

def read_file_special(file):
	ctr = 0
	database = {}
	for line in file:
		dnary = {}
		line = line.split("\n")
		line = line[0].split(":")
		s_no = line[0]
		line = line[1].split(";")
		for entry in line:
			entry = entry.split(",")
			dnary[entry[0]] = entry[1]
		database[s_no] = dnary
		ctr = ctr + 1
	return database

def read_file_special2(file):
	database = {}
	for line in file:
		line = line.split("\n")
		line = line[0].split(":")
		s_no = line[0]
		faculty = line[1].split(",")
		database[s_no] = faculty 
	return database
	
def open_file(fname):
	try:
		file = open(str(fname + ".txt"), "r+")
	except IOError:
		print "Error! File not found. Now creating file."
		file = file = open(str(fname + ".txt"), "w+")
	return file

			
def save_file(database, file, ref, filename):
	file.close()
	file = open(filename+".txt", "w+")
	for key in database:
		file.write(key+',')
		for i in ref:
			if (i != len(ref)-1):
				file.write(database[key][ref[i]]+',')
			else:
				file.write(database[key][ref[i]]+'\n')
	return file

	
#main
student_ref = {0: "f_name", 1: "l_name", 2: "m_name", 3: "suffix", 4: "sex", 5: "bday", 6: "course"}
student_file = open_file("student")
student_database = read_file(student_file, student_ref)
print student_database
student_file = save_file(student_database, student_file, student_ref, "student")

faculty_ref = {0: "f_name", 1: "l_name", 2: "m_name", 3: "suffix", 4: "sex", 5: "bday", 6: "college", 7: "dept"}
faculty_file = open_file("faculty")
faculty_database = read_file(faculty_file, faculty_ref)
print faculty_database
faculty_file = save_file(faculty_database, faculty_file, faculty_ref, "faculty")

subject_ref = {0: "code", 1: "title", 2: "e_year", 3: "status"}
subject_file = open_file("subject")
subject_database = read_file(subject_file, subject_ref)
subject_database = edit_subject(subject_database)
print subject_database
subject_file = save_file(subject_database, subject_file, subject_ref, "subject")
# subject_student_ref = {0: "list", 1: "s_number", 2: "grade"}
# subject_student_file = open_file("subject_student")
# subject_faculty_file = open_file("subject_faculty")
# subject_student_database = read_file_special(subject_student_file)
# subject_faculty_database = read_file_special2(subject_faculty_file)

# add_student(student_file)
# print student_database
# student_file.close()

# add_faculty(faculty_file)
# print faculty_database
# faculty_file.close()

# add_subject(subject_file)
# print subject_database
# subject_file.close()

# student_database = edit_student(student_database)
# student_file = save_student_file(student_database, student_file)
# print student_database[search_student(student_database)]

# faculty_database = edit_faculty(faculty_database)
# faculty_file = save_faculty_file(faculty_database, faculty_file)
# print faculty_database[search_faculty(faculty_database)]

# subject_database = edit_subject(subject_database)
# subject_file = save_subject_file(subject_database, subject_file)
# print subject_database[search_subject(subject_database)]

# subject_student_database = enlist_student(subject_student_database)
# print subject_student_database
# subject_student_database = remove_student(subject_student_database)
# print subject_student_database

# subject_faculty_database = assign_faculty(subject_faculty_database)
# print subject_faculty_database
# subject_faculty_database = remove_faculty(subject_faculty_database)
# print subject_faculty_database

# print subject_student_database
# subject_student_database = assign_grade(subject_student_database)
# print subject_student_database
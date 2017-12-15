def add_student(database, ref):
	temp_dict = {}
	key = ""
	while (key == ""):
		key = raw_input("Enter student number of student (ex: 201509321):\n>>>")
		if (is_unique(database, key) == False):
			print ("Error! Student already exists! Returning to main menu...\n")
			return database
	temp_dict[ref[0]] = raw_input("Enter first name of student (ex: Jean Louie):\n>>> ").title()
	temp_dict[ref[1]] = raw_input("Enter last name of student (ex: Victor):\n>>> ").title()
	temp_dict[ref[2]] = raw_input("Enter middle name of student (ex: Aguilar):\n>>> ").title()
	temp_dict[ref[3]] = raw_input("Enter suffix of student (ex: IV | 'n/a' if not applicable):\n>>> ")
	if (temp_dict[ref[3]] == "n/a"): temp_dict[ref[3]] = " "
	temp_dict[ref[4]] = raw_input("Enter sex of student (M/F):\n>>> ").title()
	temp_dict[ref[5]] = raw_input("Enter birthday of student in MM/DD/YYYY (ex: 10/29/1998):\n>>> ")
	temp_dict[ref[6]] = raw_input("Enter course of student (ex: BS Industrial Engineering):\n>>> ")
	database[key] = temp_dict
	return database

def edit_student(database):
	SD = search_student(database)
	temp_info = database[SD]
	temp_info["sex"] = (raw_input("Enter new sex of student (M/F):\n>>> "))
	temp_info["bday"] = raw_input("Enter new birthday of student in MMDDYY (ex: 10/29/1998):\n>>> ")
	temp_info["course"] = (raw_input("Enter new course of student (ex: BS Industrial Engineering):\n>>> "))
	database[SD] = temp_info
	return database

def search_student(database):
	sn = raw_input("Enter student number (ex: 201509321): ")
	for i in database:
		if i == sn:
			return i
	print "Error! Student does not exist!"
	return 0

def add_faculty(database, ref):
	temp_dict = {}
	key = ""
	while (key == ""):
		key = raw_input("Enter faculty number of faculty (ex: 201509321):\n>>>")
		if (is_unique(database, key) == False):
			print ("Error! Faculty already exists! Returning to main menu...\n")
			return database
	temp_dict[ref[0]] = raw_input("Enter first name of faculty (ex: Rose Ann):\n>>> ").title()
	temp_dict[ref[1]] = raw_input("Enter last name of faculty (ex: Zuniga):\n>>> ").title()
	temp_dict[ref[2]] = raw_input("Enter middle name of faculty (ex: Sale):\n>>> ").title()
	temp_dict[ref[3]] = raw_input("Enter suffix of faculty (ex: IV | 'n/a' if not applicable):\n>>> ")
	if (temp_dict[ref[3]] == "n/a"): temp_dict[ref[3]] = " "
	temp_dict[ref[4]] = raw_input("Enter sex of faculty (M/F):\n>>> ").title()
	temp_dict[ref[5]] = raw_input("Enter birthday of faculty in MM/DD/YYYY (ex: 10/29/1998):\n>>> ")
	temp_dict[ref[6]] = raw_input("Enter college of faculty (ex: College Of Engineering):\n>>> ").title()
	temp_dict[ref[7]] = raw_input("Enter department of faculty (ex: Computer Science): \n>>> ").title()
	database[key] = temp_dict
	return database

def edit_faculty(database):
	FD = search_faculty(database)
	temp_info = database[FD]
	temp_info["sex"] = (raw_input("Enter sex of faculty (M/F):\n>>> ")).title()
	temp_info["bday"] = raw_input("Enter birthday of faculty in MMDDYY (ex: 10/29/1998):\n>>> ")
	temp_info["college"] = (raw_input("Enter college of faculty (ex: College of Engineering):\n>>> ")).title()
	temp_info["dept"] = (raw_input("Enter department of faculty (ex: Computer Science):\n>>> ")).title()
	database[FD] = temp_info
	return database

def search_faculty(database):
	fn = raw_input("Enter faculty number (ex: 201509321): ")
	for i in database:
		if i == fn:
			return i
	print "Error! Faculty does not exist!"
	return 0
	
def add_subject(database, ref):
	temp_dict = {}
	key = ""
	while (key == ""):
		key = raw_input("Enter subject number of subject (ex: 52918):\n>>>")
		if (is_unique(database, key) == False):
			print ("Error! Student already exists! Returning to main menu...\n")
			return database
	temp_dict[ref[0]] = raw_input("Enter subject code (ex: ES 26):\n>>> ")
	temp_dict[ref[1]] = raw_input("Enter subject title (ex: Introduction to Computer Programming):\n>>> ")
	temp_dict[ref[2]] = raw_input("Enter subject effectivity year (ex: 2016-2017):\n>>> ")
	temp_dict[ref[3]] = raw_input("Enter subject status (active/inactive):\n>>> ")
	database[key] = temp_dict
	return database

def edit_subject(database):
	UD = search_subject(database)
	temp_info = database[UD]
	temp_info["code"] = (raw_input("Enter subject code (ex: ES 26):\n>>> "))
	temp_info["title"] = (raw_input("Enter subject title (ex: Introduction to Computer Programming):\n>>> "))
	temp_info["e_year"] = (raw_input("Enter subject effectivity year (ex: 2016-2017):\n>>> "))
	temp_info["status"] = (raw_input("Enter subject status (active/inactive):\n>>> "))
	database[UD] = temp_info
	return database

def search_subject(database):
	subn = raw_input("Enter subject number (ex: 52987): ")
	for i in database:
		if subn == i:
			return i
	print "Error! Subject does not exist!"
	return 0

def is_unique(database, comparable):
	for key in database:
		if comparable == key:
			return False
	return True

def update_subjects(db_1, db_2, db_3):
	for subj in db_1:
		if (subj in db_2) == False:
			db_2[subj] = {}
		if (subj in db_3) == False:
			db_3[subj] = []
	return db_2, db_3
	
def enlist_student(db_1, db_2):
	subj_no = search_subject(db_1)
	if (subj_no == 0): return db_1
	stud_no = search_student(db_2)
	if (stud_no == 0): return db_1
	if stud_no in db_1[subj_no]:
		print ("Error! Student already enrolled!\n")
		return db_1
	grade = raw_input("Enter grade of student (ex. 94.87 | n/a if no grade): ")
	db_1[subj_no][stud_no] = grade
	print "Student enlisted into subject\n"
	return db_1

def remove_student(database):
	subj_no = search_subject(database)
	stud_no = raw_input("Student number (ex: 201509321): ")
	if (stud_no in database[subj_no]) == False:
		print "Error! Student not enrolled in class!\n"
		return database
	if database[subj_no][stud_no] != "n/a":
		print ("Error! Student already has a grade. Student cannot be removed.\n")
		return database
	for i in database[subj_no]:
		if i == stud_no:
			database[subj_no].pop(stud_no, None)
			break
	return database

def assign_faculty(db_1, db_2):
	subj_no = search_subject(db_1)
	if (subj_no == 0): return db_1
	fac_no = search_faculty(db_2)
	if (fac_no == 0): return db_1
	if fac_no in db_1[subj_no]:
		print "Error! Faculty already assigned.\n"
		return db_1
	db_1[subj_no].append(fac_no)
	print "Faculty assigned to subject\n"
	return db_1

def remove_faculty(database):
	subj_no = search_subject(database)
	faculty = raw_input("Faculty number (ex: 201509321): ")
	if (faculty in database[subj_no]) == False:
		print "Error! Faculty is not assigned to this subject.\n"
		return database
	for i in database[subj_no]:
		if i == faculty:
			database[subj_no].remove(faculty)
			break
	return database

def assign_grade(db_1, db_2):
	subj_no = search_subject(db_1)
	if (subj_no == 0): return db_1
	stud_no = search_student(db_2)
	if (stud_no == 0): return db_1
	if (stud_no in db_1[subj_no] == False):
		print "Error! Student not enrolled in class\n"
	grade = raw_input("Enter grade [0 - 100]: ")
	db_1[subj_no][stud_no] = grade
	return db_1
	
def read_file(file, ref):
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

def read_file_2(file):
	ctr = 0
	database = {}
	for line in file:
		dnary = {}
		line = line.split("\n")
		line = line[0].split(":")
		s_no = line[0]
		if(len(line[1]) != 0):
			line = line[1].split(";")
			for entry in line:
				entry = entry.split(",")
				dnary[entry[0]] = entry[1]
		database[s_no] = dnary
		ctr = ctr + 1
	return database

def read_file_3(file):
	database = {}
	for line in file:
		faculty = []
		line = line.split("\n")
		line = line[0].split(":")
		s_no = line[0]
		if (len(line[1]) != 0):
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

def save_file_2(database, file, filename):
	file.close()
	file = open(filename+".txt", "w+")
	for key in database:
		file.write(key+':')
		ctr = (len(database[key]))
		for s_no in database[key]:
			if ctr != 1:
				file.write(s_no+","+database[key][s_no]+";")
			else:
				file.write(s_no+","+database[key][s_no]+"\n")
			ctr = ctr - 1
	return file

def save_file_3(database, file, filename):
	file.close()
	file = open(filename+".txt", "w+")
	for key in database:
		file.write(key+':')
		if (len(database[key]) == 0): continue
		for i in range(0, len(database[key])):
			if (i != len(database[key])-1):
				file.write(database[key][i]+',')
			else:
				file.write(database[key][i]+'\n')
	return file

# report generation VVV

def count_students_under_course(database):
	ctr = 0
	course = raw_input("Enter degree program (ex. BS Industrial Engineering): ")
	for student in database:
		if (database[student]["course"] == course):
			ctr = ctr + 1
	if (ctr == 0):
		print "There are no students taking the", course, "degree program\n"
		return
	print "Students taking", course, ":", ctr

def count_students_under_subject(db_1, db_2):
	subj_no = search_subject(db_1)
	if (subj_no == 0):
		print "Error! No such subject exists\n"
		return
	print "Students under", db_2[subj_no]["code"], str("["+subj_no+"]") , ":", len(db_1[subj_no])

def count_total_students(database):
	print "Total number of students:", len(database)

def count_faculty_per_department(database):
	ctr = 0
	dept = raw_input("Enter department: ").title()
	for fac_no in database:
		if database[fac_no]["dept"] == dept:
			ctr = ctr + 1
	if (ctr == 0):
		print "There are no faculty members under", dept
		return
	print "Faculty members under", dept, ":", ctr

def count_faculty_per_college(database):
	ctr = 0
	coll = raw_input("Enter college: ").title()
	for fac_no in database:
		if database[fac_no]["college"] == coll:
			ctr = ctr + 1
	if (ctr == 0):
		print "There are no faculty members under", coll
		return
	print "Faculty members under", coll, ":", ctr

def count_total_faculty(database):
	print "Total number of faculty members:", len(database)

def count_sex_students(database, sex):
	ctr = 0
	for s_n in database:
		if database[s_n]["sex"] == sex:
			ctr = ctr + 1
	if (sex == "M"):
		print "Number of male students :", ctr
	if (sex == "F"):
		print "Number of female students :", ctr

def count_subjects_under_faculty(db_1, db_2):
	fac_no = search_faculty(db_2)
	if (fac_no == 0):
		return
	ctr = 0
	for subj_no in db_1:
		if fac_no in db_1[subj_no]:
			ctr = ctr + 1
	if (ctr == 0):
		print "There are no subjects under", db_2[fac_no]["f_name"], db_2[fac_no]["m_name"], db_2[fac_no]["l_name"], db_2[fac_no]["suffix"], str("["+fac_no+"]")
		return
	print "Subjects under", dept, ":", ctr

def view_students(database):
	if (len(database) == 0):
		print "\nNo students yet. Returning to main menu...\n"
		return
	print str("FORMAT:\n-------------------------------------------------------------------------------------\nStudent No. | Last Name | First Name | Middle Name | Suffix | Sex | Birthday | Course\n-------------------------------------------------------------------------------------\n")
	for student in database:
		string = str("\n"+student+" | "+database[student]["f_name"]+" | "+database[student]["l_name"]+" | "+database[student]["m_name"]+" | "+database[student]["suffix"]+" | "+database[student]["sex"]+" | "+database[student]["bday"]+" | "+database[student]["course"]+"\n")
		print "-"*(len(string)-1) + string + "-"*(len(string)-1)

def view_faculty(database):
	if (len(database) == 0):
		print "\nNo faculty yet. Returning to main menu...\n"
		return
	print str("FORMAT:\n---------------------------------------------------------------------------------------------------\nFaculty No. | Last Name | First Name | Middle Name | Suffix | Sex | Birthday | College | Department\n---------------------------------------------------------------------------------------------------\n")
	for faculty in database:
		string = str("\n"+faculty+" | "+database[faculty]["f_name"]+" | "+database[faculty]["l_name"]+" | "+database[faculty]["m_name"]+" | "+database[faculty]["suffix"]+" | "+database[faculty]["sex"]+" | "+database[faculty]["bday"]+" | "+database[faculty]["college"]+" | "+database[faculty]["dept"]+"\n")
		print "-"*(len(string)-1) + string + "-"*(len(string)-1)

def view_subjects(database):
	if (len(database) == 0):
		print "\nNo subjects yet. Returning to main menu...\n"
		return
	print str("FORMAT:\n----------------------------------------------------------------------\nSubject No. | Subject Code | Subject Title | Effectivity Year | Status\n----------------------------------------------------------------------\n")
	for subject in database:
		string = str("\n"+subject+" | "+database[subject]["code"]+" | "+database[subject]["title"]+" | "+database[subject]["e_year"]+" | "+database[subject]["status"]+"\n")
		print "-"*(len(string)-1) + string + "-"*(len(string)-1)

def view_students_under_subject(db_1, db_2, db_3, ref):
	subj_no = search_subject(db_1)
	if (subj_no == 0): return db_1
	if (len(db_1[subj_no]) == 0):
		print "---------------------------------\nNo students enlisted in class yet\n---------------------------------\n"
		return
	print "\n---------------------\nStudents under", db_3[subj_no]["code"], str("["+subj_no+"]"), "\n---------------------\n"
	for student in db_1[subj_no]:
		string = str("\n"+student+" | "+db_2[student]["l_name"]+" , "+db_2[student]["f_name"]+" "+db_2[student]["m_name"]+" "+db_2[student]["suffix"]+" | "+db_1[subj_no][student]+" - "+str(convert_grade(db_1[subj_no][student], ref))+"\n")
		print "-"*(len(string)-1) + string + "-"*(len(string)-1)

def view_subject_faculty_pair(db_1, db_2, db_3):
	for subject in db_1:
		if (len(db_1[subject]) == 0):
			print "----------------------------------------\nNo faculty members assigned to", db_3[subject]["code"], str("["+subject+"]"),"yet\n----------------------------------------\n"
			continue
		print "\n-------------------------------\nFaculty members under", db_3[subject]["code"], str("["+subject+"]"), "\n-------------------------------"
		for faculty in db_1[subject]:
			string = str("\n"+faculty+" | "+db_2[faculty]["l_name"]+" , "+db_2[faculty]["f_name"]+" "+db_2[faculty]["m_name"]+" "+db_2[faculty]["suffix"]+"\n")
			print "-"*(len(string)-1) + string + "-"*(len(string)-1)

def view_specific_student(db_1, db_2, db_3, ref):
	stud_no = search_student(db_1)
	if (stud_no == 0): return
	print "\n------------------------STUDENT------------------------\nStudent Number:\t", stud_no
	print "Name:\t\t", db_1[stud_no]["l_name"],",", db_1[stud_no]["f_name"], db_1[stud_no]["m_name"], db_1[stud_no]["suffix"]
	print "Sex:\t\t", db_1[stud_no]["sex"]
	print "Birthday:\t", db_1[stud_no]["bday"]
	print "Course:\t\t", db_1[stud_no]["course"], "\n\n-------------------CLASS INFORMATION-------------------"
	print "Subject Number \tSubject Code \tGrade\n"
	for subject in db_2:
		if (stud_no in db_2[subject]):
			print subject,"\t\t", db_3[subject]["code"], "\t\t", convert_grade(db_2[subject][stud_no], ref)
	print "--------------------------END--------------------------\n"

def view_specific_faculty(db_1, db_2, db_3):
	fac_no = search_faculty(db_1)
	if (fac_no == 0): return
	print "\n------------------------FACULTY------------------------\nFaculty Number:\t", fac_no
	print "Name:\t\t", db_1[fac_no]["l_name"],",", db_1[fac_no]["f_name"], db_1[fac_no]["m_name"], db_1[fac_no]["suffix"]
	print "Sex:\t\t", db_1[fac_no]["sex"]
	print "Birthday:\t", db_1[fac_no]["bday"]
	print "Department:\t", db_1[fac_no]["dept"]
	print "College:\t", db_1[fac_no]["college"], "\n\n--------------------COURSES HANDLED--------------------"
	print "Subject Number \tSubject Code \tSubject Title\n"
	for subject in db_2:
		if fac_no in db_2[subject]:
			print subject,"\t\t", db_3[subject]["code"], "\t\t", db_3[subject]["title"]
	print "--------------------------END--------------------------\n"

def view_specific_subject(db_1, db_2, db_3, db_4, db_5, ref):
	subj_no = search_subject(db_1)
	if (subj_no == 0): return
	print "\n------------------------SUBJECT------------------------\nSubject Number:\t\t", subj_no
	print "Subject Code:\t\t", db_1[subj_no]["code"]
	print "Title:\t\t\t", db_1[subj_no]["title"]
	print "Effectivity Year:\t", db_1[subj_no]["e_year"]
	print "Status:\t\t\t", db_1[subj_no]["status"]
	print "\n----------------FACULTY MEMBER ASSIGNED----------------\nFaculty Number \tName \t\t"
	for faculty in db_2:
		if faculty in db_3[subj_no]:
			print faculty, " ", db_2[faculty]["f_name"], db_2[faculty]["m_name"], db_2[faculty]["l_name"], db_2[faculty]["suffix"]
	print "\n-------------------ENLISTED STUDENTS-------------------\nStudent Number \tName \t\tGrade\n"
	for student in db_4:
		if student in db_5[subj_no]:
			print student, " ", db_4[student]["f_name"], db_4[student]["m_name"], db_4[student]["l_name"], db_4[student]["suffix"], "|", db_5[subj_no][student], "-", str(convert_grade(db_5[subj_no][student], ref))
	print "--------------------------END--------------------------\n"


def convert_grade(percentage, ref):
	for grade in ref:
		try:
			if int(float(percentage)) in ref[grade]:
				return grade
		except:
			return "n/a [No grade yet]"

#main

grade_ref = {1.0: list(range(92,101)), 1.25: list(range(88,92)), 1.5: list(range(84,88)), 1.75: list(range(80,84)), 2.0: list(range(76,80)), 2.25: list(range(72,76)), 2.5: list(range(68,72)), 2.75: list(range(64,68)), 3.0: list(range(60,64)), 5.0: list(range(0, 60))}#

#initialize student
student_ref = {0: "f_name", 1: "l_name", 2: "m_name", 3: "suffix", 4: "sex", 5: "bday", 6: "course"}
student_file = open_file("student")
student_database = read_file(student_file, student_ref)

#initilalize faculty
faculty_ref = {0: "f_name", 1: "l_name", 2: "m_name", 3: "suffix", 4: "sex", 5: "bday", 6: "college", 7: "dept"}
faculty_file = open_file("faculty")
faculty_database = read_file(faculty_file, faculty_ref)

#initialize subject
subject_ref = {0: "code", 1: "title", 2: "e_year", 3: "status"}
subject_file = open_file("subject")
subject_database = read_file(subject_file, subject_ref)

#initialize subject_student
subject_student_file = open_file("subject_student")
subject_student_database =  read_file_2(subject_student_file)

#initialize subject_faculty
subject_faculty_file = open_file("subject_faculty")
subject_faculty_database = read_file_3(subject_faculty_file)

#main main
while(True):
	option = -1
	while (option < 0 or option > 6):
		option = int(input("------------------\nChoose an option:\n------------------\n1 - Add\n2 - Edit\n3 - Enlistment\n4 - Assigning Faculty\n5 - Grade\n6 - Generate reports\n0 - Exit\n>>> "))
		if (option < 0 or option > 6):
			print "Error! Incorrect input!"

	if (option == 0):
		print "Saving files...\n"

		print str("Saving student.txt... Please don't exit...\n")
		student_file = save_file(student_database, student_file, student_ref, "student")
		student_file.close()
		print str("student.txt saved!\n")

		print str("Saving faculty.txt... Please don't exit...\n")
		faculty_file = save_file(faculty_database, faculty_file, faculty_ref, "faculty")
		faculty_file.close()
		print str("faculty.txt saved!\n")

		print str("Saving subject.txt... Please don't exit...\n")
		subject_file = save_file(subject_database, subject_file, subject_ref, "subject")
		subject_file.close()
		print str("subject.txt saved!\n")

		print str("Saving subject_student.txt... Please don't exit...\n")
		subject_student_file = save_file_2(subject_student_database, subject_student_file, "subject_student")
		subject_student_file.close()
		print str("subject_student.txt saved!\n")

		print str("Saving subject_faculty.txt... Please don't exit...\n")
		subject_faculty_file = save_file_3(subject_faculty_database, subject_faculty_file, "subject_faculty")
		subject_faculty_file.close()
		print str("subject_faculty.txt saved!\n")

		print "Done saving files. Now exiting...\n\n"
		exit(0)
	
	if (option == 1):
		add = -1
		while (add < 0 or add > 3):
			add = int(input("-------------------\nChoose what to add:\n-------------------\n1 - Student\n2 - Faculty\n3 - Subject\n0 - Back\n>>> "))
			if (add < 0 or add > 3):
				print "Error! Incorrect input!\n"
		if (add == 0):
			continue
		if (add == 1):
			student_database = add_student(student_database, student_ref)
			student_file = save_file(student_database, student_file, student_ref, "student")
			continue
		if (add == 2):
			faculty_database = add_faculty(faculty_database, faculty_ref)
			faculty_file = save_file(faculty_database, faculty_file, faculty_ref, "faculty")
			continue
		if (add == 3):
			subject_database = add_subject(subject_database, subject_ref)
			subject_student_database, subject_faculty_database = update_subjects(subject_database, subject_student_database, subject_faculty_database)
			subject_student_file = save_file_2(subject_student_database, subject_student_file, "subject_student")
			subject_faculty_file = save_file_3(subject_faculty_database, subject_faculty_file, "subject_faculty")
			subject_file = save_file(subject_database, subject_file, subject_ref, "subject")
			continue

	if (option == 2):
		edit = -1
		while (edit < 0 or edit > 3):
			edit = int(input("-------------------\nChoose what to edit:\n-------------------\n1 - Student\n2 - Faculty\n3 - Subject\n0 - Back\n>>> "))
			if (edit < 0 or edit > 3):
				print "Error! Incorrect input!\n"
		if (edit == 0):
			continue
		if (edit == 1):
			student_database = edit_student(student_database)
			student_file = save_file(student_database, student_file, student_ref, "student")
			continue
		if (edit == 2):
			faculty_database = edit_faculty(faculty_database)
			faculty_file = save_file(faculty_database, faculty_file, faculty_ref, "faculty")
			continue
		if (edit == 3):
			subject_database = edit_subject(subject_database)
			subject_file = save_file(subject_database, subject_file, subject_ref, "subject")
			continue

	if (option == 3):
		enlist = -1
		while (enlist < 0 or enlist > 2):
			enlist = int(input("-------------------\nChoose what to do:\n-------------------\n1 - Enlist a student to a subject\n2 - Remove a student from a subject\n0 - Back\n>>> "))
			if (enlist < 0 or enlist > 2):
				print "Error! Incorrect input!\n"
		if (enlist == 0):
			continue
		if (enlist == 1):
			subject_student_database = enlist_student(subject_student_database, student_database)
			subject_student_file = save_file_2(subject_student_database, subject_student_file, "subject_student")
			continue
		if (enlist == 2):
			subject_student_database = remove_student(subject_student_database)
			subject_student_file = save_file_2(subject_student_database, subject_student_file, "subject_student")
			continue

	if (option == 4):
		assign = -1
		while (assign < 0 or assign > 2):
			assign = int(input("-------------------\nChoose what to do:\n-------------------\n1 - Assign a faculty to a subject\n2 - Remove a faculty from a subject\n0 - Back\n>>> "))
			if (assign < 0 or assign > 2):
				print "Error! Incorrect input!\n"
		if (assign == 0):
			continue
		if (assign == 1):
			subject_faculty_database = assign_faculty(subject_faculty_database, faculty_database)
			subject_faculty_file = save_file_3(subject_faculty_database, subject_faculty_file, "subject_faculty")
			continue
		if (assign == 2):
			subject_faculty_database = remove_faculty(subject_faculty_database)
			subject_faculty_file = save_file_3(subject_faculty_database, subject_faculty_file, "subject_faculty")
			continue

	if (option == 5):
		subject_student_database = assign_grade(subject_student_database, student_database)
		subject_student_file = save_file_2(subject_student_database, subject_student_file, "subject_student")

	if (option == 6):
		report = -1
		while (report < 0 or report > 3):
			report = int(input("----------------------------\nWhat would you like to view:\n----------------------------\n1 - Lists\n2 - Counts\n3 - Information\n0 - Exit\n>>> "))
			if (report < 0 or report > 3):
				print "Error! Incorrect Input!\n"
		if (report == 0):
			continue
		if (report == 1):
			lists = -1
			while (lists < 0 or lists > 5):
				lists = int(input("----------------------------\nWhich list would you like to view:\n----------------------------\n1 - Students\n2 - Faculty Members\n3 - Subjects\n4 - Students enlisted in a subject\n5 - Subject|Faculty pair\n0 - Back\n>>> "))
				if (lists < 0 or lists > 5):
					print "Error! Incorrect Input!\n"
			if (lists == 0):
				continue
			if (lists == 1):
				view_students(student_database)
				continue
			if (lists == 2):
				view_faculty(faculty_database)
				continue
			if (lists == 3):
				view_subjects(subject_database)
				continue
			if (lists == 4):
				view_students_under_subject(subject_student_database, student_database, subject_database, grade_ref)
				continue
			if (lists == 5):
				view_subject_faculty_pair(subject_faculty_database, faculty_database, subject_database)
				continue
		
		if (report == 2):
			count = -1
			while (count < 0 or count > 9):
				count = int(input("----------------------------\nWhich count would you like:\n----------------------------\n1 - Students under a course\n2 - Total numbers of students\n3 - Faculty members under a college\n4 - Faculty members under a department\n5 - Total number of faculty\n6 - Male students\n7 - Female students\n8 - Students enlisted in a subject\n9 - Courses handled by a faculty\n0 - Back\n>>> "))
				if (count < 0 or count > 9):
					print "Error! Incorrect Input!\n"
			if (count == 0):
				continue
			if (count == 1):
				count_students_under_course(student_database)
				continue
			if (count == 2):
				count_total_students(student_database)
				continue
			if (count == 3):
				count_faculty_per_college(faculty_database)
				continue
			if (count == 4):
				count_faculty_per_department(faculty_database)
				continue
			if (count == 5):
				count_total_faculty(faculty_database)
				continue
			if (count == 6):
				count_sex_students(student_database, "M")
				continue
			if (count == 7):
				count_sex_students(student_database, "F")
				continue
			if (count == 8):
				count_students_under_subject(subject_student_database, subject_database)
				continue
			if (count == 9):
				count_subjects_under_faculty(subject_student_database, faculty_database)
				continue
		
		if (report == 3):
			info = -1
			while (info < 0 or info > 9):
				info = int(input("-------------------------------------------\nWhich specific information would you like:\n-------------------------------------------\n1 - Student\n2 - Faculty\n3 - Subject\n0 - Back\n>>> "))
				if (info < 0 or info > 9):
					print "Error! Incorrect Input!\n"
			if (info == 0):
				continue
			if (info == 1):
				view_specific_student(student_database, subject_student_database, subject_database, grade_ref)
				continue
			if (info == 2):
				view_specific_faculty(faculty_database, subject_faculty_database, subject_database)
				continue
			if (info == 3):
				view_specific_subject(subject_database, faculty_database, subject_faculty_database, student_database, subject_student_database, grade_ref)
				continue
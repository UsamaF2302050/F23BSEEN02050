


# Define a class for Faculty
class Faculty:
	def __init__(self, name):
		self.name = name
		self.departments = []

# Define a class for Department
class Department:
	def __init__(self, name, faculty):
		self.name = name
		self.faculty = faculty
		self.courses = []
		self.students = []

# Define a class for Campus
class Campus:
	def __init__(self, name):
		self.name = name
		self.faculties = []

# Define a class for Course
class Course:
	def __init__(self, name, code, department):
		self.name = name
		self.code = code
		self.department = department
		self.students = []

# Define a class for Student
class Student:
	def __init__(self, name, roll_number, department):
		self.name = name
		self.roll_number = roll_number
		self.department = department
		self.courses = []

# Define a class for the Academic Session
class AcademicSession:
	def __init__(self):
		self.campuses = []

	def add_campus(self, campus):
		self.campuses.append(campus)

	def add_faculty(self, faculty, campus):
		campus.faculties.append(faculty)

	def add_department(self, department, faculty):
		faculty.departments.append(department)

	def add_course(self, course, department):
		department.courses.append(course)

	def add_student(self, student, department):
		department.students.append(student)

	def enroll_student_in_course(self, student, course):
		student.courses.append(course)
		course.students.append(student)

	def print_student_courses(self, student):
		print(f"{student.name} is enrolled in:")
		for course in student.courses:
			print(course.name)

# Create an instance of the AcademicSession class
session = AcademicSession()

# Create some campuses, faculties, departments, courses, and students
campus1 = Campus("abbasia")
faculty1 = Faculty("Science")
department1 = Department("software", faculty1)
course1 = Course("oop", "software01", department1)
student1 = Student("usama", 1, department1)

campus2 = Campus("baghdad")
faculty2 = Faculty("Arts")
department2 = Department("English", faculty2)
course2 = Course("Literature", "ENG101", department2)
student2 = Student("usama", 2, department2)





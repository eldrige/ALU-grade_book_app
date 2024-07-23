import csv
from student import Student
from course import Course

students_csv_file = 'students.csv'
courses_csv_file = 'courses.csv'


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.load_students_from_csv()
        self.load_courses_from_csv()

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        self.save_students_to_csv()
        print('----------------------------------------------')
        print(f"Student {student.names} added successfully.")
        print('----------------------------------------------')

        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_courses_to_csv()
        print('----------------------------------------------')
        print(f"Course {course.name} added successfully.")
        print('----------------------------------------------')

        return course

    def register_student_for_course(self, student, course):
        student.register_for_course(course)

    # def calculate_GPA(self):
    #     for student in self.student_list:
    #         student.calculate_GPA()

    # def calculate_ranking(self):
    #     self.student_list.sort(key=lambda x: x.GPA, reverse=True)

    # def search_by_grade(self, grade_range):
    #     students = []
    #     for student in self.student_list:
    #         for course in student.courses_registered:
    #             if grade_range[0] <= course.grade <= grade_range[1]:
    #                 students.append(student)
    #                 break
    #     return students

    def save_students_to_csv(self):
        with open(students_csv_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for student in self.student_list:
                writer.writerow([student.email, student.names])

    def save_courses_to_csv(self):
        with open(courses_csv_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for course in self.course_list:
                writer.writerow(
                    [course.name, course.trimester, course.credits])

    def generate_transcript(self, student):
        print(f"Transcript for {student.names}")
        print(f"Email: {student.email}")
        print(f"GPA: {student.GPA:.2f}")
        print("Courses Registered:")
        for course in student.courses_registered:
            print(
                f"- {course.name} ({course.trimester}, {course.credits} credits) - Grade: {course.grade}")

    def load_students_from_csv(self):
        try:
            with open(students_csv_file, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    email, names = row
                    student = Student(email, names)
                    self.student_list.append(student)
        except FileNotFoundError:
            print(
                f"No {students_csv_file} file found. Starting with an empty student list.")

    def load_courses_from_csv(self):
        try:
            with open(courses_csv_file, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    name, trimester, credit = row
                    course = Course(name, trimester, credit)
                    self.course_list.append(course)
        except FileNotFoundError:
            print(
                f"No {courses_csv_file} file found. Starting with an empty course list.")

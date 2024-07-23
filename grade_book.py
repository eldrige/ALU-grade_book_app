import csv
import json
from student import Student
from course import Course

students_json = 'students.json'
courses_json = 'courses.json'


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.load_students_from_json()
        self.load_courses_from_json()

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append({
            'email': student.email,
            'names': student.names,
            'courses_registered': [],
            'GPA': 0.0
        })
        self.save_students()
        print('----------------------------------------------')
        print(f"Student {student.names} added successfully.")
        print('----------------------------------------------')

        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append({
            'name': course.name,
            'trimester': course.trimester,
            'credits': course.credits,
        })
        self.save_courses()
        print('----------------------------------------------')
        print(f"Course {course.name} added successfully.")
        print('----------------------------------------------')

        return course

    def register_student_for_course(self, student, course):
        student.register_for_course(course)

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        self.student_list.sort(key=lambda x: x.GPA, reverse=True)

    def search_by_grade(self, grade_range):
        students = []
        for student in self.student_list:
            for course in student.courses_registered:
                if grade_range[0] <= course.grade <= grade_range[1]:
                    students.append(student)
                    break
        return students

    def save_students(self):
        """
        Save the student data to a JSON file.
        """
        with open(students_json, 'w') as file:
            json.dump(self.student_list, file, indent=4)

    def save_courses(self):
        """
        Save the course data to a JSON file.
        """
        with open(courses_json, 'w') as file:
            json.dump(self.course_list, file, indent=4)

    def generate_transcript(self, student):
        print(f"Transcript for {student.names}")
        print(f"Email: {student.email}")
        print(f"GPA: {student.GPA:.2f}")
        print("Courses Registered:")
        for course in student.courses_registered:
            print(
                f"- {course.name} ({course.trimester}, {course.credits} credits) - Grade: {course.grade}")

    def load_students_from_json(self):
        try:
            with open(students_json, 'r') as file:
                students = json.load(file)
                self.student_list = students
        except FileNotFoundError:
            print(
                f"No {students_json} file found. Starting with an empty student list.")

    def load_courses_from_json(self):
        try:
            with open(courses_json, 'r') as file:
                courses = json.load(file)
                self.course_list = courses
        except FileNotFoundError:
            print(
                f"No {courses_json} file found. Starting with an empty course list.")


import json
from student import Student
from course import Course

STUDENTS_JSON = 'students.json'
COURSES_JSON = 'courses.json'


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []
        self.load_students_from_json()
        self.load_courses_from_json()

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        self.save_students()
        print('----------------------------------------------')
        print(f"Student {student.names} added successfully.")
        print('----------------------------------------------')

        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_courses()
        print('----------------------------------------------')
        print(f"Course {course.name} added successfully.")
        print('----------------------------------------------')

        return course

    def register_student_for_course(self, student_email, course_name):
        """
        Register a student for a course.

        Args:
            student_email (str): The email of the student.
            course_name (str): The name of the course.
        """
        student = next(
            (s for s in self.student_list if s.email == student_email), None)
        course = next(
            (c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course)
            self.save_students()
            print('----------------------------------------------')
            print(f"Student {student.names} registered for course {
                  course.name}.")
            print('----------------------------------------------')
        else:
            print("Student or course not found.")

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()
        sorted_students = sorted(
            self.student_list, key=lambda s: s.GPA, reverse=True)
        print('------------------------------------------------------------')
        print(f"{'Rank':<5}{'Name':<20}{'Email':<20}{'GPA':<5}")
        for i, student in enumerate(sorted_students, start=1):
            print(f"{i:<5}{student.names:<20}{
                  student.email:<20}{student.GPA:.2f}")
        print('------------------------------------------------------------')

        return sorted_students

    def search_by_grade(self, grade_range):
        students = []
        for student in self.student_list:
            for course in student.courses_registered:
                if grade_range[0] <= course['grade'] <= grade_range[1]:
                    students.append(student)
                    break
        return students

    def save_students(self):
        """
        Save the student data to a JSON file.
        """
        with open(STUDENTS_JSON, 'w') as file:
            json.dump([s.__dict__ for s in self.student_list], file, indent=4)

    def save_courses(self):
        """
        Save the course data to a JSON file.
        """
        with open(COURSES_JSON, 'w') as file:
            json.dump(
                [course.__dict__ for course in self.course_list], file, indent=4)

    def generate_transcript(self, student):
        print('------------------------------------------------------------')
        print(f"Transcript for {student.names}")
        print(f"Email: {student.email}")
        print(f"GPA: {student.GPA:.2f}")
        print("Courses Registered:")
        for course in student.courses_registered:
            print(
                f"- {course['name']} ({course['trimester']}, {course['credits']} credits) - Grade: {course['grade']}")
        print('------------------------------------------------------------')

    def load_students_from_json(self):
        try:
            with open(STUDENTS_JSON, 'r') as file:
                students = json.load(file)
                self.student_list = [Student(**data) for data in students]
        except FileNotFoundError:
            print(
                f"No {STUDENTS_JSON} file found. Starting with an empty student list.")

    def load_courses_from_json(self):
        try:
            with open(COURSES_JSON, 'r') as file:
                courses = json.load(file)
                self.course_list = [Course(**data) for data in courses]
        except FileNotFoundError:
            print(
                f"No {COURSES_JSON} file found. Starting with an empty course list.")

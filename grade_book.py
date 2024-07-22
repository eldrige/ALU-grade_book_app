from student import Student
from course import Course


class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        # print(f"Student {student.names} added successfully.")
        return student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print(f"Course {course.name} added successfully.")
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

    def generate_transcript(self, student):
        print(f"Transcript for {student.names}")
        print(f"Email: {student.email}")
        print(f"GPA: {student.GPA:.2f}")
        print("Courses Registered:")
        for course in student.courses_registered:
            print(
                f"- {course.name} ({course.trimester}, {course.credits} credits) - Grade: {course.grade}")

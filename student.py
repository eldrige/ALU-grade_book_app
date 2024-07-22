class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    # def calculate_GPA(self):
    #     total_credits = 0
    #     total_grade_points = 0
    #     for course in self.courses_registered:
    #         total_credits += course.credits
    #         total_grade_points += course.credits * course.grade
    #     self.GPA = total_grade_points / total_credits if total_credits else 0.0

    def register_for_course(self, course):
        self.courses_registered.append(course)

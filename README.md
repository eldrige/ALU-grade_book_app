# Eldrige's Grade Book Application

## File Structure

The application is organized into the following files:

1. **main.py**:

   - This is the main entry point of the application.
   - It prompts the user with the available options and handles the user's input.
   - It coordinates the interactions between the different components of the application.

2. **course.py**:

   - This file contains the `Course` class, which represents a course in the grade book.
   - The `Course` class has attributes such as course name, credits, and a list of students enrolled in the course.
   - It provides methods to add and retrieve information about a course.

3. **students.py**:

   - This file contains the `Student` class, which represents a student in the grade book.
   - The `Student` class has attributes such as name, email, and a list of courses the student is registered for.
   - It provides methods to add, update, and retrieve information about a student.

4. **gradebook.py**:

   - This file contains the `Gradebook` class, which is the main data structure that manages the grade book.
   - The `Gradebook` class has methods to add students, add courses, register students for courses, calculate student rankings, search by grade, and generate transcripts.
   - It also handles the persistence of student and course data using the `json` module.

5. **students.json**:

   - This file is used to store the student data in JSON format.
   - When the application is run, it reads the student data from this file and updates it when changes are made.

6. **courses.json**:
   - This file is used to store the course data in JSON format.
   - When the application is run, it reads the course data from this file and updates it when changes are made.

The file structure of the application is designed to promote modularity, reusability, and maintainability. Each file focuses on a specific aspect of the application, making it easier to understand, test, and extend the codebase.

## Usage

To run the Eldrige's Grade Book Application, execute the `main.py` file:

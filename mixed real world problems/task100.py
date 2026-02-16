class Student:
    def __init__(self):
        self.students={}

    def add_student(self, id, name, age, birthday):
        self.students[id] = [name, age, birthday]
        print("Student added successfully!")

    def student_update(self, id, name=None, age=None, birthday=None):
        if id in self.students:
            if name:
                self.students[id][0] = name
            if age:
                self.students[id][1] = age
            if birthday:
                self.students[id][2] = birthday
            print("Student updated!")
        else:
            print("Student not found!")

    def student_delete(self,id):
        if id in self.students:
            del self.students[id]
            print("Student deleted successfully!")
        else:
            print("Student not found!")
    def student_view(self):
        print("Student list:")
        for id, details in self.students.items():
            print(f"Student id {id}::Name-{details[0]}-Age-{details[1]}-Birthday-{details[2]}")

class Course:
    def __init__(self):
        self.courses={}

    def course_add(self,id,course):
        if id not in self.courses:
            self.courses[id]=[]
        self.courses[id].append(course)
        print("Course added successfully!")
    def course_update(self,previous_course,new_course):
        if id in self.courses and  previous_course in self.courses[id]:
            self.courses[id].remove(previous_course)
            self.courses[id].append(new_course)
            print("Course updated successfully!")
        else:
            print("Course not found!")

    def course_delete(self,id,course):
        if id in self.courses and course in self.courses[id]:
            self.courses[id].remove(course)
            print("Course deleted successfully!")
        else:
            print("Course not found!")
    def course_view(self):
        print("Course list:")
        for id, courses in self.courses.items():
            print(f"the courses of {id}: is {courses}")

def main():
    s = Student()
    c=Course()

    while True:
        print("Welcome to mini student management system")
        print("1.Add student details")
        print("2.Update student details")
        print("3.Delete student details")
        print("4.View student details")
        print("5.Add courses")
        print("6.Update course details")
        print("7.Delete course details")
        print("8.View course details")
        print("9.Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            id=int(input("Enter student id:"))
            name=input("Enter student name: ")
            age=int(input("Enter student age: "))
            birthday=int(input("Enter birthday:"))
            s.add_student( id, name, age, birthday)
        elif choice == 2:
            id = int(input("Enter student id:"))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            birthday = int(input("Enter birthday:"))
            s.student_update( id, name=None, age=None, birthday=None)
        elif choice==3:
            id = int(input("Enter student id:"))
            s.student_delete(id)
        elif choice==4:
            s.student_view()
        elif choice==5:
            id=int(input("Enter student id:"))
            course=input("Enter the course: ")
            c.course_add(id, course)
        elif choice==6:
            id=int(input("Enter student id:"))
            previous_course=input("Enter the previous course: ")
            new_course=input("Enter the new course: ")
            c.course_update(id,previous_course,new_course)
        elif choice==7:
            id=int(input("Enter student id:"))
            course=input("Enter the course: ")
            c.course_delete(id,course)
        elif choice==8:
            c.course_view()
        elif choice==9:
            print("Exiting from the system")
        else:
            print("Invalid choice. Please try again")

main()

#optimized code
class Student:
    def __init__(self):
        self.students = {}

    def add_student(self, sid, name, age, birthday):
        self.students[sid] = {
            "name": name,
            "age": age,
            "birthday": birthday
        }
        print("✅ Student added successfully!")

    def update_student(self, sid, name=None, age=None, birthday=None):
        if sid not in self.students:
            print("❌ Student not found!")
            return

        if name:
            self.students[sid]["name"] = name
        if age:
            self.students[sid]["age"] = age
        if birthday:
            self.students[sid]["birthday"] = birthday

        print("✅ Student updated successfully!")

    def delete_student(self, sid):
        if sid in self.students:
            del self.students[sid]
            print("✅ Student deleted successfully!")
        else:
            print("❌ Student not found!")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n📋 Student List")
        for sid, info in self.students.items():
            print(f"ID:{sid} | Name:{info['name']} | Age:{info['age']} | Birthday:{info['birthday']}")


# -------------------------------------------------

class Course:
    def __init__(self):
        self.courses = {}

    def add_course(self, sid, course):
        self.courses.setdefault(sid, []).append(course)
        print("✅ Course added successfully!")

    def update_course(self, sid, old_course, new_course):
        if sid in self.courses and old_course in self.courses[sid]:
            index = self.courses[sid].index(old_course)
            self.courses[sid][index] = new_course
            print("✅ Course updated successfully!")
        else:
            print("❌ Course not found!")

    def delete_course(self, sid, course):
        if sid in self.courses and course in self.courses[sid]:
            self.courses[sid].remove(course)
            print("✅ Course deleted successfully!")
        else:
            print("❌ Course not found!")

    def view_courses(self):
        if not self.courses:
            print("No course data available.")
            return

        print("\n📚 Course List")
        for sid, courses in self.courses.items():
            print(f"ID:{sid} -> {courses}")


# -------------------------------------------------

def get_student_input():
    sid = int(input("Enter student id: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    birthday = input("Enter birthday: ")
    return sid, name, age, birthday


# -------------------------------------------------

def main():
    student = Student()
    course = Course()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View students")
        print("5. Add course")
        print("6. Update course")
        print("7. Delete course")
        print("8. View courses")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid, name, age, birthday = get_student_input()
            student.add_student(sid, name, age, birthday)

        elif choice == "2":
            sid, name, age, birthday = get_student_input()
            student.update_student(sid, name, age, birthday)

        elif choice == "3":
            sid = int(input("Enter student id: "))
            student.delete_student(sid)

        elif choice == "4":
            student.view_students()

        elif choice == "5":
            sid = int(input("Enter student id: "))
            c = input("Enter course: ")
            course.add_course(sid, c)

        elif choice == "6":
            sid = int(input("Enter student id: "))
            old_c = input("Old course: ")
            new_c = input("New course: ")
            course.update_course(sid, old_c, new_c)

        elif choice == "7":
            sid = int(input("Enter student id: "))
            c = input("Course: ")
            course.delete_course(sid, c)

        elif choice == "8":
            course.view_courses()

        elif choice == "9":
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()





# s.add_student(1, name="Maisha", age=22, birthday=24)
# s.add_student(2, name="Rahat", age=22, birthday=29)
# s.student_update(1, age=23)
# c.course_add(1, "Python")
# c.course_add(1, "Data Structures")
# c.course_add(2, "AI")
# c.course_update(1, "Python", "Advanced Python")
# c.course_delete(1,"Data Structures")
# s.student_delete(1)
# s.student_view()
# c.course_view()

class Course:
    def __init__(self, name1):
        self.coursename = name1
        self.grade = 101

    """
    ctor of course class
    
    :param:course name
    :param:grade: grade of the course
    """

    def set_grade(self, grade1):
        if 0 <= grade1 <= 100:
            self.grade = float(grade1)

    """
    sets the grade between 0 and 100

    :param:grade
    """

    def get_course_name(self):
        return self.coursename

    """
    returns course name

    :param:self
    :return:name
    """

    def get_grade(self):
        return self.grade

    """
    returns grade of course

    :param:self
    :return:grade
    """

    def __str__(self):
        return f'{self.coursename} {self.grade}'

    def __repr__(self):
        return f'course name: {self.coursename} \n course grade:{self.grade}'


class Student:
    def __init__(self, name1, id1):
        self.name = name1
        self.__id = id1
        self.course = []

        """
        ctor of student class

        :param: name
        :param:(private) id
        :param:array of courses 
        """

    def get_id(self):
        return self.__id

    """
    return the id of the student

    :param:self
    :return:id
    """

    def get_name(self):
        return self.name

    """
    return the name of the student

    :param:self
    :return:name
    """

    def get_course_list(self):
        return self.course

    def add_course(self, course1):
        if 0 <= course1.get_grade() <= 100:
            self.course.append(course1)

    """
    function adds a course to  the course list if the grade of the course is between 0 and 100

    :param:course
    """

    def re_avg(self):
        return sum(list(map(lambda x: x.get_grade(), self.course)))/len(self.course)

    """
    the function calculates the average of the student's courses

    :param:self
    :return:average
    """

    def re_course_grade(self, course1):
        g = list(filter(lambda x: (x.get_course_name() == course1), self.course))
        if len(g) == 0:
            return 0
        else:
            return g[0].get_grade()

    """
    the function returns the grade of a specific course

    :param:course
    :return:course grade
    """

    def ret(self):
        if len(self.course) > 0:
            return len(self.course)
        else:
            return 0

    def check_course(self, course1):
        g = list(filter(lambda x: (x.get_course_name() == course1), self.course))
        return len(g)

    """
    the function checks if the course exists 

        :param:course
        :return:1 if exits 0 if there is no on the list
    """

    def __str__(self):
        return f'{self.name} {self.__id}'

    def __repr__(self):
        return f' name: {self.name} \n id:{self.__id}'


try:
    num = 0
    txt = input("please enter a text file: \n")
    f = open(txt, 'r')
    student_arr = []
    for line in f:
        name = line.strip().split('\t')[0]
        id2 = line.strip().split('\t')[1]
        student = Student(name, id2)
        course_list = line.strip().split('\t')[2].split(';')
        for j in course_list:
            count = 0
            course_name = j.split('#')[0]
            course_grade = float(j.split('#')[1])
            if student.ret() > 0:
                for i in student.get_course_list():
                    if course_name == i.get_course_name():
                        i.set_grade(course_grade)
                        count += 1
                if count == 0:
                    course = Course(course_name)
                    course.set_grade(course_grade)
                    student.add_course(course)
            else:
                course = Course(course_name)
                course.set_grade(course_grade)
                student.add_course(course)
        student_arr.append(student)
    f.close()

except FileNotFoundError:
    num = 8
    print(" file not found have a nice day")

"""
The function tries to open the file and when it opens it adds  a students and courses to a list

:param:text file
:return:list of students
"""

while num != 8:
    try:
        choice = int(input("1.Student's average: \n2.Average of a course: \n3.All student average: \n4.Exit: \n"))
        if choice == 1:
            full_name = input("Please enter a name: \n")
            if not isinstance(full_name, str):
                raise ValueError("Must be string")


            def get_name(student1):
                if full_name == student1.get_name():
                    return student1.get_id()
                else:
                    return False


            """
            the function returns the id of the student if he exists and false if not

                :param:student object
                :return:id or false
            """


            def isname(student1):
                if full_name == student1.get_name():
                    return student1.re_avg()
                else:
                    return 0


            """
            the function returns the average of the student if it is not  the student it returns 0

            :param:student object
            :return:average or 0
            """

            avg = list(map(isname, student_arr))
            y_name = list(map(get_name, student_arr))
            n_name = list(filter(lambda x: isinstance(x, str), y_name))

            if sum(avg) > 0:
                print("The average of ", n_name[0], " is :", sum(avg))
            else:
                print("The person doesnt exits")

        """
        option 1  checks if the student exists and if he does it prints his average
        :param: student's name
        """

        if choice == 2:
            course_name1 = input("Please enter a course name: \n")
            if not isinstance(course_name1, str):
                raise ValueError("Must be string")


            def is_course_name(student1):
                return student1.re_course_grade(course_name1)


            """
            the function returns all grades from the same course

            :param:student object
            return course grade
            """


            def is_count(student1):
                return student1.check_course(course_name1)


            """
            the function checks if the student learns the course 

            :param:student object
            return 1/0
            """

            avg1 = sum(list(map(is_course_name, student_arr)))
            avg2 = sum(list(map(is_count, student_arr)))
            if avg1 != 0 and avg2 != 0:
                print(" The average of the course is :", avg1 / avg2, "\n")
            else:
                print("The course doesnt exists\n")

            """
            option 2 calculates the average of a course in total
            :param: course's name
            """

        if choice == 3:
            filename = input("please enter file name: \n")
            if not isinstance(filename, str):
                raise ValueError("Must be string \n")


            def id_list(student1):
                return student1.get_id()


            """
            the function gets the id of the student

            :param: student object
            return id
            """


            def avg_list(student1):
                return student1.re_avg()


            """
            the function gets the average of the student

            :param: student object
            return average
            """

            z = open(filename, 'w')
            a = list(map(id_list, student_arr))
            b = list(map(avg_list, student_arr))
            c = list(map(lambda x, y: f'{x}  {y} \n', a, b))
            z.writelines(c)
            z.close()

        if choice == 4:
            print("Have a nice day")
            num = 8

        if choice < 0 or choice > 4:
            print("wrong number please enter again\n")

    except ValueError:
        print("Please enter again")





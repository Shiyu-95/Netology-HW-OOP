class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        if len_rating != 0:
            return round(sum_rating / len_rating, 2)
        else:
            return "Оценок за курс нет"

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_rating()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Необходимо сравнивать студентов")
            return
        return self.av_rating() < other.av_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        if len_rating != 0:
            return round(sum_rating / len_rating, 2)
        else:
            return "Оценок за курс нет"

    def __str__(self):
        res = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_rating()}"
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Необходимо сравнивать преподавателей")
            return
        return self.av_rating() < other.av_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res


# Студенты
student_1 = Student('Николай', 'Рыбин', 'Муж')
student_1.courses_in_progress += ['Python', "Git"]
student_1.finished_courses += ["Введение в программирование", "Администрирование"]

student_2 = Student('Елена', 'Семенова', 'Жен')
student_2.courses_in_progress += ['Python', "Java", "Администрирование"]
student_2.finished_courses += ["Введение в программирование", "Git"]

# Лекторы
lecturer_1 = Lecturer('Иван', 'Морозов')
lecturer_1.courses_attached += ['Python', "Git", "Java"]

lecturer_2 = Lecturer('Наталья', 'Лескова')
lecturer_2.courses_attached += ["Введение в программирование", "Администрирование"]

# Проверяющие
reviewer_1 = Reviewer('Ярослав', 'Никитин')
reviewer_1.courses_attached += ['Python', "Java", "Git"]

reviewer_2 = Reviewer('Ольга', 'Быркова')
reviewer_2.courses_attached += ['Python', "Администрирование", "Введение в программирование"]

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Git', 4)

reviewer_2.rate_hw(student_1, 'Администрирование', 5)
reviewer_2.rate_hw(student_1, 'Python', 5)
reviewer_2.rate_hw(student_1, "Введение в программирование", 4)

reviewer_1.rate_hw(student_2, 'Python', 3)
reviewer_1.rate_hw(student_2, 'Git', 5)

reviewer_2.rate_hw(student_2, 'Python', 4)
reviewer_2.rate_hw(student_2, 'Администрирование', 5)
reviewer_2.rate_hw(student_2, 'Введение в программирование', 3)

# Оценки лекторам
student_1.rate_lw(lecturer_1, 'Python', 5)
student_1.rate_lw(lecturer_1, 'Git', 5)

student_2.rate_lw(lecturer_1, 'Python', 5)
student_2.rate_lw(lecturer_1, 'Java', 4)
student_2.rate_lw(lecturer_1, 'Git', 5)

student_1.rate_lw(lecturer_2, 'Введение в программирование', 5)
student_1.rate_lw(lecturer_2, 'Администрирование', 5)

student_2.rate_lw(lecturer_2, 'Введение в программирование', 4)
student_2.rate_lw(lecturer_2, 'Администрирование', 3)


print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)
print(student_1.av_rating_for_course('Python'))
print(lecturer_1.av_rating_for_course('Python'))
print(student_2.av_rating_for_course('Python'))
print(lecturer_2.av_rating_for_course('Python'))
print(student_1.av_rating_for_course('Введение в программирование'))
print(lecturer_1.av_rating_for_course('Введение в программирование'))
print(student_2.av_rating_for_course('Введение в программирование'))
print(lecturer_2.av_rating_for_course('Введение в программирование'))
print(student_1.av_rating_for_course('Java'))
print(lecturer_1.av_rating_for_course('Java'))
print(student_2.av_rating_for_course('Java'))
print(lecturer_2.av_rating_for_course('Java'))
print(student_1.av_rating_for_course('Администрирование'))
print(lecturer_1.av_rating_for_course('Администрирование'))
print(student_2.av_rating_for_course('Администрирование'))
print(lecturer_2.av_rating_for_course('Администрирование'))
print(student_1.av_rating_for_course('Git'))
print(lecturer_1.av_rating_for_course('Git'))
print(student_2.av_rating_for_course('Git'))
print(lecturer_2.av_rating_for_course('Git'))

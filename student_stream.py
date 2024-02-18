from student_group import StudentGroup

class StudentStream:
    def __init__(self, stream_number):
        """
        Конструктор класса StudentStream.

        Parameters:
            stream_number (str): Номер потока студентов.
        """
        self.stream_number = stream_number
        self.student_groups = []

    def add_group(self, group_name, number_of_students):
        """
        Метод для добавления новой учебной группы в поток студентов.

        Parameters:
            group_name (str): Название учебной группы.
            number_of_students (int): Количество студентов в группе.
        """
        group = StudentGroup(group_name, number_of_students)
        self.student_groups.append(group)

    def sort_groups(self):
        """Метод для сортировки учебных групп сначала по количеству студентов, а затем по идентификатору группы."""
        self.student_groups = sorted(self.student_groups, key=lambda x: (x.number_of_students, x.group_name))

    def __iter__(self):
        """Метод для получения итератора по учебным группам в потоке."""
        return iter(self.student_groups)


# from student_group import StudentGroup

# class StudentStream:
#     def __init__(self, stream_number):
#         """
#         Конструктор класса StudentStream.

#         Parameters:
#             stream_number (str): Номер потока студентов.
#         """
#         self.stream_number = stream_number
#         self.student_groups = []

#     def add_group(self, group_name, number_of_students):
#         """
#         Метод для добавления новой учебной группы в поток студентов.

#         Parameters:
#             group_name (str): Название учебной группы.
#             number_of_students (int): Количество студентов в группе.
#         """
#         group = StudentGroup(group_name, number_of_students)
#         self.student_groups.append(group)

#     def sort_groups(self):
#         """Метод для сортировки учебных групп по количеству студентов."""
#         self.student_groups = sorted(self.student_groups)

#     def __iter__(self):
#         """Метод для получения итератора по учебным группам в потоке."""
#         return iter(self.student_groups)

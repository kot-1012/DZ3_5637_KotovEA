class StudentGroup:
    def __init__(self, group_name, number_of_students):
        """
        Конструктор класса StudentGroup.

        Parameters:
            group_name (str): Название учебной группы.
            number_of_students (int): Количество студентов в группе.
        """
        self.group_name = group_name
        self.number_of_students = number_of_students

    def __lt__(self, other):
        """
        Метод сравнения меньше для сортировки объектов StudentGroup по количеству студентов.

        Parameters:
            other (StudentGroup): Другой объект StudentGroup для сравнения.

        Returns:
            bool: True, если текущий объект StudentGroup имеет меньшее количество студентов, чем другой объект.
        """
        return self.number_of_students < other.number_of_students

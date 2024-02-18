from student_stream import StudentStream

if __name__ == "__main__":
    # Создаем поток студентов
    stream = StudentStream("Stream 1")
    
    # Добавляем учебные группы
    stream.add_group("Group A", 20)
    stream.add_group("Group B", 25)
    stream.add_group("Group C", 30)
    
    # Сортируем группы по количеству студентов
    stream.sort_groups()
    
    # Выводим отсортированные группы
    print(f"Student Stream: {stream.stream_number}")
    for group in stream:
        print(f"Group Name: {group.group_name}, Number of Students: {group.number_of_students}")
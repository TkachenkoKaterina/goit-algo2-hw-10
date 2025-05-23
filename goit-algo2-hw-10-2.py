# Визначення класу Teacher
class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


def create_schedule(subjects, teachers):
    uncovered = set(subjects)
    selected_teachers = []

    while uncovered:

        best_teacher = None
        best_cover = set()

        for teacher in teachers:
            can_cover = teacher.can_teach_subjects & uncovered
            if len(can_cover) > len(best_cover):
                best_cover = can_cover
                best_teacher = teacher
            elif (
                len(can_cover) == len(best_cover)
                and best_teacher
                and teacher.age < best_teacher.age
            ):
                best_cover = can_cover
                best_teacher = teacher

        if not best_teacher or not best_cover:
            return None

        best_teacher.assigned_subjects = best_cover
        selected_teachers.append(best_teacher)
        uncovered -= best_cover
        teachers.remove(best_teacher)

    return selected_teachers


if __name__ == '__main__':

    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр", "Іваненко", 45, "o.ivanenko@example.com",
            {"Математика", "Фізика"}
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій", "Коваленко", 50, "s.kovalenko@example.com",
            {"Інформатика", "Математика"}
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com",
            {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро", "Бондаренко", 35, "d.bondarenko@example.com",
            {"Фізика", "Інформатика"}
        ),
        Teacher(
            "Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}
        )
    ]
    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("\n📚 Розклад занять:\n")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, "
                f"{teacher.age} років, "
                f"email: {teacher.email}"
            )
            print(
                f"   Викладає предмети: "
                f"{', '.join(sorted(teacher.assigned_subjects))}\n"
            )
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")

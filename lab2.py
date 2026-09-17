students = {
    "olesia": {
        "password": "1234",
        "grades": [12, 10, 8, 6, 4, 11, 9]
    },
    "yaroslav": {
        "password": "4567",
        "grades": [5, 7, 3, 10, 12, 4, 8]
    },
    "mariya": {
        "password": "3876",
        "grades": [5, 2, 4, 2, 11, 8]
    },
    "alina": {
        "password": "4098",
        "grades": [2, 11, 10, 4, 6, 2, 8]
    }
}

login = input("Введіть логін: ")
password = input("Введіть пароль: ")

if login in students and students[login]["password"] == password:
    print("\nВхід виконано успішно!")
    print("Оцінки користувача:", students[login]["grades"])
    
    grades = students[login]["grades"]

    print("\nAll grades:", grades)

    zadovilni = 0
    nezadovilni = 0

    for grade in grades:
        if grade >= 5 and grade <= 12:
            zadovilni += 1
        elif grade >= 1 and grade <= 4:
            nezadovilni += 1

    print("Grades from 5 to 12:", zadovilni)
    print("Grades from 1 to 4:", nezadovilni)

else:
    print("Nepravylni login abo parol!")

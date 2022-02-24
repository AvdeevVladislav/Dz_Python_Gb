# Задание № 3


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    for j in range(len(tutors)):
        yield tutors[j], klasses[j] if j < len(klasses) else None


generator = check_gen(tutors, klasses)
# print(type(generator), * generator)
for _ in range(len(tutors)):
    print(next(generator))

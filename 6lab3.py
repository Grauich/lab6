allLang = set() #В множестве не может быть повторяющихся ключей

studentsLang = {
    "Никита": {"английский", "французский", "немецкий"},
    "Колян": {"английский", "китайский", "испанский"},
    "Егор": {"русский", "китайский", "японский"},
    "Аман": {"английский", "испанский"},
    "Артемыч": {"французский", "немецкий"},
}

for languages in studentsLang.values(): #Идет по значениям (словарям)
    allLang.update(languages) #Метод множеств (обновляем множества)
sortedLang = sorted(allLang)
print("Отсортированный список всех языков:")
for language in sortedLang:
    print(language)

china = []

for student, languages in studentsLang.items()
    if "китайский" in languages
        china.append(student)

print("\nСтуденты, которые знают китайский язык:")
for student in china:
    print(student)

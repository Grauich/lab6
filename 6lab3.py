allLang = set()

studentsLang = {
    "Никита": {"английский", "французский", "немецкий"},
    "Колян": {"английский", "китайский", "испанский"},
    "Егор": {"русский", "китайский", "японский"},
    "Аман": {"английский", "испанский"},
    "Артемыч": {"французский", "немецкий"},
}

for languages in studentsLang.values():
    allLang.update(languages)
sortedLang = sorted(allLang)
print("Отсортированный список всех языков:")
for language in sortedLang:
    print(language)

china = [
    student for student, languages in studentsLang.items() if "китайский" in languages
]

print("\nСтуденты, которые знают китайский язык:")
for student in china:
    print(student)

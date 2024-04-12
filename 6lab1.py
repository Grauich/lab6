strani = {
    "Россия": "Москва",
    "США": "Вашингтон",
    "Китай": "Пекин",
    "Япония": "Токио",
    "Германия": "Берлин",
    "Франция": "Париж",
    "Великобритания": "Лондон",
}

print(f"Страны и их столицы:")
for country, capital in strani.items():
    print(f"{country} - {capital}")

strana = "Россия"
print(f"\nСтолица страны {strana}: {strani.get(strana, 'Не найдено')}")

sorted_countries_capitals = sorted(strani.items(), key=lambda x: x[0])
print(f"\nСодержимое словаря в алфавитном порядке:")
for country, capital in sorted_countries_capitals:
    print(country, "-", capital)

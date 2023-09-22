# Запросить у пользователя вес и рост
weight = float(input("Введите свой вес в килограммах: "))
height = float(input("Введите свой рост в метрах: "))

# Рассчитать ИМТ
bmi = weight / (height ** 2)

# Определить категорию веса на основе ИМТ
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Рассчитать необходимый вес для достижения нормы (ИМТ 18.5-24.9)
ideal_weight_min = 18.5 * (height ** 2)
ideal_weight_max = 24.9 * (height ** 2)
ideal_weight_diff = round(ideal_weight_max - weight, 1)

# Вывести результаты
print("Ваш ИМТ: {:.1f} ({})".format(bmi, category))
if category != "Normal weight":
    print("Необходимо {} кг для достижения нормы (ИМТ 18.5-24.9)".format(abs(ideal_weight_diff)))
else:
    print("Вы уже находитесь в нормальном весе!")
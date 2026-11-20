import math


def read_float(prompt, min_value=None, max_value=None):
    """Ввод числа с проверкой."""
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if min_value is not None and value < min_value:
                print(f"Значение должно быть не меньше {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Значение должно быть не больше {max_value}.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите число.")


def machines_needed(line_capacity, machine_capacity):
    """Количество машин с округлением вверх."""
    return math.ceil(line_capacity / machine_capacity)


def main():
    print("=" * 55)
    print(" РАСЧЁТ ОБОРУДОВАНИЯ ПЕЛЬМЕННОГО ЦЕХА")
    print("=" * 55)

    # Исходные данные
    q_day = read_float("Суточная выработка пельменей Qсут, т: ", min_value=0.000001)
    shift_hours = read_float("Продолжительность одной смены t, ч: ", min_value=0.000001)

    dough_share = read_float(
        "Массовая доля теста в готовой продукции, %: ",
        min_value=0,
        max_value=100
    )

    dumpling_machine_capacity = read_float(
        "Производительность пельменного автомата, т/ч: ",
        min_value=0.000001
    )
    mixer_capacity = read_float(
        "Производительность тестомесильной машины, т/ч: ",
        min_value=0.000001
    )
    cutter_capacity = read_float(
        "Производительность куттера, т/ч: ",
        min_value=0.000001
    )

    # I. Линия изготовления пельменей
    # Цех работает в две смены: Pтл = Qсут / (2 * t)
    line_capacity = q_day / (2 * shift_hours)
    dumpling_machines = machines_needed(
        line_capacity, dumpling_machine_capacity
    )
    
    print("\nСпасибо за использование программы!")
    print("Расчёт оборудования линии пельменей успешно завершён.")

    # II. Линия подготовки теста
    dough_capacity = dough_share * line_capacity / 100
    mixers = machines_needed(dough_capacity, mixer_capacity)

    # III. Линия подготовки фарша
    # По методичке доля фарша равна 100% - доля теста.
    meat_share = 100 - dough_share
    meat_capacity = meat_share * line_capacity / 100
    cutters = machines_needed(meat_capacity, cutter_capacity)

    # Вывод результатов
    print("\n" + "=" * 55)
    print(" РЕЗУЛЬТАТЫ РАСЧЁТА")
    print("=" * 55)

    print("\nI. Технологическая линия изготовления пельменей")
    print(f"Производительность линии: {line_capacity:.3f} т/ч")
    print(f"Количество пельменных автоматов: {dumpling_machines} шт.")

    print("\nII. Технологическая линия подготовки теста")
    print(f"Массовая доля теста: {dough_share:.2f} %")
    print(f"Производительность линии: {dough_capacity:.3f} т/ч")
    print(f"Количество тестомесильных машин: {mixers} шт.")

    print("\nIII. Технологическая линия подготовки фарша")
    print(f"Массовая доля фарша: {meat_share:.2f} %")
    print(f"Производительность линии: {meat_capacity:.3f} т/ч")
    print(f"Количество куттеров: {cutters} шт.")

    print("\n" + "=" * 55)
    print("Расчёт завершён.")
    print("=" * 55)


if __name__ == "__main__":
    main()

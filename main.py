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

if __name__ == "__main__":
    main()
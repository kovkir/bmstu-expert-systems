from items import Disjunct
from unification import Unification
from utils import create_disjunct


def resolve(
    resolving: Disjunct, 
    knowleadge: list[Disjunct], 
    max_counter = 1000
) -> Disjunct:
    resolving_flag = True
    while resolving_flag and max_counter > 0:
        resolving_flag = False

        for rule in knowleadge:
            print("-" * 64, "\n")
            print(f"Пара дизъюнктов:\n  1) {resolving}\n  2) {rule}\n")
            
            result = Unification.unificateDisjunct(
                left=resolving.copy(), 
                right=rule.copy(),
            )
            if result == None:
                print(f"Отсутствие унификаций\n")
                continue
            
            print(f"Подстановки: {result[1]}")
            print(f"Резольвента: {result[0]}\n")

            resolving = result[0]
            if len(resolving.args) != 0:
                resolving_flag = True

            max_counter -= 1
            break

    if max_counter == 0:
        print("Превышено максимальное число итераций\n")

    return resolving


def get_knowleadge() -> list[Disjunct]: 
    knowleadge = [
        " P2(x1, y1)|  P5(z1) | ~P6(w1)",
        " P3(C)     | ~P4(z2) |  P1(x2, y2, z2)",
        "~P2(A, B)  |  P5(x3) |  P6(y3)",
        " P4(x4)    | ~P3(x4)",
    ]
    return [create_disjunct(item) for item in knowleadge]


def main() -> None:
    """
    Процедура резолюции с унификацией 
    """
    print(
        "\nБаза знаний:\n", *get_knowleadge(), "", sep="\n",
    )
    result = resolve(
        resolving=create_disjunct("~P1(A, B, C)"),
        knowleadge=get_knowleadge(),
    )
    print("-" * 64, "\n")
    print(f"Рузультат резолюции: {result}\n")


if __name__ == "__main__":
    main()

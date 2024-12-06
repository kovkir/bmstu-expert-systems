from items import Disjunct
from unification import Unification
from utils import parse_disjunct


def resolve(resolving: Disjunct, knowleadge: list[Disjunct], max_counter = 1000):
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
            resolving_flag = True
            max_counter -= 1
            break
        
        if len(resolving.args) == 0:
            break
        
    if max_counter == 0:
        print("Превышено максимальное число итераций\n")

    return resolving


def get_knowleadge(): 
    return [
        parse_disjunct(" P2(x1, y1)|  P5(w1) | ~P6(z1)"),
        parse_disjunct(" P3(C)     | ~P4(z1) |  P1(x1, y1, z1)"),
        parse_disjunct("~P2(A, B)  |  P5(w2) |  P6(z2)"),
        parse_disjunct(" P4(z2)    | ~P3(z2)"),
    ]


def main() -> None:
    print("\nБаза знаний:\n", *get_knowleadge(), "", sep="\n")
    result = resolve(
        resolving=parse_disjunct("~P1(A, B, C)"),
        # resolving=parse_disjunct("P2(x1, y1)"),
        knowleadge=get_knowleadge(),
    )
    print("-" * 64, "\n")
    print(f"Итоговая резольвента: {result}\n")


if __name__ == "__main__":
    main()

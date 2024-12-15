from deduction import DirectDeduction
from utils import parse_atom, parse_knowleadge


def get_knowleadge(): 
    return parse_knowleadge(
        """
        O(N, M)
        M(M)
        A(W)
        E(N, A)
                                    
        W(y) & A(x) & S(x,y,z) & H(z) -> C(x)
        M(x_1) & O(N, x_1) -> S(W, x_1, N)
        M(x_2) -> W(x_2)
        E(x_3,A) -> H(x_3)
        """
    )


def main() -> None:
    """
    Прямая дедукция для определенных выражений методом поиска в ширину
    """
    deduction = DirectDeduction(
        knowleadge=get_knowleadge(), 
    )
    if deduction.knowleadge_prove(
        goal=parse_atom("C(W)"),
    ):
        print("\nЦель успешно доказана ✅\n")
    else:
        print("\nНе удалось доказать цель ❌\n")


if __name__ == "__main__":
    main()

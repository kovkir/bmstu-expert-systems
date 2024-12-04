from items import Term, Atom, Disjunct
from unification import Unification


def parse_disjunct(exp: str):
    atoms = [atom.strip() for atom in exp.split("|")]
    atom_list = []
    
    for atom in atoms:
        isPositive = atom[0] != '~'
        
        if not isPositive:
            atom = atom[1:].strip()

        atom_name, atom_args = atom.split('(')

        atom_name = atom_name.strip()
        atom_args = atom_args.split(')')[0].strip()

        atom_terms = [term.strip() for term in atom_args.split(',')]

        terms = [
            Term(
                name=term, 
                type="const" if term[0].capitalize() == term[0] else "var"
            ) for term in atom_terms        
        ]
        
        atom_list.append(Atom(atom_name, terms, isPositive))
    
    return Disjunct(atom_list)


def resolve(resolving: Disjunct, knowleadge: list[Disjunct], max_counter = 1000):
    resolvingCount = 1
    while resolvingCount > 0 and max_counter > 0:
        resolvingCount = 0

        for rule in knowleadge:
            result = Unification.unificateDisjunct(
                left=resolving.copy(), 
                right=rule.copy()
            )
            if result == None:
                continue

            print(f"{resolving} ~~~ {rule} ==== ({result[1]})\n ==> {result[0]}\n")

            resolving = result[0]
            resolvingCount += 1
            max_counter -= 1
            break
        
    if resolvingCount > 0:
        print("Tries out")

    return resolving


def get_knowleadge(): 
    return [
        parse_disjunct("L(Петя, Снег)"),
        parse_disjunct("L(Петя, Дождь)"),
        
        parse_disjunct("S(x1) | ~M(x1)"),
        parse_disjunct("S(x2) | M(x2)"),
        parse_disjunct("~M(x3) | ~L(x3, Дождь)"),
        parse_disjunct("~S(x4) | L(x4, Снег)"),
        parse_disjunct("~L(Лена, y1) | ~L(Петя, y1)"),
        parse_disjunct("~L(Лена, y2) | L(Петя, y2)"), 
    ]


def main() -> None:
    print(parse_disjunct('S(x4) | ~M(K)'), "\n")

    leftDisjunct = parse_disjunct("S(x1) | ~M(x1)")
    rightDisjunct = parse_disjunct("S(x2) | M(x2)")

    print(Unification.unificateDisjunct(
        left=leftDisjunct, 
        right=rightDisjunct
    ))

    print(*get_knowleadge(), "\n", sep="\n")
    print(resolve(
        resolving=parse_disjunct("L(Лена, Снег) | ~L(Лена, Футбол)"), 
        knowleadge=get_knowleadge()
    ))
    

if __name__ == "__main__":
    main()

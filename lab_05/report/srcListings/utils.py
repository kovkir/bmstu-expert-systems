from items import Term, Atom, Conjunct, Implication, Knowleadge


def parse_term(exp: str) -> Term:
    exp = exp.strip()
    if ':' in exp:
        name, type = [item.strip() for item in exp.split(':')]
        return Term(name, type)
    
    return Term(
        name=exp, 
        type="const" if exp[0].capitalize() == exp[0] else "var"
    )


def parse_atom(exp: str) -> Atom:
    exp = exp.strip()

    is_positive = exp[0] != '~'
    if not is_positive:
        exp = exp[1:].strip()

    atom_name, atom_args = exp.split('(')

    atom_name = atom_name.strip()
    atom_args = atom_args.split(')')[0].strip()

    atom_terms = [
        parse_term(term) for term in atom_args.split(',')
    ]
    
    return Atom(
        name=atom_name, 
        args=atom_terms, 
        isPositive=is_positive,
    )


def parse_conjunct(exp: str) -> Conjunct:
    exp = exp.strip()
    atoms = [
        parse_atom(atom) for atom in exp.split("&")
    ]

    return Conjunct(args=atoms)


def parse_implication(exp: str) -> Implication: 
    exp = exp.strip()
    left, right = exp.split("->")

    return Implication(
        left=parse_conjunct(left),
        right=parse_conjunct(right),
    )


def parse_knowleadge(exp: str) -> Knowleadge:
    data = []
    rules = []

    for string in exp.splitlines():
        string = string.strip()
        if not string:
            continue

        try:
            impl = parse_implication(string)
            rules.append(impl)
        except:
            atom = parse_atom(string)
            data.append(atom)

    return Knowleadge(
        data=Conjunct(args=data), 
        open_rules=rules,
    )
    
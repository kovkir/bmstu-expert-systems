from items import Term, Atom, Disjunct


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
        atom_terms = [
            term.strip() for term in atom_args.split(',')
        ]
        terms = [
            Term(
                name=term,
                type="const" if term[0].capitalize() == term[0] else "var"
            ) for term in atom_terms
        ]
        atom_list.append(Atom(atom_name, terms, isPositive))
    
    return Disjunct(atom_list)

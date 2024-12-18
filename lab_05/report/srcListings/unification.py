from items import Term, Atom


def add_substitution(substitions: dict, sub_key: str, term: Term) -> None:
    for key in substitions:
        if substitions[key].name == sub_key:
            substitions[key] = term

    substitions[sub_key] = term


def add_substitutions(
    dest_substitions: dict, 
    sourse_substitions: dict,
) -> None:
    for sub_key in sourse_substitions:
        add_substitution(
            substitions=dest_substitions, 
            sub_key=sub_key, 
            term=sourse_substitions[sub_key],
        )

        
def unificate_atoms(left: Atom, right: Atom) -> dict[str, Term] | None:
    if left.name != right.name or len(left.args) != len(right.args):
        return
    
    substitions = {}

    for i in range(len(left.args)):
        left_term = left.args[i]
        right_term = right.args[i]

        if left_term.type == "const" and right_term.type == "const":
            if left_term.value != right_term.value:
                return
            
        elif left_term.type == "var" and right_term.type == "const":
            add_substitution(substitions, left_term.name, right_term)

        elif left_term.type == "const" and right_term.type == "var":
            add_substitution(substitions, right_term.name, left_term)

        elif left_term.type == "var" and right_term.type == "var":
            if left_term.name != right_term.name:
                add_substitution(substitions, left_term.name, right_term)

    return substitions   


def apply_substitution(
    atoms_list: list[Atom], 
    substitutions: dict[str, Term],
) -> None:
    for atom in atoms_list:
        for term in atom.args:
            if term.name in substitutions:
                substitution_term = substitutions[term.name]

                term.name = substitution_term.name
                term.type = substitution_term.type
                
                if substitution_term.type == "const":
                    term.value = substitution_term.value

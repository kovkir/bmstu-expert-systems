from items import Atom, Disjunct, Term


class Unification:
    @classmethod
    def unificateDisjunct(cls, left: Disjunct, right: Disjunct):
        unificationCount = 0
        result = left.copy().args + right.copy().args
        globalSubstitutions = {}

        while True:
            localUnificationCount = 0

            for i, leftAtom in enumerate(result):
                for rightAtom in result[i + 1:]:
                    # Унификация возможна, только если имена атомов совпадают
                    if leftAtom.name == rightAtom.name:
                        if leftAtom.isPositive == rightAtom.isPositive:
                            substitutions = cls.__unificateAtoms(
                                left=leftAtom.copy(), 
                                right=rightAtom.copy()
                            )
                            # print(leftAtom, rightAtom, substitutions)
                            if substitutions != None and len(substitutions) == 0:
                                result.remove(rightAtom)
                                # localUnificationCount += 1
                            continue

                        substitutions = cls.__unificateAtoms(
                            left=leftAtom.copy(), 
                            right=rightAtom.copy()
                        )
                        if substitutions == None:
                            continue
                        
                        result.remove(leftAtom)
                        result.remove(rightAtom)
                        
                        for sub in substitutions:
                            globalSubstitutions[sub] = substitutions[sub]

                        cls.__applySubstitution(result, substitutions)

                        localUnificationCount += 1
                        break
            
            if localUnificationCount == 0:
                break

            unificationCount += localUnificationCount

        if unificationCount == 0:
            return None

        return Disjunct(result), globalSubstitutions

    @classmethod
    def __unificateAtoms(cls, left: Atom, right: Atom):
        if left.name != right.name:
            return
        if len(left.args) != len(right.args):
            return
        
        substitions = {}

        for i in range(len(left.args)):
            leftTerm = left.args[i]
            rightTerm = right.args[i]

            if leftTerm.type == "const" and rightTerm.type == "const":
                if leftTerm.value != rightTerm.value:
                    return

            elif leftTerm.type == "var" and rightTerm.type == "const":
                substitions[leftTerm.name] = rightTerm

            elif leftTerm.type == "const" and rightTerm.type == "var":
                substitions[rightTerm.name] = leftTerm

            elif leftTerm.type == "var" and rightTerm.type == "var":
                if leftTerm.name != rightTerm.name:
                    substitions[leftTerm.name] = rightTerm
            else:
                print("Ошибка\n")

        return substitions
    
    @classmethod
    def __applySubstitution(
        cls, 
        atomsList: list[Atom], 
        substitutions: dict[str, Term]
    ):
        for atom in atomsList:
            for term in atom.args:
                if term.name in substitutions:
                    substitution_term = substitutions[term.name]

                    term.name = substitution_term.name
                    term.type = substitution_term.type
                    
                    if substitution_term.type == "const":
                        term.value = substitution_term.value

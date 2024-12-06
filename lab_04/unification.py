from items import Atom, Disjunct, Term


class Unification:
    @classmethod
    def unificateDisjunct(
        cls, 
        left: Disjunct, 
        right: Disjunct
    ) -> tuple[Disjunct, dict[str, Term]] | None:
        unificationCount = 0
        result = left.copy().args + right.copy().args
        globalSubstitutions = {}

        while True:
            localUnificationCount = 0

            for i, leftAtom in enumerate(result):
                for rightAtom in result[i + 1:]:
                    if leftAtom.name == rightAtom.name:
                        if leftAtom.isPositive == rightAtom.isPositive:
                            cls.__deleteIdenticalAtom(
                                leftAtom=leftAtom,
                                rightAtom=rightAtom,
                                result=result,
                            )
                        elif cls.__tryToUnificateAtoms(
                            leftAtom=leftAtom,
                            rightAtom=rightAtom,
                            result=result,
                            globalSubstitutions=globalSubstitutions,
                        ):
                            localUnificationCount += 1
                            break
                            
            if localUnificationCount == 0:
                break

            unificationCount += localUnificationCount

        if unificationCount == 0:
            return None

        return Disjunct(result), globalSubstitutions

    @classmethod
    def __tryToUnificateAtoms(
        cls, 
        leftAtom: Atom,
        rightAtom: Atom,
        result: list[Atom],
        globalSubstitutions: dict[str, Term],
    ) -> bool:
        substitutions = cls.__unificateAtoms(
            left=leftAtom.copy(),
            right=rightAtom.copy(),
        )
        print(
            f"  Унификация предикатов:\n    {leftAtom}\n    {rightAtom}\n\n"\
            f"  Полученные подстановки: {substitutions}"
        )
        if substitutions == None:
            return False

        result.remove(leftAtom)
        result.remove(rightAtom)
        
        for sub in substitutions:
            globalSubstitutions[sub] = substitutions[sub]

        cls.__applySubstitution(result, substitutions)

        print(f"  Резольвента: {Disjunct(result)}\n")

        return True

    @classmethod
    def __unificateAtoms(
        cls, 
        left: Atom, 
        right: Atom,
    ) -> dict[str, Term] | None:
        if left.name != right.name or len(left.args) != len(right.args):
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
                    
        return substitions
    
    @classmethod
    def __applySubstitution(
        cls, 
        atomsList: list[Atom], 
        substitutions: dict[str, Term],
    ) -> None:
        for atom in atomsList:
            for term in atom.args:
                if term.name in substitutions:
                    substitution_term = substitutions[term.name]

                    term.name = substitution_term.name
                    term.type = substitution_term.type
                    
                    if substitution_term.type == "const":
                        term.value = substitution_term.value

    @classmethod
    def __deleteIdenticalAtom(
        cls,
        leftAtom: Atom,
        rightAtom: Atom,
        result: list[Atom],
    ) -> None:
        substitutions = cls.__unificateAtoms(
            left=leftAtom.copy(), 
            right=rightAtom.copy()
        )
        if substitutions != None and len(substitutions) == 0:
            result.remove(rightAtom)

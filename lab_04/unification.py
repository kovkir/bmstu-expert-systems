from items import Atom, Disjunct, Term


class Unification:
    @classmethod
    def unificateDisjunct(
        cls, 
        left: Disjunct, 
        right: Disjunct
    ) -> tuple[Disjunct, dict[str, Term]] | None:
        unificationCount = 0
        globalSubstitutions = {}
        
        leftAtoms = left.copy().args
        rightAtoms = right.copy().args

        while True:
            localUnificationCount = 0

            for leftAtom in leftAtoms:
                for rightAtom in rightAtoms:
                    if leftAtom.name == rightAtom.name:
                        if leftAtom.isPositive == rightAtom.isPositive:
                            cls.__deleteIdenticalAtom(
                                leftAtom=leftAtom,
                                rightAtom=rightAtom,
                                atomList=rightAtoms,
                            )
                        elif cls.__tryToUnificateAtoms(
                            leftAtom=leftAtom,
                            rightAtom=rightAtom,
                            leftAtoms=leftAtoms,
                            rightAtoms=rightAtoms,
                            globalSubstitutions=globalSubstitutions,
                        ):
                            localUnificationCount += 1
                            break
                            
            if localUnificationCount == 0:
                break

            unificationCount += localUnificationCount

        if unificationCount == 0:
            return None

        return Disjunct(leftAtoms + rightAtoms), globalSubstitutions

    @classmethod
    def __tryToUnificateAtoms(
        cls, 
        leftAtom: Atom,
        rightAtom: Atom,
        leftAtoms: list[Atom],
        rightAtoms: list[Atom],
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

        # удаление контрарных атомов
        leftAtoms.remove(leftAtom)
        rightAtoms.remove(rightAtom)
        
        for sub in substitutions:
            globalSubstitutions[sub] = substitutions[sub]

        cls.__applySubstitution(leftAtoms, substitutions)
        cls.__applySubstitution(rightAtoms, substitutions)

        print(f"  Резольвента: {Disjunct(leftAtoms + rightAtoms)}\n")

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
        atomList: list[Atom],
    ) -> None:
        substitutions = cls.__unificateAtoms(
            left=leftAtom.copy(), 
            right=rightAtom.copy()
        )
        if substitutions != None and len(substitutions) == 0:
            atomList.remove(rightAtom)

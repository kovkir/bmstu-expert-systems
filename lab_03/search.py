from items import Rule, Node, Label
from stack import Stack


class Search:
    """
    Обратный поиск в глубину от цели
    """
    def __init__(self, rule_arr: list[Rule]):
        self.rule_arr = rule_arr  # база знаний
        self.open_node_st = Stack()
        self.open_rule_lst = []
        self.close_node_lst = []
        self.close_rule_lst = []
        self.prohibited_node_lst = []
        self.prohibited_rule_lst = []

        self.goal_node = None
        self.solution_flg = False
        self.no_solution_flg = False

    def run(self, goal_node: Node, in_node_arr: list[Node]):
        self.goal_node = goal_node
        self.open_node_st.push(goal_node)
        self.close_node_lst = in_node_arr

        while not self.solution_flg and not self.no_solution_flg:
            rule_cnt = self.child_search()

            if self.solution_flg:
                print(f'\nРешение было найдено ✅\n')
                return

            if rule_cnt == 0 and self.open_node_st.length() < 2:
                self.no_solution_flg = True
                print("\nРешение не было найдено ❌\n")
            elif rule_cnt == 0:
                print("\nВозвращение назад:")
                self.backtracking()

    def child_search(self):
        cnt_rules = 0

        for rule in self.rule_arr:
            current_node = self.open_node_st.peek()
            print(f'\nТекущее правило: {rule.number}')
            print(f'Текущая вершина: {current_node.number}')

            if rule.label != Label.OPEN:
                print(f'Правило уже было обработано\n\n{'—' * 64}')
                continue

            if rule.out_node == current_node:
                print(f'Выходная вершина правила равна текущей вершине')

                rule.label = Label.VIEWED
                self.open_rule_lst.append(rule)

                is_new_goal_added = self.add_new_goal(rule.node_arr)
                if not is_new_goal_added:
                    print(f'Все входные вершина правила являются закрытыми')
                    print('\nМаркировка:')
                    self.label()

                cnt_rules += 1
                self.print_info()
                break

            if self.is_prohibited_node_exist(rule.node_arr):
                print(f'Среди входных вершин правила есть запрещенная')
                self.prohibited_rule_lst.append(rule)
                rule.label = Label.FORBIDDEN

                self.print_info()
                continue

            self.print_info()

        return cnt_rules

    def label(self):
        while True:
            rule = self.open_rule_lst.pop()
            self.close_rule_lst.append(rule)

            node = self.open_node_st.pop()
            self.close_node_lst.append(node)

            print('    Правило {:3d} -> список закрытых правил'.format(rule.number))
            print('    Вершина {:3d} -> список закрытых вершин'.format(node.number))

            if node == self.goal_node:
                self.solution_flg = True
                break

            current_node = self.open_node_st.peek()
            current_rule = self.open_rule_lst[-1]
            if current_rule.out_node != current_node:
                break

    def backtracking(self):
        current_goal = self.open_node_st.pop()
        rule = self.open_rule_lst.pop()

        current_goal.flag = Label.FORBIDDEN
        self.prohibited_node_lst.append(current_goal)

        rule.label = Label.FORBIDDEN
        self.prohibited_rule_lst.append(rule)

        print('    Правило {:3d} -> список запрещенных правил'.format(rule.number))
        print('    Вершина {:3d} -> список запрещенных вершин'.format(current_goal.number))

        for node in rule.node_arr:
            print('    Вершина {:3d} должна быть удалена из стека открытых вершин'.format(node.number))
            self.open_node_st.remove_element(node)

        print('\n' + '—' * 64)

    def add_new_goal(self, node_arr: list[Node]):
        new_goal_flg = False

        for node in node_arr[::-1]:
            if node not in self.close_node_lst:
                self.open_node_st.push(node)
                new_goal_flg = True

        return new_goal_flg

    def is_prohibited_node_exist(self, node_arr: list[Node]):
        for node in node_arr:
            if node in self.prohibited_node_lst:
                return True
            
        return False

    def print_info(self):
        print('\nСтек открытых вершин:      ', end='')
        self.open_node_st.show()
        print('Список закрытых вершин:    ', end='')
        self.print_nodes(self.close_node_lst)
        print('Список запрещенных вершин: ', end='')
        self.print_nodes(self.prohibited_node_lst)

        print('Список открытых правил:    ', end='')
        self.print_rules(self.open_rule_lst)
        print('Список доказанных правил:  ', end='')
        self.print_rules(self.close_rule_lst)
        print('Список запрещенных правил: ', end='')
        self.print_rules(self.prohibited_rule_lst)

        print('\n' + '—' * 64)
    
    def print_nodes(self, node_arr: list[Node]):
        for node in node_arr:
            print(node, end=' ')
        print()

    def print_rules(self, rule_arr: list[Rule]):
        for rule in rule_arr:
            print(rule.number, end=' ')
        print()

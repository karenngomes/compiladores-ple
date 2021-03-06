from semanthicanalyzer.states import StatesChain, ExpressionChain
from syntaticanalyzer import JumpIndex
from scope import BEGIN_ENTRY_NAME, END_ENTRY_NAME
from semanthicanalyzer.Semanthic import Semanthic

class RoutineChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self.__begin, **kwargs)
        self.scope = None
        self.jump = JumpIndex()
        self.parameter_list = []
        self.parameter_index = 0

    def __begin(self, token):
        self.state = self.__resolve_parameters
        current_scope_name = self.scope_manager.get_stack_top_name()

        if current_scope_name.split('-')[-1] == token[0]:
            scope_name = current_scope_name
        else:
            scope_name = current_scope_name + '-' + token[0]

        self.scope = self.scope_manager[scope_name].copy() # copia o escopo antes de salvar na pilha
                                                           # tem que fechar antes do programa acabar
        self.jump.small_jump_index = self.scope[BEGIN_ENTRY_NAME].value[0]
        self.jump.big_jump_index = self.scope[END_ENTRY_NAME].value[0]
        self.__get_parameters_in_scope()

    def __sort_parameter_list(self, entry):
        return int(entry.category.split('parameter')[1])

    def __get_parameters_in_scope(self):
        for entry in self.scope.items.values():
            if entry.category.startswith('parameter'):
                self.parameter_list.append(entry)
        self.parameter_list.sort(key=self.__sort_parameter_list)

    def __resolve_parameters(self, token):
        if token[0]  == '(' or token[0] == ',':
            return
        elif token[1] != 'id' and token[1] != 'intnum': # )
            self.scope_manager.push_in_stack(self.scope)
            self.__check_args_quantity()
            self.__call()
        else: # passando argumentos
            self.__pass_args()

    def __pass_args(self):
        index = self.parameter_index
        self.parameter_index += 1
        entry_value = ExpressionChain(self.scope_manager,
                                      self.token_list,
                                      self.index).exec()
        try:
            self.__arg_type_validation(self.parameter_list[index],
                                    entry_value)
        except IndexError:
            qt_expected = len(self.parameter_list)
            raise Exception(f'Routine {self.scope.scope_name} expected {qt_expected} arguments.')


    def __check_args_quantity(self):
        qt_expected = len(self.parameter_list)
        if qt_expected != self.parameter_index:
            raise Exception(f'Routine {self.scope.scope_name} expected {qt_expected} arguments.')

    def __arg_type_validation(self, param, entry_value):
        if param.type == "boolean" and isinstance(entry_value, bool):
            param.value = entry_value
        elif param.type == "integer" and not isinstance(entry_value, bool):
            param.value = entry_value
        else:
            raise Exception(f'Invalid argument type: parameter {param.lexema} is a {param.type}.')

    def __call(self):
        sem = Semanthic(self.token_list, self.scope_manager,
                        begin=self.jump.small_jump_index,
                        end=self.jump.big_jump_index).analyze()
        self.scope_manager.pop_stack()
        self._finalize()
        return

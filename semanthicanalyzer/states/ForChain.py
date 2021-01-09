from semanthicanalyzer.states import StatesChain, AttributionChain, ExpressionChain
from syntaticanalyzer import TOKEN_POS_INDEX, JumpIndex


class ForChain(StatesChain):
    """
    for <id> := <expressao> to <expressao> do 
        begin 
        <sentencas> 
        end

    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, state=self._begin, **kwargs)
        self.jump_index = None # define para onde o código irá pular depois
        self.was_declared_now = False # mantem controle se já passamos no loop antes
        self.loop_variable = None # variavel inicializada no loop
    
    def _begin(self, token):
        if token[0] == "for":
            self.state = self._attribution
            self.jump_index = token[TOKEN_POS_INDEX] # recupera o JumpIndex do for
        else: # "to"
            self.state = self._solve_condition
            self.jump_index = token[TOKEN_POS_INDEX] # recupera o JumpIndex do to
            
            loop_variable_index = self.jump_index.small_jump_index # recupera o token da variavel
            loop_variable_token = self.token_list[loop_variable_index] 
            self.loop_variable = self.scope_manager.search_identifier(loop_variable_token[0])
            #print(self.loop_variable)

    def _attribution(self, token):
        self.loop_variable = self.scope_manager.search_identifier(token[0])
        #print(self.loop_variable)
        AttributionChain(self.scope_manager, self.token_list,
                                self.index).exec()
        self.state = self._solve_condition
        self.was_declared_now = True
        
    def _solve_condition(self, token):
        if token[0] == 'to' and self.was_declared_now: # se a variavel foi declarada nessa execucao
            end_index = self.jump_index.big_jump_index - 1 
            for_index = self.jump_index.small_jump_index
            
            jump = JumpIndex(small_jump=for_index + 1,
                                big_jump=end_index + 1, #indice do end do for
                                jump_big=True)
            token.append(jump)
            self.token_list[end_index][TOKEN_POS_INDEX].big_jump_index = self.index[0]
            return

        exp_value = ExpressionChain(self.scope_manager, self.token_list,
                                self.index).exec()

        if self.loop_variable.value <= exp_value: # se a condicao for respeitada
            self.jump_index.jump_big = False # nao pula mais pro end
            self.index[0] += 2 # pula para o begin depois da condição
        else:
            self.jump_index.jump_big = True
            #print(self.jump_index.big_jump_index)
            self.index[0] = self.jump_index.big_jump_index # pula para o token depois do seu par "end"
                                                        # essa alteração é feita no JumpMaker.
        
        self.loop_variable.value += 1
        self._finalize()
        return

class ConditionChain(StatesChain):
    def __init__(self, *args, **kwargs):
        super.__init__(self, args, kwargs)
        self.accumulated_value = None
        self.operator = None

    def __begin(self, token):
        if (token[1] == "id" and token[1] == "integer") or token[1] == "intnum"
            

        """
        if num ou id seguido de operator
            goto ExpressionChain then goto operator then goto ExpressionChain then return true or false
            podemos pensar como 3 falsos estados da maquina
            1 - ExpressionChain
            valor = ExpressionChain()
            2 - le o operador e se prepara para resolver
            3 - ExpressionChain e resolve a desigualdade, parecido com o ExpressionChain só que dessa vez os operadores sao > < = etc
        elif boolean2(not) ou id seguido de boolean1(and ou or)
            goto BoolExpressionChain
        """

    def expression(self, index):
        exp_chain = ExpressionChain(self.scope_manager)
        while True:
            first_value = exp_chain.run(tokens[index])
            if exp_chain.has_done(): break
            index += 1
        index += 1
        if tokens[index][1] == "operator":
            operator = tokens[index][0]
            exp_chain = ExpressionChain(self.scope_manager)
            while True:
                second_value = exp_chain.run(tokens[index])
                if exp_chain.has_done(): break
                index += 1
            


        return value
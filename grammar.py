# Grammar Lib
class Grammar:
  # Initial grammar
  op = ['+', '-', '/', '*']
  #op = [['sin(', 'exp', ')'], '*']
  exp = [['exp', 'op', 'exp'], ['sin(', 'exp', ')'], ['cos(', 'exp', ')'], ['sqrt(', 'exp', ')'], 'var']
  expWeight = [40, 5, 5, 10, 40]
  var = []

  def symbolReplacement(self, expression, symbol, position):
    if not isinstance(symbol, list):
      expression[position] = symbol
    else:
      expression[position] = symbol[0]
      k = 1
      for element in symbol[1:]:
        expression.insert(position + k, element)
        k = k + 1

  def setVariables(self, variables):
    self.var = variables

  def cromossomeToExpression(self, cromossome):
    expression = ['exp']
    i = 0
    i_max = 100
    k = 0
    while(i < len(expression)):
      if(expression[i] == 'exp' or expression[i] == 'var' or expression[i] == 'op'):
        if(expression[i] == 'exp'):
          if(i < i_max):
            newSymbol = self.exp[cromossome[k] % len(self.exp)]
          else:
            newSymbol = self.exp[-1]

        elif(expression[i] == 'op'):
          newSymbol = self.op[cromossome[k] % len(self.op)]

        elif(expression[i] == 'var'):
          newSymbol = self.var[cromossome[k] % len(self.var)]

        self.symbolReplacement(expression, newSymbol, i)
        k = k + 1
        k = k % len(cromossome)

      else:
        i = i + 1
    
    if(i == i_max):
      expression = "NaN"
    else:
      expression = "".join(expression)
    return expression
# Vinicius Pinhatari Souza Campos - 34706 - ELT - Unifei
# Biblioteca fuzzy usada: Fuzzy logic toolkit for SciPy "https://pythonhosted.org/scikit-fuzzy/".  
# requirements.txt => scikit-fuzzy==0.4.0
import math
import numpy as np
import skfuzzy as fuzzy
from skfuzzy import control as ctrl

t_externa = ctrl.Antecedent(np.arange(-10, 31, 1), 't_externa')
# Os valores de -25 a 125, foram pensados para uma melhor aproximaçao da centroide, e resultadso mais precisos de TA
i_aquecedor = ctrl.Consequent(np.arange(-25, 126, 1), 'i_aquecedor')

#funçoes de pertinencia da entrada temperatura externa
t_externa['fria'] = fuzzy.trimf(t_externa.universe, [-10,-10,10])
t_externa['morna'] = fuzzy.trimf(t_externa.universe, [-10, 10, 30])
t_externa['quente'] = fuzzy.trimf(t_externa.universe, [10, 30,30])

#funçoes de pertinencia da saida Intensidade do aquecedor
i_aquecedor['fraco'] = fuzzy.trimf(i_aquecedor.universe, [-25,-25,50])
i_aquecedor['medio'] = fuzzy.trimf(i_aquecedor.universe, [20, 50, 80])
i_aquecedor['intenso'] = fuzzy.trimf(i_aquecedor.universe, [50, 125, 125])

#definiçao das regras
regra1 = ctrl.Rule(t_externa['fria'], i_aquecedor['intenso'])
regra2 = ctrl.Rule(t_externa['morna'], i_aquecedor['medio'])
regra3 = ctrl.Rule(t_externa['quente'], i_aquecedor['fraco'])

#controle e simulaçao
controle = ctrl.ControlSystem([regra1, regra2, regra3])
a = ctrl.ControlSystemSimulation(controle)

for i in range(-5,26):
  # Entrada da temperatura externa 
  te = a.input['t_externa'] = i

  # Output intensidade do aquecedor
  a.compute()
  ia = a.output['i_aquecedor']

  # Formula de simulação
  matricula = 34706
  ta = te + ia/2.7 + 5*abs(math.sin(matricula/500)) 

  # Definir duas casas após a virgula para melhor visualização
  ia_arred = round(ia,2)
  ta_arred = round(ta,2)

  # Visualização da Temperatura externa; Intensidade; Temperatura Agua.
  print ('\nTE = %i°c'%te,'   IA = %i%%' %ia_arred,'   TA =',ta_arred)
 

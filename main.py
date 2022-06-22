import numpy as np
#creamos la clase pereceptron
class Perceptron():
  def __init__(self,inputs,weights):
    self.inputs=np.array(inputs)
    self.weights=np.array(inputs)
 

  def decide(self,treshold):
    total=0
    
    for input_,weight_ in zip(self.inputs,self.weights):
      total+=input_*weight_  
    if total>=treshold:
      valor=True
    else:
      valor=False
    print(valor)
    return valor
inputs,weights=[],[]

preguntas=[
  "¿cual es la velocidad?.. ",
  "¿ritmo cardiaco?.. ",
  "respiracion.. "
]

for pregunta in preguntas:
  i=int(input(pregunta))
  w=int(input("y sus peso asociado es... "))
  inputs.append(i)
  weights.append(w)
  print()
treshold=int(input("y nuestro umbral/limite sera: ")) 


p=Perceptron(inputs,weights)
print(p.decide(treshold))
import numpy as np
#creamos la clase pereceptron
class Perceptron():
  def __init__(self,inputs,weights):
    self.inputs=np.array(inputs)
    self.weights=np.array(inputs)
 

  def  decide(self,treshold):
    total=0
    for input_,weight_ in zip(self.inputs,self.weights):
      total+=input_*weight_

    if total>=treshold:
      valor=True
    else:
      valor=False
    return valor
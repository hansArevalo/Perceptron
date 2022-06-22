inputs,weights=[],[]

preguntas=[
  "¿cual es la velocidad?",
  "¿ritmo cardiaco?",
  "respiracion"
]

for pregunta in preguntas:
  i=int(input(pregunta))
  w=int(input("y sus peso asociado es..."))
  inputs.append(i)
  weights.append(w)
  print()
treshold=int(input("y nuestro umbral/limite sera")) 
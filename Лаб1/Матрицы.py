#Вариант 11

import numpy as np
matrix  = np.array([[5, 9, 7, 7, 8],[12,  8, 10,  6, 11],[12,  8, 10,  6, 11], [8,  7, 0,  4, 10]])
q=[0.0, 0.0, 0.43, 0.57, 0.0]
p=[0.0, 0.0, 0.71, 0.29, 0.0]
answer = {}
lower_price = max([min(x) for x in matrix])
upper_price = min([max(x) for x in np.rot90(matrix)])
if lower_price==upper_price:print("седловая точка есть", f"ответ v={lower_price}")
else:
  buff=0
  for i,pin in zip(matrix,p):
    buff+=pin*sum([x*y for x,y in zip(i,q)])
  answer["H(P,Q)"]=buff
  for k, i  in enumerate(np.rot90(matrix),1):
    answer["H(P,B{})".format(k)]=sum([x*y for x,y in zip(i,p)])
for i in [(x,y) for x,y in answer.items()]:
  print("Ответ выйгрыш игрока А в ситуации {0[0]} = {0[1]}".format(i))
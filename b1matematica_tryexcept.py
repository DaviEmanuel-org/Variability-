conta=0
lista=[]
diferenças=[]
desvios=[]
diferenças_ao2=[]
print(f'Coloque os numeros que serão calculados\nQuando terminar apenas aperte "enter" ')
while True:
  try:
    lista.append(float(input('Numero: ')))
    conta+=1
  except ValueError:
    break
media=(sum(lista)/conta)
for o in lista:
    dif=o-media
    diferenças.append(dif)
    if dif<0:
        des=dif*-1
    else:
        des=dif
    desvios.append(des)
    dif_2=dif**2
    diferenças_ao2.append(dif_2)
Var=sum(diferenças_ao2)/conta
DM=sum(desvios)/conta
DP=Var**0.5
print(f'\033[32mDM: {DM:.2f}, Var: {Var:.2f}, DP: {DP:.2f}, Media: {media:.2f}\033[0m\n')
print('Números / Diferenças / Desvio / Diferença^2')
for i in range(conta): 
  print(f'{lista[i]}    {diferenças[i]:.2f}    {desvios[i]:.2f}      {diferenças_ao2[i]:.2f}')
print(f'Soma:   {sum(diferenças):.2f}   {sum(desvios):.2f}       {sum(diferenças_ao2):.2f}')
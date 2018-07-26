

multy = 0
fn1 = 1
fn2 = 0

while multy < 80:
    fn = fn1 + fn2
    fn1 = fn2
    fn2 = fn
    multy += 1

    listDivs = [1, 1]
    evaluar = fn

    for div in (9,8,7,6,5,4,3,2,1):
        if evaluar % div == 0: 
            listDivs.append(div)
            evaluar = evaluar / div  

            numero = (sum(listDivs)*sum(listDivs))
            if numero >= 1000:
                print "El Numero de la serie es: {}, \ty tiene {} divisores ".format(fn, numero)

#lo hice asi oporque si lo hacia recorriendo cada numero estaba mucho tiempo evaluando xD 
# y los recursos son escsasos xD

#se usa la logica de descomposision del numero 

# 498454011879264

""" El Numero de la serie es: 4807526976, 	y tiene 1024 divisores 
El Numero de la serie es: 4807526976, 	y tiene 1089 divisores 
El Numero de la serie es: 498454011879264, 	y tiene 1024 divisores 
El Numero de la serie es: 498454011879264, 	y tiene 1156 divisores 
El Numero de la serie es: 498454011879264, 	y tiene 1225 divisores 
El Numero de la serie es: 51680708854858323072, 	y tiene 1024 divisores 
El Numero de la serie es: 51680708854858323072, 	y tiene 1089 divisores  """

'''Meseros virtuales'''

print("¡Bienvenid@ a Mamá Juana!")

#variables
n_pizzas=int(input("Ingrese la cantidad de pizzas a ordenar: "))
pizza_c=1
precio_total=0

while(pizza_c<=n_pizzas):
    print(f"Ingrese los ingredientes para la pizza", {pizza_c})
    print("Lista de Ingredientes:")
    print("1. Tomate")
    print("2. Piña")
    print("3. Pepperoni")
    print("4. Aceitunas")
    n_ingrediente=int(input("Ingrese la cantidad de ingredientes para su pizza: "))
    ingrediente_c=1
    v_ingrediente=0

    while(ingrediente_c<=n_ingrediente):
        ingrediente=int(input(f"Ingrese ingrediente {ingrediente_c}:"))
        if(ingrediente==1):
            tomate=300
            v_ingrediente=tomate+v_ingrediente

        elif(ingrediente==2):
            piña=500
            v_ingrediente=piña+v_ingrediente

        elif(ingrediente==3):
            pepperoni=400
            v_ingrediente=pepperoni+v_ingrediente

        elif(ingrediente==4):
            aceitunas=600
            v_ingrediente=aceitunas+v_ingrediente

        else:
            print("Ingrese una opción válida")
        ingrediente_c=ingrediente_c+1
        pizza_sub=v_ingrediente+1000
    print("Subtotal:$", pizza_sub)
    pizza_c=pizza_c+1
    precio_total=precio_total+pizza_sub
print("El total a pagar es $", precio_total)
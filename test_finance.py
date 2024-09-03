# creamos el menú
def main():
    #creamos un diccionario para almacenar las cuentas
    accounts=[]
    
    while True:
        print("Bienvenido a la calculadora de Finanzas")
        print("1. Crear cuenta")
        print("2. Agregar transaccion")
        print("3. Consultar saldo de la cuenta")
        print("4. Consultar el saldo total")
        print("5. Salir")
        #capturar la opcion
        opcion= input("Ingrese la opción deseada: ")
        #Creacion de la cuenta
        if option ==1:
            name=input("Ingrese el nombre de la cuenta")
            account_type= input("Ingrese el tipo de cuenta")
            account_id= create_account(accounts, name, account_type)
            print(f"Cuenta {name} creada con el id {account_id}")
        #Agregar transaccion
        elif opcion ==2:
            account_id=int(input("Ingrese el id de la cuenta: "))
            amount=float(input("Ingrese el monto de la transacción: "))
            description= input("Ingrese la descripción de la transacción: ")
            add_transaction(accounts, account_id, amount)
            print(f"Transacción de {amount} realizada en la cuenta {account_id}")
        
        #Consultar saldo de la cuenta
        elif opcion==3:
            account_id=int(input("Ingrese el Id de la cuenta: "))
            balance =get_account_balance(accounts, account_id)
            print(f"El saldo de la cuenta {account_id} es: {balance}")
            
        #Consultar el saldo total almacenado
        elif opcion==4:
            total_balance=get_total_balance(accounts)
            print(f"El saldo total de la cuneta es: {total_balance}")
        
        #salir del programa
        elif opcion==5:
            print("¡Gracias por usar la calculadora!")
            #salimos del ciclo
            break
            
        #opcion invalida
        else:
            print("Opción invalida, intente de nuevo")
            
if __name__== "__main__":
    main()

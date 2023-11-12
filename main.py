
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numero=int(input("Number to look for their dividers:"))
    for i in range(1,numero+1):
        if numero%i == 0:
            print(str(i)+" es divisor de "+str(numero))

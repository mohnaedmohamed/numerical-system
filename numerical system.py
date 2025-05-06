#from octal to decimal
def octal_decimal(k):
 l=[]     
 l.append(k)
 result=list(map(int,str(l[0]))) 
 result.reverse()
 for i in range(len(result)):
                result[i]=result[i]*8**i  
                x=sum(result)
 return x 
#from decimal to binary
def decimal_binary(k):
    result = []
    while k > 0:
        result.append(str(k % 2))
        k = k // 2
    result.reverse()
    binary = ''.join(result)
    return binary
#from binary to decimal 
def binary_decimal(k):
 l=[]     
 l.append(k)
 result=list(map(int,str(l[0]))) 
 result.reverse()
 for i in range(len(result)):
              if result[i]==1:
                result[i]=2**i  
                x=sum(result)
              else:
                     result[i]=0     
 return x
#from octal_binary
def octal_binary(k):
       z=octal_decimal(k) 
       decimal_binary(z) 
       return z
#from decimal to octal 
def decimal_octal(k):
    result=[]
    while k>0:
        d=k%8
        result.append(d)
        k=k//8  
    result.reverse()
    result = ''.join(map(str, result))
    return result
#from binary to octal
def binary_octal(k):                      
         z=binary_decimal(k)
         h=decimal_octal(z)
         return h
#from decimal to hexadecimal
def decimal_hexadecimal(k):
    result=[]
    while k>0:
        d=k%16
        result.append(d)
        k=k//16  
    result.reverse()
    for i in range(len(result)):
        if result[i]==10:
            result[i]='A'
        elif result[i]==11:
            result[i]='B'
        elif result[i]==12:
            result[i]='C'
        elif result[i]==13:
            result[i]='D'
        elif result[i]==14:
            result[i]='E'
        elif result[i]==15:
            result[i]='F'

    result = ''.join(map(str, result))
    return result
 #from binary to hexadecimal
def binary_hexadecimal(k):                      
         z=binary_decimal(k)
         h=decimal_hexadecimal(z)
         return h
#from octal to hexadecimal
def octal_hexadecimal(k):                      
         z=octal_decimal(k) 
         h=decimal_hexadecimal(z)
         return h
def hexadecimal_decimal(k):
    k = k.upper()[::-1]
    result = []
    for i in range(len(k)):
        if k[i] == 'A':
            val = 10
        elif k[i] == 'B':
            val = 11
        elif k[i] == 'C':
            val = 12
        elif k[i] == 'D':
            val = 13
        elif k[i] == 'E':
            val = 14
        elif k[i] == 'F':
            val = 15
        else:
            val = int(k[i])
        result.append(val * (16 ** i))
    x = sum(result)
    return x
def hexadecimal_octal(k):
    z=hexadecimal_decimal(k)
    h=decimal_octal(z)
    return h
def hexadecimal_binary(k):                 
         z=hexadecimal_decimal(k)
         h=decimal_binary(z)
         return h
choice=0
def main():
    print("welcome to the number conversion program")
    print("Choose the conversion you want to perform:")
    print("1. Decimal to Octal")
    print("2. Decimal to Binary")
    print("3. Decimal to Hexadecimal")
    print("4. Octal to Decimal")
    print("5. Octal to Binary")
    print("6. Octal to Hexadecimal")
    print("7. Binary to Decimal")
    print("8. Binary to Octal")
    print("9. Binary to Hexadecimal")
    print("10. Hexadecimal to Decimal")
    print("11. Hexadecimal to Octal")
    print("12. Hexadecimal to Binary")
   
    choice = int(input("Enter your choice: "))
    if choice == 1:
          k=int(input("Enter a decimal number: "))
          q=decimal_octal(k)
          print(q)
    if choice == 2:
          k=int(input("Enter a decimal number: "))
          q=decimal_binary(k) 
          print(q)

    if choice == 3:
          k=int(input("Enter a decimal number: "))
          q=decimal_hexadecimal(k)
          print(q)

    if choice == 4:
          k=int(input("Enter a octal number: "))
          q=octal_decimal(k) 
          print(q) 
    if choice == 5:
          k=int(input("Enter a octal number: "))
          q=octal_binary(k)
          print(q)
    if choice == 6:
          k=int(input("Enter a octal number: "))
          q=octal_hexadecimal(k)
          print(q)
    if choice == 7:
          k=int(input("Enter a binary number: "))
          q=binary_decimal(k)
          print(q)
    if choice == 8:
          k=int(input("Enter a binary number: "))
          q=binary_octal(k)
          print(q)    
    if choice == 9:     
          k=int(input("Enter a binary number: "))
          q=binary_hexadecimal(k)
          print(q)
    if choice == 10:
          k=input("Enter a hexadecimal number: ")
          q=hexadecimal_decimal(k)
          print(q)
    if choice == 11:
          k=input("Enter a hexadecimal number: ")
          q=hexadecimal_octal(k)
          print(q)
    if choice == 12:
            k=input("Enter a hexadecimal number: ")
            q=hexadecimal_binary(k)
            print(q)
    if choice > 12:
            print("Invalid choice!")
            return None

while choice <= 12:
    main()  
    print("\nDo you want to perform another conversion? (yes/no)")
    again = input().lower()
    if again != 'yes':
        break
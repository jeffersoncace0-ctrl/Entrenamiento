print("SALES  RECORD")

#Registro del usuario
name_customer = input ("Name of customer: ")
price_unit = float(input("Enter the unit price of product: "))
amount = float(input("Enter the amount of products purchased: "))
membership_vip = input ("The customer has VIP membership? (yes/no) ").lower()

#Sub total de la venta 
subtotal = price_unit * amount 

#Para aplicar el descuento (si aplica el cliente)
discount = 0
if membership_vip =="si":
   discount = subtotal * 0.10

#Resultado final
total_final = subtotal - discount

#Informacion final 
print ("----- RECEIPT-----")
print(f"customer: {name_customer}")
print(f"subtotal: ${subtotal:.2f}")
print(f"discount applied: ${discount:.2f}")
print(f"total to pay: $ {total_final:.2f} ")


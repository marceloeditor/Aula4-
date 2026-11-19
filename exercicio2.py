print (""" nota final de aprovação """)

nota1 = float(input( "digite sua primeira nota : "))
nota2 = float(input(" digite sua segunda nota : " ))

media = (nota1 + nota2) /2 

if media >= 6 :
    print (f"sua média foi {media} ,entao você foi aprovado" )

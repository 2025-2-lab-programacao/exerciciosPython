# a função print concatena strings com espaço entre elas
print("Pelouro","Ihago","Ihan")

a = "meu pé de laranja lima"

a = a.replace("laranja", "maça vermelha")

print(a)

print(a.startswith("meu"))
print(a.startswith("oLÁ"))
print(a.endswith("mundo"))
print(a.endswith("lima"))

# transformar a primeira letra de toda string em maiuscula
print(a.capitalize())

# se só possui números

print(f"só possui números?" )
print( "12345".isdigit() )
print(a.isdigit())

# se é alfanumerica (só possui letras e números)
print(f"é só letra e numero?")
print('123abc'.isalnum())
print('123ab.c'.isalnum())
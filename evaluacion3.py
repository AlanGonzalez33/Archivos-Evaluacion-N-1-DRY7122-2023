acl = int(input("ingrese su numero de ACL IPV4: "))

if acl >= 1 and acl <= 99:
    print("su ACL es Estandar")
elif acl >= 100 and acl <= 199:
    print("su ACL es Extendida")

else:
    print ("su dato no es ACL numerada")

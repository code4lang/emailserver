usuario=[0]
contraseña=[0]
texto=[0]
titulo=[0]
email=[0]
p=0

r1=0
while 1:
    e=0
    r=0
    print ("1 for log in, 2 for log on")
    while r!=1 and r!=2:
        r=input("?")
        r=int(r)
    if r==1:
        a=input("nombre de usuario?")
        b=input("contraseña?")
        usuario.append(a)
        contraseña.append(b)
    else:
        e=len(usuario)
        while e==len(usuario):
            e=0
            a=input("nombre de usuario?") 
            for i in range (len(usuario)):
                if a !=usuario[i]:
                    e=e+1    
        b=input("contraseña?")
        for i in range (len(usuario)):
            if a==usuario[i]:
               p=i
        while b!=contraseña[p]:
            print("contraseña incorecta")
            b=input("contraseña?")
    print ("que quieres hacer? 1 para texto,2 para archivos,3 para mail")
    r=input("?")
    r=int(r)
    if r==1:
        r=input("1 para nuevo, 2 para abrir texto")
        r=int(r)
        if r==1:
            t=input("titulo?")
            titulo.append(t)
            text=input("escriba lo que quiera.")
            texto.append(text)
        else:
            t=input("titulo?")
            for i in range (len(titulo)):
                if t==titulo[i]:
                    p=i
            print (texto[p])
    if r==2:
        r=input("que quiere abrir?")
        open(r)
    if r==3:
        r=input("1 para enviar, 2 para recibir")
        r=int(r)
        if r==1:
            p=-1
            while not (0<p<len(usuario)):
                destinatario=input("destinatario?")
                for i in range (len(usuario)):
                    if destinatario==usuario[i]:
                        p=i
            mail=input("mensage?")
            mail="enviado por",a,               mail
            email.append(mail)
        else:
            print (email[p])

        
        

        

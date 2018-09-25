#! /usr/bin/python3
#-*- coding utf-8 -*-
import subprocess

"""
1. Pedir el numero de host virtuales
2. Pedir nombre de la carpeta de archivos
3. Crear carpeta en la ruta sudo mkdir -p /var/www/{variable nombre}/public_html
4. Darle permisos sudo chown -R $USER:$USER /var/www/example.com/public_html
5. Darle permisos de lectura sudo chmod -R 755 /var/www
6. Crear el index nano /var/www/example.com/public_html/index.html

7. Crear archivo de configuracion virtualHost sudo nano /etc/apache2/sites-available/example.com.conf
8. Avilitar los archivos virtualHost sudo a2ensite example.com.conf
"""
numVH = int(input("Numeros de Host Virtuales: "))


def newVH(nameVH):
    user = subprocess.run("whoami", stdout=subprocess.PIPE)
    result = user.stdout
    userList = ""
    for i in result:
        userList += chr(i)
    super = userList.replace("\n", "")
    ruta = "sudo -S mkdir -p /var/www/html/{}.com/public_html".format(nameVH)
    permisosUser = "sudo -S chown -R {}:{} /var/www/html/{}.com/public_html".format(super,super,nameVH)
    permisosRead = "sudo -S chmod -R 755 /var/www"

    index = "index.html"
    contentIndex = "<html>\n\t<head>\n\t<title>¡Bienvenido a {}.com!</title>\n</head>\n<body>\n\t<h1>¡Lo lograste! El virtual host {}.com está funcionando</h1>\n</body>\n</html>".format(nameVH,nameVH)
    createFileIndex = "sudo -S touch /var/www/html/{}.com/public_html/{}".format(nameVH,index)

    fileVH = "{}.com.conf".format(nameVH)
    contentFileVH = "<VirtualHost *:80>\n\tServerAdmin admin@{}.com\n\tServerName {}.com\n\tServerAlias www.{}.com\n\tDocumentRoot /var/www/{}.com/public_html\n\tErrorLog ${{APACHE_LOG_DIR}}/error.log\n\tCustomLog ${{APACHE_LOG_DIR}}/access.log combined\n</VirtualHost>".format(nameVH,nameVH,nameVH,nameVH)
    rutaFileVH = "sudo -S touch /etc/apache2/sites-available/{}".format(fileVH)


    avilitarVH = "sudo -S a2ensite {}".format(fileVH)
    reiniciarApache = "sudo -S systemctl restart apache2"

    subprocess.run(ruta.split())
    subprocess.run(permisosUser.split())
    subprocess.run(permisosRead.split())

    subprocess.run(createFileIndex.split())
    f = open("/var/www/html/{}.com/public_html/{}".format(nameVH,index),"w")
    f.write(contentIndex)
    f.close()

    subprocess.run(rutaFileVH)
    f = open("/etc/apache2/sites-available/{}".format(fileVH),"w")
    f.write(contentFileVH)
    f.close()

    subprocess.run(avilitarVH.split())
    subprocess.run(reiniciarApache.split())


for i in range(1,numVH+1):
    print("Nombre del {} VH: ".format(i), end="")
    nameVH = input()
    newVH(nameVH)




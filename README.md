# Sistema de Gestión de Empleados

Este proyecto es una aplicación web construida con **Python** y **Flask** que permite calcular el salario mensual de empleados y gerentes. Se utiliza **programación orientada a objetos (POO)** para representar diferentes tipos de empleados y aplicar conceptos como herencia, polimorfismo y propiedades.

## 🧠 Conceptos de Programación Aplicados

- **Clases y Objetos**
- **Herencia**
- **Polimorfismo**
- **Sobrecarga de métodos**
- **Propiedades (getters y setters)**

## 📁 Estructura del Proyecto


## 🚀 Cómo Ejecutar en Local

1. Asegúrate de tener Python 3 instalado.
2. Instala Flask si aún no lo tienes:

   ```bash
   pip install flask
## ⛅ Cómo Ejecutar en Remoto EC2 AWS

1. Crear instancia EC2
2. Acceder a consola servidor Linux 2023
3. Instalar el servidor web Apache en sistemas Linux que utilizan el gestor de paquetes Yum,
   
   ```bash
   sudo yum install httpd
4. Para acceder a modo superusuario `Cambia el prompt de @ a #`
   ```bash
   sudo su
5. Para crear un archivo de prueba en la ruta `cd /var/www/html`
   ```bash
   echo > index.html Servidor Linux 2023
6. Comprobamos que podemos ver el archivo index.html copiando y pegando la IP Publica que aparece en la Instancia `Dirección IPv4 pública` o  `PublicIPs`
7. Instalamos git en el servidor
   ```bash
   yum install git
8. Clonamos el repositorio en el servidor
   ```bash
   git clone https://github.com/JTiberK/gestion-empleados.git
9. Instalamos Python
   ```bash
   yum install python
10. Instalamos el pi
   ```bash
   sudo yum install python3-pip
11. Instalamos flask
   ```bash
   pip install flask

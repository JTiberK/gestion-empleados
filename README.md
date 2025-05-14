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
   ```

## ⛅ Cómo Ejecutar en Remoto EC2 AWS

1. Crear instancia EC2
2. Acceder a consola servidor Linux 2023
3. Instalar el servidor web Apache en sistemas Linux que utilizan el gestor de paquetes Yum,

   ```bash
   sudo yum install httpd
   ```

4. Para acceder a modo superusuario `Cambia el prompt de @ a #`
   ```bash
   sudo su
   ```
5. Para crear un archivo de prueba en la ruta `cd /var/www/html`
   ```bash
   echo > index.html Servidor Linux 2023
   ```
6. Comprobamos que podemos ver el archivo index.html copiando y pegando la IP Publica que aparece en la Instancia `Dirección IPv4 pública` o `PublicIPs`
7. Instalamos git en el servidor
   ```bash
   yum install git
   ```
8. Clonamos el repositorio en el servidor
   ```bash
   git clone https://github.com/JTiberK/gestion-empleados.git
   ```
9. Instalamos Python
   ```bash
   yum install python
   ```
1. Instalamos el pip

   ```bash
   sudo yum install python3-pip
2. Instalamos flask
   ```bash
   pip install flask
3. Añadimos esta línea al final del archivo app.py
   ```bash
   if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') <-------------Línea añadida
4. Lanzamos la app
   ```
   python app.py
5. Nos sale este mensaje en consola servidor
   ```bash
   [root@ip-172-31-84-35 gestion-empleados]# python app.py
   * Serving Flask app 'app'
   * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
   * Running on all addresses (0.0.0.0)
   * Running on http://127.0.0.1:5000
   * Running on http://172.31.84.35:5000
   Press CTRL+C to quit
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 119-671-202
6. Elejimos
   ```bash
   172.31.84.35:5000
7. Tambien hemos añadido el health para ver estado servidor `Verlo en los commits`
8. Antes en la ficha de seguridad de nuestra instancia EC2 hemos habilitado el puerto 5000
   ```
   Grupos de seguridad
   sg-0121a8b4ef7d0f1d2 (launch-wizard-1)

   TCP  5000   0.0.0.0
   
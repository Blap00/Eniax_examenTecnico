<p align="center">
  <a href="" rel="noopener">
 <img src="https://eniax.care/wp-content/uploads/2022/09/eniax_entiende.png" alt="Logo" width="260" height="120" class="d-inline-block align-text-top">
</p>

<h3 align="center">Eniax - UF Value Viewer</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> El proyecto abarca el examén técnico sobre visor sobre la Unidad de Fomento, esto basado en tecnologias como Python Flask, el cual nos permite utilizar una API para ver en tiempo real el valor UF.
    <br> 
</p>

## 📝 Table of Contents

- [Acerca del Proyecto](#about)
- [Iniciando](#getting_started)
- [Autores](#authors)
- [Agradecimientos](#acknowledgement)

## 🧐 Acerca del Proyecto <a name = "about"></a>

Este proyecto, UF Value Viewer , tiene como objetivo proporcionar una aplicación para ver los valores actualizados y a diarío sobre la Unidad de Fomento. Desarrollado con un enfoque en la simplicidad y la funcionalidad, esta aplicación utiliza Jinja, Javascript y bootstrap para el frontend, ofreciendo una interfaz de usuario interactiva y fácil de usar, y Flask Python para el backend, asegurando un manejo robusto y eficiente de los datos.

La aplicación permite a los usuarios buscar segun año los valores de la UF. Con un diseño responsivo y una arquitectura de API RESTful, UF Value Viewer está construido para adaptarse a diversas necesidades, desde el uso personal hasta la integración en entornos de trabajo colaborativo. Esta combinación de tecnologías modernas y buenas prácticas de desarrollo garantiza una experiencia fluida y confiable para el usuario final.

## 🏁 Primeros Pasos <a name = "getting_started"></a>

Estas instrucciones te permitirán obtener una copia del proyecto y ejecutarlo en tu máquina local para propósitos de desarrollo y pruebas. Consulta la sección de [despliegue](#deployment) para obtener notas sobre cómo desplegar el proyecto en un sistema en vivo.

### Prerrequisitos

Asegúrate de tener instaladas las siguientes herramientas:

- [Flask](https://nodejs.org/) (versión 3.1 o superior)
- [Python](https://www.npmjs.com/) (versión 3.10.11 o superior)


### Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

1. Clona el repositorio:

    ```bash
    git clone https://github.com/Blap00/Eniax_examenTecnico.git
    cd Eniax_examenTecnico
    ```

2. Configuracion del sistema:

    1. Instala las dependencias necesarias:

        ```bash
        .\venv\Scripts\activate
        ```

    3. Configura los archivos de entorno:

        - Configura un archivo '.env' con los datos necesarios.
        ```python
            API_KEY=<TU API KEY>
        ```

    4. Inicia el servidor:

        ```bash
        python .\run.py
        ```


### Estructura del Proyecto

El proyecto está dividido en dos partes principales:

- **Backend**: Ubicado en el directorio `app`, manejado por Python Flask.
- **Frontend**: Ubicado en el directorio `app/templates, app/static`, construido con HTML, JS, CSS para manejar las solicitudes.

### Ejecución

Una vez completados los pasos anteriores, deberías poder acceder a la aplicación en tu navegador en la dirección `http://localhost:5000`.

¡Ya estás listo para comenzar a desarrollar y probar el proyecto!

## ✍️ Autores <a name = "authors"></a>

- [@Blap00](https://github.com/Blap00) - Desarrollador del sistema


## 🎉 Agradecimientos <a name = "acknowledgement"></a>

- Gracias a videos en YT de [@codewithjoshoffical](https://www.youtube.com/@codewithjoshoffical)
- Proyecto inicial gracias a [Eniax](https://eniax.care/es/)

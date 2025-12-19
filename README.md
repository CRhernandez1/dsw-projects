# Proyectos DSW - Desarrollo Web en Entorno Servidor 🚀

Este repositorio centraliza las soluciones desarrolladas en grupo para la asignatura de **DSW** del Ciclo Formativo de Grado Superior en **Desarrollo de Aplicaciones Web (DAW)**. Ambos proyectos están basados en el ecosistema de **Django**.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=ffb86c)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=50fa7b)
![Status](https://img.shields.io/badge/Status-Academic_Projects-bd93f9?style=for-the-badge)

---

## 📂 Estructura del Repositorio

El repositorio se divide en dos proyectos independientes, cada uno con su propia lógica de negocio y configuración:

1.  **[SuperTODO](./super-todo/):** Sistema de gestión de tareas con lógica de estados.
2.  **[Tribu](./tribu/):** Red social de microblogging con interacciones.

---

## 🛠️ Requisitos Globales

Ambos proyectos comparten un stack moderno orientado a la eficiencia y automatización en el flujo de trabajo:

- **uv:** Gestor de paquetería y proyectos de Python de alto rendimiento.
- **just:** Lanzador de comandos para la automatización de tareas (setup, tests, migraciones).
- **Django:** Framework principal para el desarrollo de la lógica de servidor.

---

## 1. SuperTODO 📝

**SuperTODO** es una aplicación para la gestión de tareas que implementa un flujo completo de creación, edición y filtrado.

- **Características clave:**
  - Visualización dinámica de tareas pendientes y completadas.
  - Sistema de "toggle" para cambio de estado rápido.
  - Uso de formularios de modelo para integridad de datos.
  - Arquitectura basada en aplicaciones modularizadas (`tasks`, `shared`).

---

## 2. Tribu - Red Social 🐦

**Tribu** es una plataforma de microblogging funcional que gestiona la interacción entre usuarios autenticados mediante "Echos" y "Waves".

- **Características avanzadas:**
  - **Arquitectura de Modelos:** Relaciones complejas con integridad referencial y visualización dinámica.
  - **UX/UI Técnica:** Implementación de URLs canónicas, conversores de ruta personalizados y gestión de archivos estáticos (avatares).
  - **Middleware:** Uso de middleware de mensajes para confirmaciones de sistema y optimización del flujo del usuario.
  - **Seguridad:** Control de acceso mediante decoradores y gestión de permisos (403 Forbidden) para la edición de contenido propio.

---

## 🚀 Puesta en Marcha General

Cada carpeta de proyecto contiene una receta `just` para facilitar el despliegue. El proceso estándar para ambos es:

1.  Navegar a la carpeta del proyecto: `cd nombre-del-proyecto`.
2.  Configurar el entorno y dependencias:
    ```bash
    just setup
    ```
3.  Cargar los datos iniciales de prueba:
    ```bash
    just load-data
    ```
4.  Ejecutar el servidor de desarrollo:
    ```bash
    python main/manage.py runserver
    ```

---

## 🤝 Colaboración

Estos proyectos han sido realizados de forma colaborativa como solución técnica a los retos de la asignatura de **DSW**, aplicando rigor analítico y lógica estructurada en la resolución de incidencias.

- Daniele Dettori: [@Pepepe14](https://github.com/Pepepe14)
- Samuel Cruz Sánchez: [@samuelcrz30](https://github.com/samuelcrz30)
- Cristian Reyes Hernández: [@CRhernandez1](https://github.com/CRhernandez1)

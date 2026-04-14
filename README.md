# FoodBridge

FoodBridge es una plataforma en desarrollo orientada a la gestión y articulación de alimentos disponibles para donación entre generadores de alimentos y organizaciones receptoras.

En su estado actual, el proyecto se encuentra construido como backend con Django y PostgreSQL, y ya cuenta con la base inicial del modelo de datos para administrar usuarios, organizaciones, alimentos generados, publicaciones, programación de entregas, entregas y calificaciones.

## Objetivo del proyecto

El propósito de FoodBridge es servir como puente entre entidades que disponen de alimentos y organizaciones que pueden canalizarlos hacia personas que los necesitan, facilitando el registro, la publicación, la coordinación y el seguimiento de las entregas.

## Estado actual

Actualmente el proyecto incluye:

- Configuración base de Django.
- Conexión a base de datos PostgreSQL.
- Aplicación principal `Applications.core`.
- Modelado inicial de las entidades principales del sistema.
- Registro de los modelos en el panel administrativo de Django.
- Migración inicial generada.

Actualmente no incluye todavía:

- Endpoints API.
- Vistas funcionales de negocio.
- Autenticación personalizada.
- Pruebas automatizadas implementadas.
- Frontend o interfaz de usuario final.

## Tecnologías utilizadas

- Python
- Django
- PostgreSQL
- Panel administrativo de Django

## Estructura general del proyecto

```text
foodbridge/
|-- manage.py
|-- README.md
|-- foodbridge/
|   |-- settings.py
|   |-- urls.py
|   |-- asgi.py
|   |-- wsgi.py
|-- Applications/
|   |-- core/
|   |   |-- admin.py
|   |   |-- apps.py
|   |   |-- models.py
|   |   |-- views.py
|   |   |-- tests.py
|   |   |-- migrations/
```

## Modelos implementados

La aplicación `core` concentra actualmente la lógica principal del dominio mediante los siguientes modelos:

### `User`

Representa a los usuarios registrados en la plataforma.

Campos principales:

- `name`
- `email`
- `password`
- `phone`
- `created_at`

### `Organization`

Representa a las organizaciones receptoras o participantes dentro del sistema.

Campos principales:

- `user`
- `name`
- `type`
- `ruc`
- `latitude`
- `longitude`
- `address`
- `capacity`
- `verified`
- `description`
- `created_at`

### `GeneratedFood`

Representa a los generadores de alimentos o la entidad asociada a la publicación de alimentos disponibles.

Campos principales:

- `user`
- `name`
- `type`
- `ruc`
- `latitude`
- `longitude`
- `address`
- `city`
- `verified`
- `created_at`

### `Publication`

Representa una publicación de alimentos disponibles para ser gestionados.

Campos principales:

- `generated_food`
- `title`
- `description`
- `quantity`
- `weight`
- `state`
- `available_from`
- `available_until`
- `created_at`
- `updated_at`

### `Items_Publication`

Permite detallar los ítems específicos asociados a una publicación.

Campos principales:

- `publication`
- `name`
- `category`
- `quantity`
- `unit`
- `expiration_date`
- `observations`

### `Schedules`

Gestiona la programación o coordinación entre publicaciones y organizaciones.

Campos principales:

- `publication`
- `organization`
- `total_people`
- `pickup_time`
- `delivery_time`
- `notes`

### `Delivery`

Registra la información relacionada con la entrega de alimentos.

Campos principales:

- `schedule`
- `organization`
- `delivery_time`
- `observations`

### `Qualification`

Permite almacenar valoraciones o retroalimentación sobre una coordinación o entrega.

Campos principales:

- `schedule`
- `author`
- `type_author`
- `rating`
- `comments`
- `created_at`

## Relaciones principales del sistema

De forma general, el flujo de datos actual está planteado así:

1. Un `User` puede estar asociado a una `Organization`.
2. Un `User` puede estar asociado a un `GeneratedFood`.
3. Un `GeneratedFood` crea una o varias `Publication`.
4. Cada `Publication` puede tener varios `Items_Publication`.
5. Una `Organization` puede coordinar una `Publication` mediante `Schedules`.
6. A partir de una programación se registra una `Delivery`.
7. Finalmente, la experiencia puede ser evaluada mediante `Qualification`.

## Configuración actual

La configuración principal del proyecto se encuentra en `foodbridge/settings.py`.

Aspectos relevantes del estado actual:

- Idioma configurado en `es-ec`.
- Zona horaria configurada en `America/Guayaquil`.
- Base de datos PostgreSQL configurada localmente.
- La única ruta habilitada por ahora es el panel administrativo en `/admin/`.

## Base de datos

Actualmente el proyecto está configurado para trabajar con PostgreSQL con los siguientes parámetros definidos en `settings.py`:

- Base de datos: `foodbridge`
- Usuario: `postgres`
- Host: `localhost`
- Puerto: `5432`

Nota importante:
En el estado actual, las credenciales están definidas directamente en el archivo de configuración. Para un entorno de producción o trabajo colaborativo, se recomienda migrarlas a variables de entorno.

## Cómo ejecutar el proyecto en local

1. Crear y activar un entorno virtual.
2. Instalar Django y la dependencia de PostgreSQL correspondiente.
3. Crear la base de datos `foodbridge` en PostgreSQL.
4. Aplicar las migraciones.
5. Ejecutar el servidor de desarrollo.

Comandos de referencia:

```bash
python -m venv venv
venv\Scripts\activate
pip install django psycopg2-binary
python manage.py migrate
python manage.py runserver
```

Para acceder al panel administrativo:

```text
http://127.0.0.1:8000/admin/
```

Si se desea ingresar al administrador, también será necesario crear un superusuario:

```bash
python manage.py createsuperuser
```

## Panel administrativo

Los siguientes modelos ya se encuentran registrados en el administrador de Django:

- `User`
- `Organization`
- `GeneratedFood`
- `Publication`
- `Items_Publication`
- `Schedules`
- `Delivery`
- `Qualification`

Esto permite gestionar manualmente la información inicial del sistema mientras se desarrollan las vistas, endpoints y reglas de negocio.

## Alcance actual del backend

Hasta este momento, FoodBridge cuenta con una base sólida de modelado para el dominio del proyecto, pero todavía se encuentra en una etapa inicial de desarrollo. La lógica del negocio, las rutas funcionales y la exposición de servicios aún deben implementarse.

En otras palabras, el proyecto ya tiene definida la estructura principal de datos sobre la cual se puede comenzar a construir:

- autenticación y gestión de usuarios,
- APIs o vistas del sistema,
- validaciones de flujo,
- trazabilidad de donaciones,
- reportes,
- dashboards y experiencia de usuario.

## Próximos pasos recomendados

- Implementar vistas o endpoints para cada flujo principal.
- Definir roles y permisos de usuario.
- Mejorar la seguridad de credenciales mediante variables de entorno.
- Crear pruebas unitarias e integración.
- Incorporar serializadores y API REST si el proyecto seguirá una arquitectura desacoplada.
- Documentar reglas de negocio más específicas conforme avance el desarrollo.

## Autores y propósito académico o de desarrollo

Este repositorio documenta el avance actual del sistema FoodBridge y funciona como base para continuar el desarrollo técnico y funcional de la plataforma.

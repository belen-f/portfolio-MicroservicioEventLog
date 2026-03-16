# 📝 Event Log Microservice | FastAPI + MongoDB

**Breve descripción:** Microservicio de alto rendimiento para la gestión y registro de **bitácoras de eventos**, desarrollado con un enfoque en validación estricta de datos y arquitectura asíncrona.

### 🎯 Objetivo del Proyecto

El objetivo es proporcionar una interfaz centralizada **_(API REST)_** que permita a los usuarios gestionar una crónica de eventos **(CRUD)**. El sistema está diseñado para ser ligero, escalable y garantizar que solo los datos que cumplen con el esquema de negocio sean persistidos.

### 🚀 Stack Tecnológico

- **Lenguaje:** Python 3.x
- **Framework:** FastAPI (Asíncrono)
- **Base de Datos:** MongoDB (NoSQL)
- **ODM / Validación:** Pydantic & Motor
- **Documentación:** Swagger UI (Auto-generada)

### 📊 Modelo de Datos

La entidad principal es _"Evento"_, estructurada bajo los siguientes atributos:

| Campo     | Tipo       | Descripción                                      |
| --------- | ---------- | ------------------------------------------------ |
| id        | _ObjectId_ | Identificador único autogenerado                 |
| categoria | _String_   | Ámbito del evento _(ej. Auditoría, Error, Info)_ |
| nombre    | _String_   | Título breve del evento                          |
| nota      | _String_   | Descripción técnica o aclaratoria                |

### 🛠️ Lógica de Implementación (Flujo Funcional)

**Validación en Capa de Entrada:**
Uso de modelos de Pydantic para asegurar que los JSON recibidos coincidan con el contrato definido.

**Mapeo Asíncrono (ODM):**
Integración con Motor para operaciones no bloqueantes hacia MongoDB.

**Serialización:**
Conversión automática de documentos BSON a JSON para respuestas estandarizadas.

---

### 🔧 Instalación y Uso

**Clonar repositorio:** https://github.com/belen-f/portfolio-MicroservicioEventLog.git

**Configurar variables de entorno:** Crear un archivo .env con la MONGO_URL. (teniendo en cuenta si es en local o en la nube)

**Levantar el servicio:**

> bash
>
> uvicorn main:app --reload

**Acceder a la Documentación:** Una vez corriendo, visitar _/docs_ para probar los endpoints interactivamente.

![Visualización de la documentación en Swagger UI](</static/Swagger_UI_(docs).png> "/docs")

## 📈 Roadmap & Próximas Mejoras (Visión de Producto)

Como parte de la **evolución del microservicio**, se han identificado las siguientes oportunidades de mejora para robustecer la solución:

### 🔐 Seguridad y Control de Acceso:

Implementación de **autenticación** JWT (JSON Web Tokens) y manejo de **roles** (RBAC) para restringir quién puede eliminar o modificar registros de la bitácora.

### 🔍 Filtros Avanzados y Paginación:

Optimización de los endpoints de consulta para permitir **filtrado** por rango de fechas, categoría específica y soporte de **paginación** para mejorar el rendimiento con grandes volúmenes de datos.

### ⏱️ Trazabilidad Temporal:

Incorporación automática de campos _created_at_ y _updated_at_ gestionados por el servidor para una **auditoría** precisa de los eventos.

### 🐳 Containerización:

Creación de un archivo _docker-compose.yml_ para estandarizar el **entorno de ejecución**, incluyendo la base de datos MongoDB y el microservicio en contenedores aislados.

### 🧪 Cobertura de Tests:

Desarrollo de **pruebas unitarias e integrales** con Pytest para asegurar la estabilidad del flujo CRUD y las validaciones de Pydantic.

### 📊 Exportación de Datos:

Funcionalidad para **exportar** la bitácora de eventos en formatos CSV o PDF para reportes gerenciales.

---

### 📧 Datos de Contacto:

<belufer.19@gmail.com>


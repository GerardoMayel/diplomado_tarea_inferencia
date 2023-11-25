# Sesión 14: FastAPI y Modelo de Machine Learning

## Instrucciones para la Actividad Grupal

**Fecha de Entrega:** Martes, 28 de Noviembre

### Tarea: Crear una Aplicación FastAPI para Servir un Modelo

**Escenario:**
Un compañero de trabajo te ha proporcionado código para entrenar un modelo de alto rendimiento y solicita tu ayuda para implementarlo en una API local como primer paso hacia la producción.

#### Pasos a Seguir:

1. **Revisión del Código:**

   - Correr el código para verificar su funcionamiento y para crear el modelo.

2. **Refactorización:**

   - Anotar al menos 5 ideas para refactorizaciones basadas en los aprendizajes de los últimos meses.

3. **Construcción de la Aplicación FastAPI: (Tarea Principal)**
   a. Desarrollar un método POST que reciba un JSON como entrada. (Ejemplo de JSON al final del documento).
   b. Utilizar Pydantic para parsear los valores de entrada.
   c. Utilizar el modelo para realizar una predicción.
   d. Devolver la predicción al cliente, preferiblemente usando Pydantic.

4. **Demostración en Video:**

   - Grabar un video mostrando los siguientes procesos:
     a. Entrenamiento del modelo.
     b. Inicio del servidor.
     c. Uso de Postman para realizar peticiones al servidor.
     d. Recepción de una predicción como respuesta.

5. **Pruebas Unitarias:**

   - Añadir pruebas unitarias para el entrenamiento y la inferencia del modelo.

6. **Logging:**

   - Implementar un sistema de logging para registrar los valores de entrada y la predicción retornada durante la inferencia.

7. **Control de Versiones:**

   - Subir el código a un repositorio en Github. Idealmente, ir subiendo cada cambio con contribuciones de todos los integrantes del grupo.

8. **Bonificación (Opcional):**
   - Aplicar las refactorizaciones anotadas y/o mejorar el rendimiento del modelo.

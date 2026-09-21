# Preguntes RFIR

## Descripción

Este repositorio contiene un programa desarrollado en Python para la práctica y repaso de preguntas tipo test correspondientes al examen de acceso a la especialidad de **Radiofísica Hospitalaria (RFIR)**.

El programa permite realizar sesiones de estudio mediante la selección aleatoria de preguntas de un banco de datos, mostrando cuatro opciones de respuesta y proporcionando retroalimentación sobre las respuestas introducidas.

El proyecto ha sido desarrollado con fines exclusivamente educativos y como herramienta de apoyo a la preparación del examen RFIR.

## Características

El programa permite:

* Seleccionar preguntas de forma aleatoria.
* Mostrar cuatro opciones de respuesta para cada pregunta.
* Comprobar la respuesta introducida por el usuario.
* Repetir una pregunta hasta seleccionar la respuesta correcta.
* Saltar una pregunta cuando el usuario lo considere conveniente.
* Finalizar la sesión de estudio en cualquier momento.

El banco de preguntas se almacena en un archivo independiente en formato CSV, lo que permite ampliar o modificar el conjunto de preguntas sin necesidad de modificar el código principal.

## Estructura del repositorio

```text
RFIR/
│
├── Preguntes_RFIR.py
├── Pregs.csv
├── README.md
└── LICENSE
```

### `Preguntes_RFIR.py`

Contiene el código principal del programa y la lógica necesaria para seleccionar las preguntas, mostrar las opciones disponibles y comprobar las respuestas.

### `preguntas.csv`

Contiene el banco de preguntas utilizado por el programa, incluyendo las cuatro opciones de respuesta y la respuesta correcta.

### `README.md`

Documento que describe el proyecto, su funcionamiento y su procedencia.

## Requisitos

Para ejecutar el programa es necesario disponer de:

* Python 3.
* pandas.
* NumPy.

Las dependencias pueden instalarse mediante:

```bash
pip install pandas numpy
```

## Ejecución

Una vez instaladas las dependencias, el programa puede ejecutarse mediante:

```bash
python Preguntes_RFIR.py
```

El programa seleccionará una pregunta aleatoriamente y mostrará las cuatro opciones disponibles.

Las respuestas deben introducirse utilizando los números:

```text
1
2
3
4
```

También están disponibles los siguientes comandos:

```text
Pasar
```

Permite omitir la pregunta actual y continuar con otra.

```text
Terminar
```

Finaliza la sesión de estudio.

## Procedencia de las preguntas

Las preguntas incluidas en el banco de datos proceden de cuestionarios correspondientes a exámenes oficiales de **Radiofísica Hospitalaria (RFIR)** publicados por el **Ministerio de Sanidad del Gobierno de España**.

Las preguntas se han recopilado a partir de los documentos oficiales disponibles públicamente y se han organizado en formato CSV para facilitar su utilización mediante el programa.

Para consultar los documentos originales, se recomienda utilizar las fuentes oficiales del Ministerio de Sanidad correspondientes a las distintas convocatorias del proceso selectivo.

La inclusión de estas referencias en el presente proyecto tiene como finalidad identificar la procedencia del material utilizado.

## Independencia del proyecto

Este proyecto ha sido desarrollado de manera independiente y **no está afiliado, patrocinado, respaldado ni desarrollado por el Ministerio de Sanidad**.

La utilización del nombre RFIR hace referencia exclusivamente al proceso selectivo y a la especialidad de Radiofísica Hospitalaria para cuyo estudio se ha desarrollado esta herramienta.

## Reutilización del contenido

Las preguntas procedentes de los cuestionarios oficiales se identifican como material publicado por el Ministerio de Sanidad. La inclusión de dicho material en este repositorio no implica la transferencia de derechos sobre los documentos originales ni pretende establecer una licencia sobre su contenido.

El código desarrollado específicamente para este proyecto constituye un elemento independiente del contenido procedente de los cuestionarios oficiales.

Para determinar las condiciones aplicables a la reutilización de información publicada por las Administraciones Públicas, deben consultarse las disposiciones legales y condiciones de uso correspondientes, entre ellas la **Ley 37/2007, de 16 de noviembre, sobre reutilización de la información del sector público**, y su normativa de desarrollo.

## Limitaciones

Este programa constituye una herramienta de estudio y no pretende sustituir la documentación oficial, la normativa aplicable, los programas formativos ni ninguna otra fuente oficial relacionada con el proceso selectivo RFIR.

La selección de preguntas disponible en el repositorio puede no representar la totalidad de los contenidos evaluados en las distintas convocatorias.

Se recomienda consultar siempre la documentación oficial del Ministerio de Sanidad para obtener información actualizada sobre las convocatorias, el formato del examen y los contenidos correspondientes.

## Contribuciones

Las contribuciones destinadas a mejorar el funcionamiento del programa son bienvenidas.

Se pueden proponer mejoras relacionadas con:

* Corrección de errores en el código.
* Mejoras en la interfaz de usuario.
* Nuevas funcionalidades de estudio.
* Mejoras en la gestión del banco de preguntas.
* Optimización del código.

Las modificaciones relacionadas con las preguntas deberán mantener la referencia a su fuente original.

## Licencia

La licencia aplicable al código desarrollado para este proyecto se especificará de forma independiente del material procedente de los cuestionarios oficiales.

Las condiciones de reutilización de las preguntas y de los documentos originales quedan sujetas a las condiciones y disposiciones aplicables a dicho material y no se consideran modificadas por la licencia del código del proyecto.

## Fuente

**Ministerio de Sanidad — Gobierno de España**

Información oficial sobre las convocatorias de formación sanitaria especializada y los cuestionarios correspondientes al proceso de Radiofísica Hospitalaria (RFIR).

---

**Autor:** Salva

**Proyecto:** RFIR Question Bank

**Lenguaje:** Python

**¡Suerte! / Sort!**

Nostre Senyor ens ampare.

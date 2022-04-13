# Introducción a selenium con Python

### Indice
- [Conocer el ecocistema de selenium](#Conocer-el-ecocistema-de-selenium)
    - [Por qué aprender Selenium y qué verás](#Por-qué-aprender-Selenium-y-qué-verás)
    - [Historia de Selenium](#Historia-de-Selenium)
    - [Otras herramientas de testing y automatización](#Otras-herramientas-de-testing-y-automatización)
- [Preparar entorno de trabajo](#Preparar-entorno-de trabajo)
    - [Configurar entorno de trabajo](#entidades-y-atributos)
    - [Compatibilidad con python 3.9 y aprendiendo a utilizar múltiples versiones](#atributos)
    - [¡Hola, mundo!](#entidades)
- [Utilizar comandos básicos](#relaciones)
    - [Encontrar elementos con find_element](#cardinalidad-1-a-1)
    - [Preparar assertions y test suites](#cardinalidad-0-a-1)
    - [Entender las clases WwebDriver y WebElement](#cardinalidad)
- [Interactuar con elementos](#relaciones)
    - [Manejar form, textbox, checkbox y radio button](#cardinalidad-1-a-1)
    - [Manejar dropdown y listas](#cardinalidad-0-a-1)
    - [Manejar alert y pop-up](#cardinalidad)
    - [Automatizar navegación](#cardinalidad-1-a-1)
- [Sincronizar pruebas](#relaciones)
    - [Demora implícita y explícita](#cardinalidad-1-a-1)
    - [Condicionales esperadas](#cardinalidad-0-a-1)
- [Retos](#relaciones)
    - [Agregar y eliminar elementos](#cardinalidad-1-a-1)
    - [Elementos dinámicos](#cardinalidad-0-a-1)
    - [Controles dinámicos](#cardinalidad)
    - [Typos](#cardinalidad-1-a-1)
    - [Ordenar tablas](#cardinalidad)
- [Metodologías de Trabajo](#relaciones)
    - [Data Driven Testing (DDT)](#cardinalidad-1-a-1)
    - [Page Object Model (POM)](#cardinalidad-0-a-1)
- [Cierre del curso](#relaciones)
    - [Realizar pruebas técnicas](#cardinalidad-1-a-1)
    - [Conclusiones](#cardinalidad-0-a-1)

# Conocer el ecocistema de selenium

### Por qué aprender Selenium y qué verás

**¿Qué aprenderas?**

- Entender ¿Qué es Selenium? 
- Comunicar selenium con el navegador
- Automatizar pruebas unitarias y funcionales
- Generar reportes de pruebas

### Historia de Selenium

**¿Qué es Selenium?:** "Suite de herramientas para automatización de navegadores".

Es compatible con diversos navegadores web como:

![src/navegadore_web.jpg](src/navegadore_web.jpg)

Actualmente selenium es compatible con distintos lenguajes de programación

![src/lenguajes.jpg](src/lenguajes.jpg)

Selenium No es una herramienta de 
- Testing
- Web Scraping

**Todo comienza en 2004**

- Jason Huggins buscaba automatizar pruebas manuales, creando asi una aplicación llamada "JavaScriptTestRunner". Despues llamada "Selenium Core"

- Paul Hammant vio el demo y buscó una solución a la "Same Origin Policy" y creo "Selenium RC".

- Shinya Katasani en Japón envolvió el código de Selenium convirtiéndolo en un plugin para Firefox.

- Selenium IDE es capaz de grabar, repetir, importar y esportar automatizaciones

- Simon Stewart trabajó en varias herramientas llamadas "WebDriver". Reemplazando JS por un cliente para cada navegador y una API de alto nivel.

- Selenium RC se fusionó a este proyecto, dando lugar a Selenium WebDriver.

**Características, pros y contras**

**Selenium IDE**

**Pros**
- Excelente para iniciar
- No require saber programar
- Exporta scripts para Selenium RC y Selenium WwebDriver
- Genera reportes

**Contras**
- Disponible solo para Firefox y chrome
- No soporta DDT

**Selenium RC**

**Pros**
- Soporta para: 
    - Varias plataformas, navegadores y lenguajes
    - Operaciones logicas y condicionales
    - DDT
- Posee una API madura

**Contras**
- Complejo de instalar
- Necesita de un servidor corriendo
- Comandos redundantes en su API
- Navegación no tan realista

**Selenium WebDriver**

**Pros**
- Soporta para múltiples lenguajes
- Fácil de instalar
- Comunicación directa con el navegador
- Interacción más realista

**Contras**
- No soportan nuevos navegadores tan rápido
- No genera reportes o resultados de pruebas
- Requiere de saber programar

**Selenium Grid**

**características**
- Se utiliza junto a Selenium RC
- Permite correr pruebas en paralelo
- Conveniente para ahorrar tiempo

### Otras herramientas de testing y automatización

**Puppeteer**

**Pros**

- Soporte por parte de Google
- Datos del Performance Analysis de Chrome
- Mayor control de Chrome
- No requiere de drivers externos

**Contras**

- Funciona solo en Chrome con JavaScript
- Comunidad pequeña

**Cypress.io**

**Pros**
- Comunidad emergente
- Buena documentación con ejemplos
- Bastante ágil en pruebas E2E
- Orientado a desarrolladores
- Excelente manejo de asincronismo

**Contras**
- Funciona solo en Chrome y con JavaScript
- Pruebas en paralelo solo en versión pago

# Preparar entorno de trabajo

### Configurar entorno de trabajo
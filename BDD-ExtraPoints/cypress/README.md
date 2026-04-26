# BDD + Cypress

Este proyecto automatiza pruebas web usando Cypress con Cucumber (Gherkin), equivalente al ejemplo de Behave + Selenium en Python.

---

## Requisitos previos

Antes de ejecutar el proyecto necesitas instalar lo siguiente:

### 1. Node.js

Descargar e instalar Node.js (LTS): https://nodejs.org/

Verifica instalación:

```bash
node -v
npm -v
```



## Instalación del proyecto

Dentro de la carpeta del proyecto ejecuta:

```bash
npm install
```

Esto instalará las siguientes dependencias:

- **Cypress** – Framework de testing E2E
- **@badeball/cypress-cucumber-preprocessor** – Soporte para archivos `.feature` (Gherkin)
- **@bahmutov/cypress-esbuild-preprocessor** – Compilador requerido por el preprocessor



## Ejecución del proyecto

### Modo headless (sin navegador visible)

```bash
npm test
```

### Modo headed (con navegador visible)

```bash
npm run test:headed
```

### Modo interactivo (interfaz gráfica de Cypress)

```bash
npm run test:open
```

---


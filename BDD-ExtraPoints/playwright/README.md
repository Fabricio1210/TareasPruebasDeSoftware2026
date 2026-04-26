# BDD + Playwright

Este proyecto automatiza pruebas web usando Playwright con Cucumber (Gherkin), equivalente al ejemplo de Behave + Selenium en Python.

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

### 1. Instalar dependencias

```bash
npm install
```

### 2. Instalar Playwright y sus navegadores

```bash
npm init playwright@latest
```

Te pedirá varias opciones, responde así:

| Pregunta | Respuesta |
|---|---|
| TypeScript or JavaScript? | **JavaScript** |
| Where to put your end-to-end tests? | **tests** |
| Add a GitHub Actions workflow? | **n** |
| Install Playwright browsers? | **y** |

---


## Ejecución del proyecto

### Modo normal (con navegador visible)

```bash
npm test
```

### Modo headless (sin navegador visible)

Cambia en `features/step_definitions/duckduckgo_search.steps.js`:

```js
browser = await chromium.launch({
  headless: true,
  args: ["--disable-blink-features=AutomationControlled"],
});
```


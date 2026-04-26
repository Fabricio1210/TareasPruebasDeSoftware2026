# BDD + Appium

Este proyecto automatiza pruebas moviles usando APPIUM

---

##  Requisitos previos

Antes de ejecutar el proyecto necesitas instalar lo siguiente:

### 1. Node.js

Descargar e instalar Node.js (LTS): https://nodejs.org/

Verifica instalación:

```bash
node -v
npm -v
```

### 2. Java JDK

Appium requiere Java para Android automation.

- Instalar JDK 8 o superior
- Configurar variable de entorno:

```
JAVA_HOME = C:\Program Files\Java\jdk-XX
```

Agregar al PATH:

```
%JAVA_HOME%\bin
```

### 3. Android SDK + ADB

Instala Android Studio: https://developer.android.com/studio

Variables de entorno:

```
ANDROID_HOME = C:\Users\TU_USUARIO\AppData\Local\Android\Sdk
```

Agregar al PATH:

```
%ANDROID_HOME%\platform-tools
%ANDROID_HOME%\emulator
%ANDROID_HOME%\tools
%ANDROID_HOME%\tools\bin
```

### 4. Verificar ADB

Conecta un dispositivo o usa un emulador:

```bash
adb devices
```

Debe aparecer algo como:

```
List of devices attached
emulator-XXXX   device
```

### 5. Appium

Instalar Appium:

```bash
npm install appium --save-dev
```

Verificar:

```bash
appium -v
```

---

## Instalación del proyecto

Dentro del proyecto:

```bash
npm install
```

Esto instalará dependencias como:

- WebDriverIO
- Cucumber
- Appium Service
- Assert
- etc.

---

## Ejecución del proyecto

Ejecuta las pruebas con:

```bash
npx wdio run wdio.conf.js
```


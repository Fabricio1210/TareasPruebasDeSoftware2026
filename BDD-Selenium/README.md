# BDD Selenium - University Navigation Tests

## Requisitos

- Python 3.x
- Google Chrome instalado

## Instalación

```bash
pip install behave selenium
```

## Cómo correr las pruebas

```bash
behave
```

## Estructura del proyecto

```
features/
├── search.feature      # Escenarios de prueba
└── steps/
    └── search.py       # Implementación de los steps
```

## Universidades que se prueban

| Universidad | Sección buscada |
|---|---|
| iteso.mx | programas |
| uvm.mx | oferta |
| tec.mx | es/educacion |

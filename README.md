# Juego 2D con Pygame

Un esqueleto básico de un juego 2D desarrollado con Pygame.

## Características

- Ventana de 800x600 píxeles
- Bucle principal del juego con 60 FPS
- Manejo de eventos (cierre de ventana y tecla ESC)
- Estructura de clase para fácil extensión
- Colores predefinidos para uso común

## Instalación

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta el juego:
```bash
python game.py
```

## Controles

- **ESC**: Salir del juego
- **X (botón de cerrar ventana)**: Salir del juego

## Estructura del código

- `Game` class: Maneja la inicialización, eventos, actualización y dibujo
- `handle_events()`: Procesa eventos de teclado y mouse
- `update()`: Lógica de actualización del juego (vacía, lista para implementar)
- `draw()`: Dibuja elementos en pantalla (incluye un rectángulo rojo de ejemplo)
- `run()`: Bucle principal del juego

## Extensión

Para agregar funcionalidad al juego, puedes:

1. Añadir lógica en el método `update()`
2. Dibujar elementos en el método `draw()`
3. Manejar eventos adicionales en `handle_events()`
4. Agregar nuevas clases para sprites, enemigos, etc.

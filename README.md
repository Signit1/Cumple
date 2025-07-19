# 🎂 CumpleC - Hackathon Emocional para Constantino

Una aplicación interactiva de cumpleaños con temática de Fórmula 1 y programación, diseñada como una "hackathon emocional" para celebrar el cumpleaños de Constantino.

## 🚀 Características

- **Dos fases interactivas** con temática de F1 y pádel
- **8 pistas gamificadas** basadas en libros de su librero
- **Acertijos y desafíos** que combinan F1, alemán y programación
- **Barra de progreso visual** y animaciones
- **Mensajes personalizados** en cada pista
- **Dos versiones disponibles**: Python (terminal) y JavaScript (web)

## 📋 Requisitos

### Versión Python
- Python 3.6 o superior
- Terminal/Consola
- Los libros mencionados en las pistas (físicos)

### Versión JavaScript (Recomendada)
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- Los libros mencionados en las pistas (físicos)
- **¡No requiere instalación!**

## 🎮 Cómo Ejecutar

### 🌐 Versión JavaScript (Recomendada)

**¡La forma más fácil!**

1. **Abrir en el navegador:**
   - Simplemente abre el archivo `index.html` en cualquier navegador web
   - O haz doble clic en `index.html`

2. **Usar en cualquier dispositivo:**
   - Computadora, tablet o smartphone
   - Funciona offline (sin internet)

3. **Características adicionales:**
   - Interfaz moderna y responsiva
   - Animaciones suaves
   - Confeti animado al final
   - Diseño adaptativo para móviles

### 🐍 Versión Python

#### Opción 1: Ejecución Directa
```bash
python3 cumplec.py
```

#### Opción 2: Hacer Ejecutable (macOS/Linux)
```bash
chmod +x cumplec.py
./cumplec.py
```

#### Opción 3: Script de Prueba
```bash
python3 test_cumplec.py
```

## 📅 Fases del Desafío

### Fase 1: Día del Pádel (18 de Julio)
- Mensaje motivador de bienvenida
- Celebración del espíritu de logro
- Preparación para el desafío del día siguiente

### Fase 2: Día de las Pistas (19 de Julio)
- Acertijo inicial sobre F1 y alemán
- 8 pistas basadas en libros específicos
- Sistema de claves y progreso visual
- Mensaje final de celebración

## 📚 Libros Requeridos

Para que el desafío funcione completamente, Constantino necesitará acceso a estos libros:

1. **El Principito** - Antoine de Saint-Exupéry
2. **Harry Potter** - J.K. Rowling
3. **Padre Rico Padre Pobre** - Robert Kiyosaki
4. **The Lean Startup** - Eric Ries
5. **El Negociador** - Michael Wheeler
6. **How to Win Friends and Influence People** - Dale Carnegie
7. **The Psychology of Money** - Morgan Housel

## 🎯 Preparación

### Para el 18 de Julio (Fase 1):
1. Ejecutar el programa (Python) o abrir en navegador (JavaScript)
2. Mostrar el mensaje de bienvenida
3. Cerrar el programa
4. Preparar las cartas para mañana

### Para el 19 de Julio (Fase 2):
1. **Preparar las cartas físicas** con los mensajes personalizados
2. **Colocar las cartas** en los libros correspondientes
3. **Ejecutar el programa** para iniciar el Gran Premio
4. **Seguir las pistas** del sistema

## 🔑 Sistema de Claves

Cada pista tiene una clave principal y una alternativa:

| Pista | Clave Principal | Clave Alternativa |
|-------|----------------|-------------------|
| 1 | zorro | esencial |
| 2 | combates | lucha |
| 3 | ricos | dinero |
| 4 | learn | faster |
| 5 | acuerdo | victoria |
| 6 | interested | friends |
| 7 | disciplina | poder |
| 8 | realidad | viable |

## 🎨 Características Técnicas

### Versión JavaScript
- **Interfaz web moderna** con gradientes y animaciones
- **Responsive design** para todos los dispositivos
- **Animaciones CSS** suaves y profesionales
- **Confeti animado** al completar el desafío
- **Sin dependencias externas** - funciona offline
- **Navegación intuitiva** con transiciones suaves

### Versión Python
- **Interfaz de terminal** con emojis y colores
- **Animaciones de carga** y confeti
- **Barra de progreso visual**
- **Sistema de intentos** (3 por pista)
- **Manejo de errores** elegante
- **Verificación de fechas** automática

## 🛠️ Personalización

### Versión JavaScript
Edita `script.js` en la sección de datos:
```javascript
this.pistas = {
    1: {
        mensaje: 'Tu mensaje personalizado aquí',
        // ...
    }
};
```

### Versión Python
Edita `cumplec.py` en la sección de pistas:
```python
self.pistas = {
    1: {
        'mensaje': 'Tu mensaje personalizado aquí',
        # ...
    }
}
```

## 🎉 Resultado Final

Al completar todas las pistas, Constantino recibirá:
- Un mensaje de celebración personalizado
- Animación de confeti (JavaScript) o confeti en terminal (Python)
- Instrucciones para encontrar sus regalos
- Reconocimiento de su logro

## 💡 Consejos de Uso

### Versión JavaScript (Recomendada)
1. **Probar antes**: Abre `index.html` y usa "Modo Prueba"
2. **Preparar cartas**: Imprimir desde `cartas_para_imprimir.txt`
3. **Ubicación de regalos**: Definir claramente dónde estarán
4. **Compartir fácilmente**: Envía los archivos por email o compártelos

### Versión Python
1. **Probar antes**: Ejecutar `test_cumplec.py`
2. **Preparar cartas**: Imprimir desde `cartas_para_imprimir.txt`
3. **Ubicación de regalos**: Definir claramente dónde estarán
4. **Backup**: Tener una copia del programa

## 📁 Estructura de Archivos

### Versión JavaScript
```
CumpleC/
├── index.html          # Página principal
├── styles.css          # Estilos CSS
├── script.js           # Lógica JavaScript
├── cartas_para_imprimir.txt
├── README.md
└── INSTRUCCIONES.md
```

### Versión Python
```
CumpleC/
├── cumplec.py          # Programa principal
├── test_cumplec.py     # Script de prueba
├── config.py           # Configuración
├── cartas_para_imprimir.txt
├── requirements.txt
├── README.md
└── INSTRUCCIONES.md
```

## 🎂 ¡Feliz Cumpleaños, Constantino!

Este programa es una celebración de:
- Tu pasión por la programación
- Tu amor por F1
- Tu interés en aprender alemán
- Tu espíritu competitivo en el pádel
- Tu capacidad para resolver desafíos

**¡Recomendación:** Usa la versión JavaScript para una experiencia más visual y moderna, especialmente si Constantino disfruta de las interfaces web y la tecnología moderna.

---

*Desarrollado con ❤️ para el cumpleaños de Constantino* 
# 🎂 INSTRUCCIONES COMPLETAS - CUMPLC

## 📋 Lista de Verificación Previa

### ✅ Requisitos Técnicos
- [ ] Python 3.6+ instalado
- [ ] Terminal/Consola disponible
- [ ] Acceso a los libros mencionados

### ✅ Materiales Necesarios
- [ ] 8 cartas impresas (ver `cartas_para_imprimir.txt`)
- [ ] Los libros correspondientes
- [ ] Regalos para el final
- [ ] Papel y tijeras para recortar las cartas

## 🚀 Instalación y Configuración

### Paso 1: Verificar Python
```bash
python3 --version
```
Debe mostrar Python 3.6 o superior.

### Paso 2: Descargar los archivos
Asegúrate de tener todos estos archivos en la misma carpeta:
- `cumplec.py` (programa principal)
- `test_cumplec.py` (script de prueba)
- `cartas_para_imprimir.txt` (cartas para imprimir)
- `config.py` (configuración)
- `README.md` (documentación)

### Paso 3: Probar el programa
```bash
python3 test_cumplec.py
```
Esto te permitirá probar ambas fases sin depender de las fechas.

## 📅 Cronograma de Ejecución

### Día 1: 18 de Julio (Fase 1)
**Hora sugerida:** Después del pádel

1. **Ejecutar el programa:**
   ```bash
   python3 cumplec.py
   ```

2. **Mostrar el mensaje de bienvenida**
3. **Cerrar el programa**
4. **Preparar las cartas para mañana**

### Día 2: 19 de Julio (Fase 2)
**Hora sugerida:** Mañana o tarde

1. **Colocar las cartas en los libros** (ver sección de cartas)
2. **Ejecutar el programa:**
   ```bash
   python3 cumplec.py
   ```
3. **Seguir las pistas del sistema**
4. **Celebrar al final**

## 📚 Preparación de las Cartas

### Paso 1: Imprimir las cartas
1. Abre `cartas_para_imprimir.txt`
2. Imprime cada carta en papel de calidad
3. Recorta siguiendo los marcos

### Paso 2: Colocar en los libros
Coloca cada carta en el libro correspondiente:

| Carta | Libro | Ubicación Sugerida |
|-------|-------|-------------------|
| 1 | El Principito | Capítulo del zorro |
| 2 | Harry Potter | Capítulo 17 del primer libro |
| 3 | Padre Rico Padre Pobre | Capítulos sobre dinero |
| 4 | The Lean Startup | Capítulos sobre aprendizaje |
| 5 | El Negociador | Capítulos sobre acuerdos |
| 6 | How to Win Friends... | Capítulos sobre conexión |
| 7 | The Psychology of Money | Capítulos sobre disciplina |
| 8 | The Lean Startup | Capítulos iniciales |

### Paso 3: Asegurar las cartas
- Usa marcadores de página
- Dobla ligeramente las esquinas
- Asegúrate de que no se caigan fácilmente

## 🎯 Ejecución del Desafío

### Fase 1 (18 de Julio)
1. Ejecuta `python3 cumplec.py`
2. El programa mostrará el mensaje de bienvenida
3. Presiona ENTER para continuar
4. El programa se cerrará automáticamente

### Fase 2 (19 de Julio)
1. Ejecuta `python3 cumplec.py`
2. Resuelve el acertijo inicial (EAU ROUGE)
3. Sigue cada pista del sistema
4. Busca las cartas en los libros
5. Ingresa las claves correctas
6. Completa todas las pistas
7. Disfruta del mensaje final

## 🔑 Sistema de Claves

Cada carta tiene una clave principal y una alternativa:

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

## 🎁 Preparación de Regalos

### Ubicación Sugerida
- **Lugar:** Centro de la mesa en el comedor
- **Alternativa:** Junto a su computadora
- **Opcional:** En su lugar de trabajo favorito

### Ideas de Regalos
- Libros técnicos
- Accesorios de F1
- Material para aprender alemán
- Equipo de pádel
- Gadgets tecnológicos

## 🛠️ Solución de Problemas

### Error: "Python no encontrado"
```bash
# En macOS/Linux
which python3

# En Windows
python --version
```

### Error: "Módulo no encontrado"
```bash
# Instalar dependencias (si es necesario)
pip3 install -r requirements.txt
```

### Error: "Fecha no programada"
- Verifica que la fecha del sistema sea correcta
- Usa `test_cumplec.py` para probar sin restricciones de fecha

### Error: "Clave incorrecta"
- Verifica que estés usando la clave correcta
- Las claves no distinguen mayúsculas/minúsculas
- Acepta tanto la clave principal como la alternativa

## 🎨 Personalización

### Cambiar fechas
Edita `config.py`:
```python
FECHA_FASE_1 = (18, 7)  # Cambia por las fechas deseadas
FECHA_FASE_2 = (19, 7)
```

### Cambiar mensajes
Edita `cumplec.py` en la sección de pistas:
```python
self.pistas = {
    1: {
        'mensaje': 'Tu mensaje personalizado aquí',
        # ...
    }
}
```

### Cambiar ubicación de regalos
Edita `cumplec.py` en la función `mostrar_mensaje_final()`:
```python
"Ahora, dirígete al [NUEVA UBICACIÓN] para recoger tu trofeo..."
```

## 📞 Soporte

### Antes del evento
- Prueba el programa completo
- Verifica que todos los libros estén disponibles
- Imprime las cartas con anticipación

### Durante el evento
- Mantén el programa ejecutándose
- Ten las claves a mano (pero ocultas)
- Prepárate para ayudar si es necesario

### Después del evento
- Guarda el programa como recuerdo
- Considera reutilizar la idea para otros eventos
- Comparte la experiencia

## 🎂 ¡Feliz Cumpleaños, Constantino!

Este programa es una celebración de:
- Tu pasión por la programación
- Tu amor por F1
- Tu interés en aprender alemán
- Tu espíritu competitivo en el pádel
- Tu capacidad para resolver desafíos

¡Que disfrutes de esta hackathon emocional!

---

*Desarrollado con ❤️ para hacer tu cumpleaños especial* 
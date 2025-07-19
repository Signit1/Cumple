# -*- coding: utf-8 -*-
"""
Archivo de configuración para CumpleC
Aquí puedes personalizar fácilmente el programa sin tocar el código principal.
"""

# Configuración de fechas
FECHA_FASE_1 = (18, 7)  # (día, mes) - 18 de Julio
FECHA_FASE_2 = (19, 7)  # (día, mes) - 19 de Julio

# Configuración del acertijo inicial
ACERTIJO_INICIAL = {
    'pregunta': """🏁 ACERTIJO INICIAL - CURVA MÁGICA 🏁

Soy la curva más famosa de un circuito belga, donde la velocidad y la valentía se unen. 
Mi nombre, en alemán, podría evocar la palabra 'rojo'. ¿Qué curva soy?

💡 Pista: Piensa en la intensidad y el color...""",
    'respuesta_correcta': 'eau rouge',
    'pista_adicional': 'La respuesta era: EAU ROUGE'
}

# Configuración de mensajes del sistema
MENSAJES_SISTEMA = {
    1: "¡Primera vuelta completada!",
    2: "Has superado la primera vuelta, Ahora, el siguiente desafío",
    3: "¡Gran avance en el sector financiero! La próxima parada te espera.",
    4: "¡Acelera en la innovación! La siguiente señal de boxes está en.",
    5: "¡Negociando la curva perfecta! Tu próxima parada es en.",
    6: "¡Conectando con la parrilla! La última parada antes de la meta está en.",
    7: "¡Recta final hacia la sabiduría financiera! Busca en.",
    8: "¡Cruzando la línea de meta de la innovación! La última pista te espera en."
}

# Configuración del mensaje final
MENSAJE_FINAL = {
    'titulo': "¡BANDERA A CUADROS! ¡CAMPEÓN DEL GRAN PREMIO DEL AMOR Y EL CONOCIMIENTO!",
    'contenido': """¡Lo lograste, Constantino! Has demostrado una vez más que no hay desafío que se te resista. Cada logro tuyo es un motivo de alegría y orgullo para mí. Tu esfuerzo, tu inteligencia y tu corazón gigante me inspiran.

Ahora, dirígete al centro de la mesa en el comedor para recoger tu trofeo y celebrar tu cumpleaños, ¡y la promesa de muchos logros más juntos!

¡Feliz Cumpleaños, mi amor! Siempre recuerda cuánto te amo y valoro. Eres increíble.""",
    'ubicacion_regalos': 'centro de la mesa en el comedor'
}

# Configuración de animaciones
ANIMACIONES = {
    'duracion_carga': 2,  # segundos
    'duracion_confeti': 3,  # ciclos
    'velocidad_animacion': 0.1  # segundos entre frames
}

# Configuración de intentos
INTENTOS_MAXIMOS = 3

# Configuración de emojis
EMOJIS = {
    'padel': '🏓',
    'f1': '🏎️',
    'trophy': '🏆',
    'birthday': '🎂',
    'heart': '💝',
    'book': '📚',
    'key': '🔑',
    'confetti': ['🎉', '🎊', '🎈', '🎂', '🏆', '💝', '✨', '🌟']
}

# Configuración de colores (para terminales que soporten ANSI)
COLORES = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m'
}

# Configuración de sonidos (opcional - requiere biblioteca adicional)
SONIDOS = {
    'habilitado': False,  # Cambiar a True si quieres sonidos
    'victoria': 'victory.wav',
    'error': 'error.wav',
    'progreso': 'progress.wav'
}

# Configuración de idioma
IDIOMA = 'es'  # 'es' para español, 'en' para inglés

# Configuración de modo debug
DEBUG = False  # Cambiar a True para ver información de debug

# Configuración de backup
BACKUP_AUTOMATICO = True  # Crear backup automático de progreso

# Configuración de personalización
PERSONALIZACION = {
    'nombre': 'Constantino',
    'apodo': 'Ingeniero',
    'fecha_cumpleanos': '19 de Julio',
    'temas_favoritos': ['F1', 'Programación', 'Alemán', 'Pádel']
} 
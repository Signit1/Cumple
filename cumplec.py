#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
¡CumpleC - Hackathon Emocional para Constantino!
Una aventura para encontrar tu regalo de cumpleaños con temática de F1 y programación.
"""

import os
import time
import sys
from datetime import datetime

class CumpleC:
    def __init__(self):
        self.current_phase = 1
        self.current_pista = 0
        self.pistas_completadas = 0
        self.total_pistas = 8
        
        # Datos de las pistas
        self.pistas = {
            1: {
                'libro': 'El Principito',
                'ubicacion': 'cerca de donde el zorro comparte una gran verdad',
                'frase': 'Lo esencial es invisible a los ojos.',
                'mensaje': 'Dicen que lo esencial es invisible a los ojos... por suerte, yo tengo rayos X en el corazón 🤓💘\n\nPorque contigo lo veo todo: tu forma de cuidarme, de hacerme reír, de estar incluso cuando no estás.\n\nY aunque no siempre se vea, lo nuestro brilla más que cualquier cosa visible.',
                'clave': 'zorro',
                'clave_alternativa': 'esencial'
            },
            2: {
                            'libro': 'Los Miserables',
            'ubicacion': 'Capítulo 17 del primer libro',
                'frase': 'El mayor de los combates es aquel que se libra contra uno mismo.',
                'mensaje': 'Sé que te exiges mucho, y admiro tu constante búsqueda de mejora. Recuerda que ya has ganado muchas batallas internas y externas, y eso te hace increíblemente fuerte. Siempre estaré aquí para ti ya que somos un equipo.',
                'clave': 'combates',
                'clave_alternativa': 'lucha'
            },
            3: {
                'libro': 'Padre Rico Padre Pobre',
                'ubicacion': 'en sus principios fundamentales sobre el dinero',
                'frase': 'La gente pobre y de clase media trabaja por dinero. Los ricos hacen que el dinero trabaje para ellos.',
                'mensaje': 'Siempre me impresionas con tu visión y tu disciplina para lograr tus metas económicas. Sé que el dinero trabajará para ti porque estás construyendo un futuro sólido y brillante. ¡Eres un maestro en ello!',
                'clave': 'ricos',
                'clave_alternativa': 'dinero'
            },
            4: {
                'libro': 'The Lean Startup',
                'ubicacion': 'en los capítulos sobre el aprendizaje ágil',
                'frase': 'The only way to win is to learn faster than anyone else.',
                'mensaje': 'Esta frase te describe a la perfección. Tu insaciable sed de conocimiento y tu capacidad para adaptarte y aprender rápidamente son tus mayores superpoderes. ¡Con eso, siempre ganas!',
                'clave': 'learn',
                'clave_alternativa': 'faster'
            },
            5: {
                'libro': 'El Negociador',
                'ubicacion': 'en los capítulos sobre el arte de llegar a acuerdos',
                'frase': 'El objetivo de la negociación no es la victoria, sino el acuerdo.',
                'mensaje': 'Aunque eres un ganador nato, valoro aún más tu capacidad para construir puentes y encontrar soluciones que beneficien a todos. Eso es verdadero liderazgo y éxito.',
                'clave': 'acuerdo',
                'clave_alternativa': 'victoria'
            },
            6: {
                'libro': 'How to Win Friends and Influence People',
                'ubicacion': 'en sus principios para conectar con los demás',
                'frase': 'To be interesting, be interested.',
                'mensaje': 'Tu curiosidad genuina y tu interés por aprender de todo y de todos te hacen una persona fascinante y un líder natural. ¡Nunca dejes de inspirar!',
                'clave': 'interested',
                'clave_alternativa': 'friends'
            },
            7: {
                'libro': 'The Psychology of Money',
                'ubicacion': 'hacia la mitad del libro, donde se habla de la disciplina',
                'frase': 'Tener dinero es poder; mantenerlo es disciplina.',
                'mensaje': 'Tú entiendes que el verdadero poder no es solo acumular, sino gestionar con sabiduría. Tu disciplina y visión en cada aspecto de tu vida son un ejemplo para mí y para muchos. Estoy increíblemente orgullosa de ti.',
                'clave': 'disciplina',
                'clave_alternativa': 'poder'
            },
            8: {
                'libro': 'The Lean Startup',
                'ubicacion': 'en los primeros capítulos sobre cómo empezar',
                'frase': 'El producto mínimo viable es tu boleto a la realidad.',
                'mensaje': 'Siempre transformas tus ideas en realidades. Cada paso que das, por pequeño que parezca, es un avance hacia los gigantes proyectos que construirás. Eres un arquitecto de sueños. ¡Te amo!',
                'clave': 'realidad',
                'clave_alternativa': 'viable'
            }
        }

    def limpiar_pantalla(self):
        """Limpia la pantalla de la terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def mostrar_progreso(self):
        """Muestra la barra de progreso de las pistas"""
        print(f"\n🏁 PISTAS COMPLETADAS: {self.pistas_completadas}/{self.total_pistas}")
        progreso = "█" * self.pistas_completadas + "░" * (self.total_pistas - self.pistas_completadas)
        print(f"[{progreso}] {self.pistas_completadas * 12.5:.0f}% completado")
        print("=" * 50)

    def animacion_carga(self, mensaje, duracion=2):
        """Muestra una animación de carga"""
        print(f"\n{mensaje}")
        for i in range(duracion * 10):
            print("⏳", end="", flush=True)
            time.sleep(0.1)
            print("\b", end="", flush=True)
            print("⏳", end="", flush=True)
            time.sleep(0.1)
            print("\b", end="", flush=True)
        print("✅")

    def animacion_confeti(self):
        """Muestra una animación de confeti"""
        confeti = ["🎉", "🎊", "🎈", "🎂", "🏆", "💝", "✨", "🌟"]
        for _ in range(3):
            for emoji in confeti:
                print(f"{emoji} ", end="", flush=True)
                time.sleep(0.1)
            print()
            time.sleep(0.3)

    def fase_1(self):
        """Ejecuta la Fase 1 - Día del Pádel"""
        self.limpiar_pantalla()
        print("🏓" * 20)
        print("🏓" * 20)
        print()
        
        mensaje_bienvenida = """
¡Bienvenido al Desafío del Campeón, Constantino!

Hoy hemos compartido la cancha, y una vez más me has demostrado tu pasión y tu espíritu de lucha. Como en el pádel, en la vida eres un verdadero campeón, un ganador nato que convierte cada desafío en una oportunidad. Esta es solo la primera jugada de algo especial.

Mañana, la verdadera carrera comienza. Prepárate para usar todo tu ingenio. Por ahora, solo disfruta de este momento y de ser el increíble tú que eres.
"""
        print(mensaje_bienvenida)
        print("🏓" * 20)
        print("🏓" * 20)
        
        input("\n🎾 Presiona ENTER para continuar...")
        
        self.animacion_carga("Programando el desafío para mañana...")
        print("\n✅ Programa cargado para el 19 de Julio. ¡Que la suerte y el éxito te acompañen!")
        
        input("\n🏁 Presiona ENTER para cerrar...")

    def fase_2(self):
        """Ejecuta la Fase 2 - Día de las Pistas"""
        self.limpiar_pantalla()
        print("🏎️" * 20)
        print("🏎️" * 20)
        print()
        
        mensaje_inicio = """
¡Gran Premio de Cumpleaños: Se encienden las luces verdes!

¡Ingeniero, los motores están encendidos! Hoy es el día de un Gran Premio diferente, donde el circuito es tu intelecto y la meta es una celebración única. Para la primera vuelta, resuelve este acertijo y usa la respuesta como tu clave de acceso.
"""
        print(mensaje_inicio)
        print("🏎️" * 20)
        print("🏎️" * 20)
        
        # Acertijo inicial
        acertijo = """
🏁 ACERTIJO INICIAL - CURVA MÁGICA 🏁

Soy la curva más famosa de un circuito belga, donde la velocidad y la valentía se unen. 
Mi nombre, en alemán, podría evocar la palabra 'rojo'. ¿Qué curva soy?

💡 Pista: Piensa en la intensidad y el color...
"""
        print(acertijo)
        
        respuesta_correcta = "eau rouge"
        intentos = 0
        
        while intentos < 3:
            respuesta = input("\n🏁 Tu respuesta: ").strip().lower()
            intentos += 1
            
            if respuesta == respuesta_correcta:
                print("\n🎉 ¡CORRECTO! ¡Has superado la primera chicane!")
                self.animacion_carga("Inicializando el Gran Premio...")
                break
            else:
                if intentos < 3:
                    print(f"\n❌ Incorrecto. Intento {intentos}/3. ¡Sigue intentando!")
                else:
                    print(f"\n💡 La respuesta era: EAU ROUGE")
                    print("¡Pero no te preocupes! Continuemos con el desafío...")
        
        # Comenzar con las pistas
        self.comenzar_pistas()

    def comenzar_pistas(self):
        """Inicia el sistema de pistas"""
        self.current_pista = 1
        
        while self.current_pista <= self.total_pistas:
            self.mostrar_pista_actual()
            
            if self.current_pista == self.total_pistas:
                self.mostrar_mensaje_final()
                break
            else:
                self.current_pista += 1

    def mostrar_pista_actual(self):
        """Muestra la pista actual y solicita la clave"""
        pista = self.pistas[self.current_pista]
        
        self.limpiar_pantalla()
        self.mostrar_progreso()
        
        print(f"\n🏁 PISTA {self.current_pista} - VUELTA {self.current_pista}")
        print("=" * 50)
        
        # Mensaje del sistema según la pista
        mensajes_sistema = {
            1: "¡Primera vuelta completada!",
            2: "¡Has superado la primera chicane! Ahora, enfrenta el desafío interno.",
            3: "¡Gran avance en el sector financiero! La próxima parada te espera.",
            4: "¡Acelera en la innovación! La siguiente señal de boxes está en.",
            5: "¡Negociando la curva perfecta! Tu próxima parada es en.",
            6: "¡Conectando con la parrilla! La última parada antes de la meta está en.",
            7: "¡Recta final hacia la sabiduría financiera! Busca en.",
            8: "¡Cruzando la línea de meta de la innovación! La última pista te espera en."
        }
        
        print(f"\n{mensajes_sistema[self.current_pista]}")
        print(f"📚 Busca en tu librero el libro **'{pista['libro']}'**, {pista['ubicacion']}.")
        
        input("\n📖 Presiona ENTER cuando hayas encontrado la carta...")
        
        # Mostrar contenido de la carta
        print(f"\n💌 CONTENIDO DE LA CARTA:")
        print("-" * 30)
        print(f"📝 Frase: \"{pista['frase']}\"")
        print(f"💝 Tu mensaje: {pista['mensaje']}")
        print("-" * 30)
        
        # Solicitar clave
        print(f"\n🔑 Ingresa la clave de la carta para continuar...")
        
        intentos = 0
        while intentos < 3:
            clave = input("🔑 Clave: ").strip().lower()
            intentos += 1
            
            if clave in [pista['clave'], pista['clave_alternativa']]:
                print(f"\n🎉 ¡CORRECTO! ¡Pista {self.current_pista} completada!")
                self.pistas_completadas += 1
                self.animacion_carga("Procesando siguiente pista...")
                break
            else:
                if intentos < 3:
                    print(f"\n❌ Clave incorrecta. Intento {intentos}/3.")
                    print(f"💡 Pista: Busca una palabra clave en la carta...")
                else:
                    print(f"\n💡 La clave era: {pista['clave'].upper()}")
                    print("¡Pero continuemos! No te rindas...")
                    self.pistas_completadas += 1

    def mostrar_mensaje_final(self):
        """Muestra el mensaje final de victoria"""
        self.limpiar_pantalla()
        
        print("🏆" * 20)
        print("🏆" * 20)
        print()
        
        mensaje_final = """
¡BANDERA A CUADROS! ¡CAMPEÓN DEL GRAN PREMIO DEL CONOCIMIENTO Y LA CONSTANCIA!

¡Lo lograste, Constantino! Has demostrado una vez más que no hay desafío que se te resista. Cada logro tuyo es un motivo de alegría y orgullo para mí. Tu esfuerzo, tu inteligencia y tu corazón gigante me inspiran.

Ahora, dirígete al centro de la mesa en el comedor para recoger tu trofeo y celebrar tu cumpleaños, ¡y la promesa de muchos logros más juntos!

¡Feliz Cumpleaños, mi amor! Siempre recuerda cuánto te amo y valoro. Eres increíble.
"""
        print(mensaje_final)
        print("🏆" * 20)
        print("🏆" * 20)
        
        # Animación de confeti
        print("\n🎉 ¡CELEBRACIÓN! 🎉")
        self.animacion_confeti()
        
        input("\n🏁 Presiona ENTER para cerrar el programa...")

def main():
    """Función principal del programa"""
    app = CumpleC()
    
    # Verificar la fecha para determinar la fase
    fecha_actual = datetime.now()
    
    print("🎂 ¡CumpleC - Hackathon Emocional! 🎂")
    print("=" * 50)
    
    if fecha_actual.day == 18 and fecha_actual.month == 7:
        print("📅 Fase 1: Día del Pádel")
        app.fase_1()
    elif fecha_actual.day == 19 and fecha_actual.month == 7:
        print("📅 Fase 2: Día de las Pistas")
        app.fase_2()
    else:
        print("📅 Fecha no programada para el desafío.")
        print("💡 El desafío está programado para el 18 y 19 de Julio.")
        input("\nPresiona ENTER para salir...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego, Constantino!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("Presiona ENTER para salir...") 
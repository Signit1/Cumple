#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de prueba para CumpleC
Permite probar ambas fases sin depender de las fechas específicas.
"""

import sys
import os

# Agregar el directorio actual al path para importar cumplec
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cumplec import CumpleC

def test_fase_1():
    """Prueba la Fase 1 del programa"""
    print("🧪 PROBANDO FASE 1 - DÍA DEL PÁDEL")
    print("=" * 50)
    
    app = CumpleC()
    app.fase_1()

def test_fase_2():
    """Prueba la Fase 2 del programa"""
    print("🧪 PROBANDO FASE 2 - DÍA DE LAS PISTAS")
    print("=" * 50)
    
    app = CumpleC()
    app.fase_2()

def main():
    """Función principal del script de prueba"""
    print("🎂 CumpleC - Script de Prueba")
    print("=" * 50)
    print("Este script te permite probar ambas fases del programa.")
    print()
    
    while True:
        print("¿Qué fase quieres probar?")
        print("1. Fase 1 - Día del Pádel")
        print("2. Fase 2 - Día de las Pistas")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            test_fase_1()
        elif opcion == "2":
            test_fase_2()
        elif opcion == "3":
            print("\n👋 ¡Hasta luego!")
            break
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")
        
        input("\nPresiona ENTER para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("Presiona ENTER para salir...") 
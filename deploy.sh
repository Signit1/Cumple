#!/bin/bash

# 🚀 Script de Despliegue Automático - CumpleC
# Este script facilita el despliegue en diferentes plataformas

echo "🏎️ CumpleC - Script de Despliegue Automático"
echo "=============================================="

# Verificar que la carpeta build existe
if [ ! -d "build" ]; then
    echo "❌ Error: La carpeta 'build' no existe."
    echo "💡 Ejecuta primero: mkdir build && cp *.html *.css *.js build/"
    exit 1
fi

# Función para mostrar el menú
show_menu() {
    echo ""
    echo "🌐 Selecciona la plataforma de despliegue:"
    echo "1) 📦 GitHub Pages"
    echo "2) ⚡ Netlify (Drag & Drop)"
    echo "3) 🚀 Vercel"
    echo "4) 🔥 Firebase Hosting"
    echo "5) 📋 Mostrar contenido de build/"
    echo "6) 🧪 Probar localmente"
    echo "7) ❌ Salir"
    echo ""
    read -p "Selecciona una opción (1-7): " choice
}

# Función para GitHub Pages
deploy_github_pages() {
    echo "📦 Desplegando en GitHub Pages..."
    echo ""
    echo "Pasos a seguir:"
    echo "1. Subir la carpeta build al repositorio:"
    echo "   git add build/"
    echo "   git commit -m '📦 Build para despliegue'"
    echo "   git push origin main"
    echo ""
    echo "2. Configurar en GitHub:"
    echo "   - Ve a Settings > Pages"
    echo "   - Source: Deploy from a branch"
    echo "   - Branch: main, Folder: /build"
    echo ""
    echo "3. URL resultante: https://signit1.github.io/CumpleC/"
    echo ""
    read -p "Presiona ENTER cuando hayas completado los pasos..."
}

# Función para Netlify
deploy_netlify() {
    echo "⚡ Desplegando en Netlify..."
    echo ""
    echo "Pasos a seguir:"
    echo "1. Ve a https://netlify.com"
    echo "2. Arrastra la carpeta 'build' al área de deploy"
    echo "3. ¡Listo! Tu app estará online en segundos"
    echo ""
    echo "💡 Alternativa con CLI:"
    echo "   npm install -g netlify-cli"
    echo "   netlify deploy --dir=build --prod"
    echo ""
    read -p "Presiona ENTER cuando hayas completado los pasos..."
}

# Función para Vercel
deploy_vercel() {
    echo "🚀 Desplegando en Vercel..."
    echo ""
    echo "Pasos a seguir:"
    echo "1. Ve a https://vercel.com"
    echo "2. Conecta tu repositorio de GitHub"
    echo "3. Selecciona la carpeta 'build' como directorio raíz"
    echo "4. Deploy automático"
    echo ""
    echo "💡 Alternativa con CLI:"
    echo "   npm install -g vercel"
    echo "   cd build && vercel --prod"
    echo ""
    read -p "Presiona ENTER cuando hayas completado los pasos..."
}

# Función para Firebase
deploy_firebase() {
    echo "🔥 Desplegando en Firebase Hosting..."
    echo ""
    echo "Pasos a seguir:"
    echo "1. Instalar Firebase CLI:"
    echo "   npm install -g firebase-tools"
    echo ""
    echo "2. Login y inicializar:"
    echo "   firebase login"
    echo "   firebase init hosting"
    echo "   (Selecciona la carpeta 'build' como directorio público)"
    echo ""
    echo "3. Deploy:"
    echo "   firebase deploy"
    echo ""
    read -p "Presiona ENTER cuando hayas completado los pasos..."
}

# Función para mostrar contenido
show_build_content() {
    echo "📋 Contenido de la carpeta build/:"
    echo "=================================="
    ls -la build/
    echo ""
    echo "📄 Archivos principales:"
    echo "- index.html (Página principal)"
    echo "- simular_produccion.html (Simulación)"
    echo "- styles.css (Estilos)"
    echo "- script.js (JavaScript)"
    echo ""
    echo "⚙️ Archivos de configuración:"
    echo "- .htaccess (Apache)"
    echo "- netlify.toml (Netlify)"
    echo "- vercel.json (Vercel)"
    echo "- firebase.json (Firebase)"
    echo "- deploy-config.json (Configuración general)"
    echo ""
    read -p "Presiona ENTER para continuar..."
}

# Función para probar localmente
test_locally() {
    echo "🧪 Probando localmente..."
    echo ""
    echo "Iniciando servidor local en http://localhost:8000"
    echo "Presiona Ctrl+C para detener"
    echo ""
    cd build
    python3 -m http.server 8000
}

# Bucle principal
while true; do
    show_menu
    
    case $choice in
        1)
            deploy_github_pages
            ;;
        2)
            deploy_netlify
            ;;
        3)
            deploy_vercel
            ;;
        4)
            deploy_firebase
            ;;
        5)
            show_build_content
            ;;
        6)
            test_locally
            ;;
        7)
            echo "👋 ¡Hasta luego!"
            exit 0
            ;;
        *)
            echo "❌ Opción inválida. Intenta de nuevo."
            ;;
    esac
done 
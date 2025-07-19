// CumpleC - Hackathon Emocional para Constantino
// JavaScript principal de la aplicación

class CumpleC {
    constructor() {
        this.currentPhase = 1;
        this.currentPista = 1;
        this.pistasCompletadas = 0;
        this.totalPistas = 8;
        this.riddleAttempts = 0;
        this.maxRiddleAttempts = 3;
        
        // Datos de las pistas
        this.pistas = {
            1: {
                libro: 'El Principito',
                ubicacion: 'cerca de donde el zorro comparte una gran verdad',
                frase: 'Lo esencial es invisible a los ojos.',
                mensaje: 'Dicen que lo esencial es invisible a los ojos... por suerte, yo tengo rayos X en el corazón 🤓💘\n\nPorque contigo lo veo todo: tu forma de cuidarme, de hacerme reír, de estar incluso cuando no estás.\n\nY aunque no siempre se vea, lo nuestro brilla más que cualquier cosa visible.',
                clave: 'zorro',
                claveAlternativa: 'esencial'
            },
            2: {
                            libro: 'Los Miserables',
            ubicacion: 'Capítulo 17 del primer libro',
                frase: 'El mayor de los combates es aquel que se libra contra uno mismo.',
                mensaje: 'Sé que te exiges mucho, y admiro tu constante búsqueda de mejora. Recuerda que ya has ganado muchas batallas internas y externas, y eso te hace increíblemente fuerte. Siempre estaré aquí para ti ya que somos un equipo.',
                clave: 'combates',
                claveAlternativa: 'lucha'
            },
            3: {
                libro: 'Padre Rico Padre Pobre',
                ubicacion: 'en sus principios fundamentales sobre el dinero',
                frase: 'La gente pobre y de clase media trabaja por dinero. Los ricos hacen que el dinero trabaje para ellos.',
                mensaje: 'Siempre me impresionas con tu visión y tu disciplina para lograr tus metas económicas. Sé que el dinero trabajará para ti porque estás construyendo un futuro sólido y brillante. ¡Eres un maestro en ello!',
                clave: 'ricos',
                claveAlternativa: 'dinero'
            },
            4: {
                libro: 'The Lean Startup',
                ubicacion: 'en los capítulos sobre el aprendizaje ágil',
                frase: 'The only way to win is to learn faster than anyone else.',
                mensaje: 'Esta frase te describe a la perfección. Tu insaciable sed de conocimiento y tu capacidad para adaptarte y aprender rápidamente son tus mayores superpoderes. ¡Con eso, siempre ganas!',
                clave: 'learn',
                claveAlternativa: 'faster'
            },
            5: {
                libro: 'El Negociador',
                ubicacion: 'en los capítulos sobre el arte de llegar a acuerdos',
                frase: 'El objetivo de la negociación no es la victoria, sino el acuerdo.',
                mensaje: 'Aunque eres un ganador nato, valoro aún más tu capacidad para construir puentes y encontrar soluciones que beneficien a todos. Eso es verdadero liderazgo y éxito.',
                clave: 'acuerdo',
                claveAlternativa: 'victoria'
            },
            6: {
                libro: 'How to Win Friends and Influence People',
                ubicacion: 'en sus principios para conectar con los demás',
                frase: 'To be interesting, be interested.',
                mensaje: 'Tu curiosidad genuina y tu interés por aprender de todo y de todos te hacen una persona fascinante y un líder natural. ¡Nunca dejes de inspirar!',
                clave: 'interested',
                claveAlternativa: 'friends'
            },
            7: {
                libro: 'The Psychology of Money',
                ubicacion: 'hacia la mitad del libro, donde se habla de la disciplina',
                frase: 'Tener dinero es poder; mantenerlo es disciplina.',
                mensaje: 'Tú entiendes que el verdadero poder no es solo acumular, sino gestionar con sabiduría. Tu disciplina y visión en cada aspecto de tu vida son un ejemplo para mí y para muchos. Estoy increíblemente orgullosa de ti.',
                clave: 'disciplina',
                claveAlternativa: 'poder'
            },
            8: {
                libro: 'The Lean Startup',
                ubicacion: 'en los primeros capítulos sobre cómo empezar',
                frase: 'El producto mínimo viable es tu boleto a la realidad.',
                mensaje: 'Siempre transformas tus ideas en realidades. Cada paso que das, por pequeño que parezca, es un avance hacia los gigantes proyectos que construirás. Eres un arquitecto de sueños. ¡Te amo!',
                clave: 'realidad',
                claveAlternativa: 'viable'
            }
        };

        // Mensajes del sistema
        this.mensajesSistema = {
            1: "¡Primera vuelta completada!",
            2: "¡Has superado la primera chicane! Ahora, enfrenta el desafío interno.",
            3: "¡Gran avance en el sector financiero! La próxima parada te espera.",
            4: "¡Acelera en la innovación! La siguiente señal de boxes está en.",
            5: "¡Negociando la curva perfecta! Tu próxima parada es en.",
            6: "¡Conectando con la parrilla! La última parada antes de la meta está en.",
            7: "¡Recta final hacia la sabiduría financiera! Busca en.",
            8: "¡Cruzando la línea de meta de la innovación! La última pista te espera en."
        };

        this.init();
    }

    init() {
        this.bindEvents();
        this.checkDate();
    }

    bindEvents() {
        // Botones principales
        document.getElementById('start-btn').addEventListener('click', () => this.showPhaseSelect());
        document.getElementById('test-btn').addEventListener('click', () => this.showPhaseSelect());
        document.getElementById('back-btn').addEventListener('click', () => this.showScreen('start-screen'));

        // Selección de fase
        document.querySelectorAll('.phase-card').forEach(card => {
            card.addEventListener('click', (e) => {
                const phase = e.currentTarget.dataset.phase;
                if (phase === '1') {
                    this.showPhase1();
                } else {
                    this.showPhase2();
                }
            });
        });

        // Fase 1
        document.getElementById('continue-btn').addEventListener('click', () => this.continuePhase1());

        // Fase 2 - Acertijo
        document.getElementById('submit-riddle').addEventListener('click', () => this.checkRiddle());
        document.getElementById('riddle-answer').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.checkRiddle();
        });

        // Pistas
        document.getElementById('found-card-btn').addEventListener('click', () => this.showCardContent());
        document.getElementById('submit-key').addEventListener('click', () => this.checkKey());
        document.getElementById('key-answer').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') this.checkKey();
        });

        // Pantalla final
        document.getElementById('restart-btn').addEventListener('click', () => this.restart());
    }

    checkDate() {
        const today = new Date();
        const day = today.getDate();
        const month = today.getMonth() + 1;

        if (day === 18 && month === 7) {
            // Fase 1 - Día del Pádel
            this.showPhase1();
        } else if (day === 19 && month === 7) {
            // Fase 2 - Día de las Pistas
            this.showPhase2();
        }
        // Si no es ninguna fecha específica, mostrar pantalla de inicio
    }

    showScreen(screenId) {
        // Ocultar todas las pantallas
        document.querySelectorAll('.screen').forEach(screen => {
            screen.classList.remove('active');
        });

        // Mostrar la pantalla seleccionada
        document.getElementById(screenId).classList.add('active');
    }

    showPhaseSelect() {
        this.showScreen('phase-select-screen');
    }

    showPhase1() {
        this.showScreen('phase1-screen');
    }

    showPhase2() {
        this.showScreen('phase2-screen');
        this.riddleAttempts = 0;
    }

    continuePhase1() {
        const continueBtn = document.getElementById('continue-btn');
        const loadingBtn = document.getElementById('loading-btn');

        continueBtn.style.display = 'none';
        loadingBtn.style.display = 'inline-block';

        // Simular carga
        setTimeout(() => {
            this.showFeedback('✅ Programa cargado para el 19 de Julio. ¡Que la suerte y el éxito te acompañen!', 'success');
            setTimeout(() => {
                this.showScreen('start-screen');
            }, 3000);
        }, 2000);
    }

    checkRiddle() {
        const answer = document.getElementById('riddle-answer').value.trim().toLowerCase();
        const correctAnswer = 'eau rouge';
        const feedback = document.getElementById('riddle-feedback');

        this.riddleAttempts++;

        if (answer === correctAnswer) {
            feedback.textContent = '🎉 ¡CORRECTO! ¡Has superado la primera chicane!';
            feedback.className = 'feedback success';
            feedback.style.display = 'block';
            
            setTimeout(() => {
                this.startPistas();
            }, 2000);
        } else {
            if (this.riddleAttempts < this.maxRiddleAttempts) {
                feedback.textContent = `❌ Incorrecto. Intento ${this.riddleAttempts}/${this.maxRiddleAttempts}. ¡Sigue intentando!`;
                feedback.className = 'feedback error';
            } else {
                feedback.textContent = '💡 La respuesta era: EAU ROUGE. ¡Pero no te preocupes! Continuemos con el desafío...';
                feedback.className = 'feedback hint';
                setTimeout(() => {
                    this.startPistas();
                }, 3000);
            }
            feedback.style.display = 'block';
        }

        document.getElementById('riddle-answer').value = '';
    }

    startPistas() {
        this.currentPista = 1;
        this.pistasCompletadas = 0;
        this.showPista();
    }

    showPista() {
        this.showScreen('pistas-screen');
        this.updateProgress();
        this.displayPista();
    }

    updateProgress() {
        const completedCount = document.getElementById('completed-count');
        const progressPercentage = document.getElementById('progress-percentage');
        const progressFill = document.getElementById('progress-fill');

        completedCount.textContent = this.pistasCompletadas;
        const percentage = (this.pistasCompletadas / this.totalPistas) * 100;
        progressPercentage.textContent = `${Math.round(percentage)}%`;
        progressFill.style.width = `${percentage}%`;
    }

    displayPista() {
        const pista = this.pistas[this.currentPista];
        const pistaTitle = document.getElementById('pista-title');
        const pistaNumber = document.querySelector('.pista-number');
        const pistaMessage = document.getElementById('pista-message');
        const pistaLocation = document.getElementById('pista-location');

        pistaTitle.textContent = `🏁 PISTA ${this.currentPista} - VUELTA ${this.currentPista}`;
        pistaNumber.textContent = `${this.currentPista}/${this.totalPistas}`;
        pistaMessage.textContent = this.mensajesSistema[this.currentPista];
        pistaLocation.textContent = `📚 Busca en tu librero el libro **"${pista.libro}"**, ${pista.ubicacion}.`;

        // Resetear elementos
        document.getElementById('card-content').style.display = 'none';
        document.getElementById('key-input').style.display = 'none';
        document.getElementById('key-feedback').style.display = 'none';
        document.getElementById('found-card-btn').style.display = 'inline-block';
    }

    showCardContent() {
        const pista = this.pistas[this.currentPista];
        const cardQuote = document.getElementById('card-quote');
        const cardMessage = document.getElementById('card-message');

        cardQuote.textContent = `"${pista.frase}"`;
        cardMessage.innerHTML = pista.mensaje.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

        document.getElementById('card-content').style.display = 'block';
        document.getElementById('key-input').style.display = 'block';
        document.getElementById('found-card-btn').style.display = 'none';
    }

    checkKey() {
        const key = document.getElementById('key-answer').value.trim().toLowerCase();
        const pista = this.pistas[this.currentPista];
        const feedback = document.getElementById('key-feedback');

        if (key === pista.clave || key === pista.claveAlternativa) {
            feedback.textContent = `🎉 ¡CORRECTO! ¡Pista ${this.currentPista} completada!`;
            feedback.className = 'feedback success';
            this.pistasCompletadas++;

            setTimeout(() => {
                this.nextPista();
            }, 1500);
        } else {
            feedback.textContent = '❌ Clave incorrecta. Intenta de nuevo.';
            feedback.className = 'feedback error';
        }

        feedback.style.display = 'block';
        document.getElementById('key-answer').value = '';
    }

    nextPista() {
        if (this.currentPista >= this.totalPistas) {
            this.showFinalScreen();
        } else {
            this.currentPista++;
            this.showPista();
        }
    }

    showFinalScreen() {
        this.showScreen('final-screen');
        this.createConfetti();
    }

    createConfetti() {
        const confettiContainer = document.getElementById('confetti-container');
        const colors = ['#f00', '#0f0', '#00f', '#ff0', '#f0f', '#0ff', '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4'];

        for (let i = 0; i < 100; i++) {
            setTimeout(() => {
                const confetti = document.createElement('div');
                confetti.className = 'confetti';
                confetti.style.left = Math.random() * 100 + '%';
                confetti.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];
                confetti.style.animationDelay = Math.random() * 3 + 's';
                confetti.style.animationDuration = (Math.random() * 3 + 2) + 's';
                confettiContainer.appendChild(confetti);

                // Remover confeti después de la animación
                setTimeout(() => {
                    confetti.remove();
                }, 5000);
            }, i * 50);
        }
    }

    showFeedback(message, type) {
        // Crear elemento de feedback temporal
        const feedback = document.createElement('div');
        feedback.className = `feedback ${type}`;
        feedback.textContent = message;
        feedback.style.position = 'fixed';
        feedback.style.top = '20px';
        feedback.style.left = '50%';
        feedback.style.transform = 'translateX(-50%)';
        feedback.style.zIndex = '1000';
        feedback.style.padding = '15px 30px';
        feedback.style.borderRadius = '10px';
        feedback.style.fontWeight = 'bold';

        document.body.appendChild(feedback);

        setTimeout(() => {
            feedback.remove();
        }, 3000);
    }

    restart() {
        this.currentPhase = 1;
        this.currentPista = 1;
        this.pistasCompletadas = 0;
        this.riddleAttempts = 0;
        this.showScreen('start-screen');
    }
}

// Inicializar la aplicación cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    new CumpleC();
});

// Función para manejar errores
window.addEventListener('error', (e) => {
    console.error('Error en la aplicación:', e.error);
    alert('Ha ocurrido un error. Por favor, recarga la página.');
});

// Función para prevenir el zoom en dispositivos móviles
document.addEventListener('touchstart', (e) => {
    if (e.touches.length > 1) {
        e.preventDefault();
    }
}, { passive: false });

// Función para mejorar la experiencia en dispositivos móviles
let lastTouchEnd = 0;
document.addEventListener('touchend', (e) => {
    const now = (new Date()).getTime();
    if (now - lastTouchEnd <= 300) {
        e.preventDefault();
    }
    lastTouchEnd = now;
}, false); 
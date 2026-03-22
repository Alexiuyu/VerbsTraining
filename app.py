import streamlit as st
import random

# Configuración de la página
st.set_page_config(
    page_title="Entrenador de Verbos en Inglés",
    page_icon="🎓",
    layout="wide"
)

# CSS y JavaScript personalizado
st.markdown("""
<style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px;
    }
    .success-box {
        padding: 20px;
        border-radius: 5px;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .error-box {
        padding: 20px;
        border-radius: 5px;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .verb-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #e7f3ff;
        border-left: 5px solid #2196F3;
        margin: 10px 0;
    }
    h1 {
        color: #2196F3;
        text-align: center;
    }
    .stProgress > div > div > div > div {
        background-color: #4CAF50;
    }
    
    /* Estilos para la tabla de errores */
    .error-review {
        background-color: #e3f2fd;
        border: 2px solid #2196F3;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
    }
    .error-item {
        background-color: white;
        border-left: 4px solid #dc3545;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .error-verb {
        font-weight: bold;
        color: #2196F3;
        font-size: 1.2em;
        margin-bottom: 10px;
    }
    .error-detail {
        margin: 5px 0;
        padding: 5px;
    }
    .wrong-answer {
        color: #dc3545;
        font-weight: bold;
    }
    .correct-answer {
        color: #28a745;
        font-weight: bold;
    }
    .field-name {
        color: #6c757d;
        font-style: italic;
    }
    
    /* Estilos para botones de nivel */
    .nivel-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 20px 40px;
        border-radius: 15px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        transition: transform 0.2s, box-shadow 0.2s;
        margin: 10px;
    }
    .nivel-button:hover {
        transform: translateY(-3px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* OCULTAR el placeholder "Press Enter to submit form" */
    input[placeholder="Press Enter to submit form"]::placeholder {
        color: transparent !important;
    }
    input[placeholder="Press Enter to submit form"] {
        color: inherit !important;
    }
    
    /* Badge de nivel */
    .nivel-badge {
        display: inline-block;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 14px;
        margin: 10px 0;
    }
    .nivel-1-2 {
        background-color: #4CAF50;
        color: white;
    }
    .nivel-3-4 {
        background-color: #FF9800;
        color: white;
    }
</style>

<script>
(function() {
    function setupEnterAsTab() {
        setTimeout(() => {
            const inputs = document.querySelectorAll('input[type="text"]:not([aria-label=""])');
            
            inputs.forEach((input, index) => {
                const newInput = input.cloneNode(true);
                input.parentNode.replaceChild(newInput, input);
                
                newInput.addEventListener('keydown', function(e) {
                    if (e.key === 'Enter') {
                        e.preventDefault();
                        e.stopPropagation();
                        
                        const form = this.closest('form');
                        if (form) {
                            e.preventDefault();
                        }
                        
                        const currentInputs = document.querySelectorAll('input[type="text"]:not([aria-label=""])');
                        const currentIndex = Array.from(currentInputs).indexOf(this);
                        
                        if (currentIndex >= 0 && currentIndex < currentInputs.length - 1) {
                            const nextInput = currentInputs[currentIndex + 1];
                            nextInput.focus();
                            nextInput.select();
                        }
                        
                        return false;
                    }
                }, true);
                
                const form = newInput.closest('form');
                if (form && !form.dataset.enterHandled) {
                    form.dataset.enterHandled = 'true';
                    form.addEventListener('submit', function(e) {
                        if (!e.submitter || e.submitter.type !== 'submit') {
                            e.preventDefault();
                            return false;
                        }
                    }, true);
                }
            });
        }, 300);
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupEnterAsTab);
    } else {
        setupEnterAsTab();
    }
    
    const observer = new MutationObserver(setupEnterAsTab);
    observer.observe(document.body, { childList: true, subtree: true });
    
    setInterval(setupEnterAsTab, 1000);
})();
</script>
""", unsafe_allow_html=True)

# 📚 BASE DE DATOS DE VERBOS - NIVEL 1º-2º ESO
VERBOS_1_2 = {
    "ser/estar": ["be", "was/were", "been"],
    "convertirse": ["become", "became", "become"],
    "empezar": ["begin", "began", "begun"],
    "romper": ["break", "broke", "broken"],
    "traer": ["bring", "brought", "brought"],
    "construir": ["build", "built", "built"],
    "comprar": ["buy", "bought", "bought"],
    "capturar/atrapar": ["catch", "caught", "caught"],
    "elegir": ["choose", "chose", "chosen"],
    "venir": ["come", "came", "come"],
    "cortar": ["cut", "cut", "cut"],
    "hacer (deporte)": ["do", "did", "done"],
    "beber": ["drink", "drank", "drunk"],
    "conducir": ["drive", "drove", "driven"],
    "comer": ["eat", "ate", "eaten"],
    "caer": ["fall", "fell", "fallen"],
    "alimentar": ["feed", "fed", "fed"],
    "sentir": ["feel", "felt", "felt"],
    "encontrar": ["find", "found", "found"],
    "volar": ["fly", "flew", "flown"],
    "olvidar": ["forget", "forgot", "forgotten"],
    "conseguir": ["get", "got", "got"],
    "dar": ["give", "gave", "given"],
    "ir": ["go", "went", "gone"],
    "crecer": ["grow", "grew", "grown"],
    "colgar": ["hang", "hung", "hung"],
    "tener": ["have", "had", "had"],
    "escuchar": ["hear", "heard", "heard"],
    "golpear": ["hit", "hit", "hit"],
    "mantener": ["keep", "kept", "kept"],
    "saber": ["know", "knew", "known"],
    "tumbar": ["lay", "laid", "laid"],
    "aprender": ["learn", "learnt/learned", "learnt/learned"],
    "abandonar": ["leave", "left", "left"],
    "dejar": ["let", "let", "let"],
    "perder": ["lose", "lost", "lost"],
    "hacer (tarta)": ["make", "made", "made"],
    "conocer (a alguien)": ["meet", "met", "met"],
    "pagar": ["pay", "paid", "paid"],
    "poner": ["put", "put", "put"],
    "leer": ["read", "read", "read"],
    "montar": ["ride", "rode", "ridden"],
    "sonar (teléfono)": ["ring", "rang", "rung"],
    "correr": ["run", "ran", "run"],
    "decir": ["say", "said", "said"],
    "ver": ["see", "saw", "seen"],
    "vender": ["sell", "sold", "sold"],
    "enviar": ["send", "sent", "sent"],
    "brillar": ["shine", "shone", "shone"],
    "cantar": ["sing", "sang", "sung"],
    "sentar": ["sit", "sat", "sat"],
    "dormir": ["sleep", "slept", "slept"],
    "hablar": ["speak", "spoke", "spoken"],
    "gastar": ["spend", "spent", "spent"],
    "barrer": ["sweep", "swept", "swept"],
    "nadar": ["swim", "swam", "swum"],
    "coger/tomar": ["take", "took", "taken"],
    "enseñar": ["teach", "taught", "taught"],
    "contar (historia)": ["tell", "told", "told"],
    "pensar": ["think", "thought", "thought"],
    "lanzar": ["throw", "threw", "thrown"],
    "entender": ["understand", "understood", "understood"],
    "despertar": ["wake", "woke", "woken"],
    "ganar": ["win", "won", "won"],
    "escribir": ["write", "wrote", "written"]
}

# 📚 BASE DE DATOS DE VERBOS - NIVEL 3º-4º ESO
VERBOS_3_4 = {
    "ser/estar": ["be", "was/were", "been"],
    "golpear/pegar": ["beat", "beat", "beaten"],
    "convertirse": ["become", "became", "become"],
    "empezar": ["begin", "began", "begun"],
    "apostar": ["bet", "bet", "bet"],
    "romper": ["break", "broke", "broken"],
    "traer": ["bring", "brought", "brought"],
    "transmitir": ["broadcast", "broadcast", "broadcast"],
    "construir": ["build", "built", "built"],
    "comprar": ["buy", "bought", "bought"],
    "capturar/atrapar": ["catch", "caught", "caught"],
    "elegir": ["choose", "chose", "chosen"],
    "venir": ["come", "came", "come"],
    "costar": ["cost", "cost", "cost"],
    "cortar": ["cut", "cut", "cut"],
    "hacer": ["do", "did", "done"],
    "dibujar": ["draw", "drew", "drawn"],
    "beber": ["drink", "drank", "drunk"],
    "conducir": ["drive", "drove", "driven"],
    "comer": ["eat", "ate", "eaten"],
    "caer": ["fall", "fell", "fallen"],
    "alimentar": ["feed", "fed", "fed"],
    "sentir": ["feel", "felt", "felt"],
    "pelear": ["fight", "fought", "fought"],
    "encontrar": ["find", "found", "found"],
    "volar": ["fly", "flew", "flown"],
    "olvidar": ["forget", "forgot", "forgotten"],
    "conseguir": ["get", "got", "got"],
    "dar": ["give", "gave", "given"],
    "ir": ["go", "went", "gone"],
    "crecer": ["grow", "grew", "grown"],
    "colgar": ["hang", "hung", "hung"],
    "tener": ["have", "had", "had"],
    "escuchar": ["hear", "heard", "heard"],
    "golpear": ["hit", "hit", "hit"],
    "sostener": ["hold", "held", "held"],
    "herir": ["hurt", "hurt", "hurt"],
    "mantener": ["keep", "kept", "kept"],
    "saber": ["know", "knew", "known"],
    "colocar/tumbar": ["lay", "laid", "laid"],
    "aprender": ["learn", "learnt/learned", "learnt/learned"],
    "abandonar": ["leave", "left", "left"],
    "dejar": ["let", "let", "let"],
    "perder": ["lose", "lost", "lost"],
    "hacer/crear": ["make", "made", "made"],
    "significar": ["mean", "meant", "meant"],
    "conocer": ["meet", "met", "met"],
    "pagar": ["pay", "paid", "paid"],
    "poner": ["put", "put", "put"],
    "leer": ["read", "read", "read"],
    "montar": ["ride", "rode", "ridden"],
    "sonar": ["ring", "rang", "rung"],
    "correr": ["run", "ran", "run"],
    "decir": ["say", "said", "said"],
    "ver": ["see", "saw", "seen"],
    "vender": ["sell", "sold", "sold"],
    "enviar": ["send", "sent", "sent"],
    "colocar": ["set", "set", "set"],
    "brillar": ["shine", "shone/shined", "shone/shined"],
    "mostrar": ["show", "showed", "shown"],
    "cantar": ["sing", "sang", "sung"],
    "sentar": ["sit", "sat", "sat"],
    "dormir": ["sleep", "slept", "slept"],
    "hablar": ["speak", "spoke", "spoken"],
    "gastar": ["spend", "spent", "spent"],
    "estar de pie": ["stand", "stood", "stood"],
    "robar": ["steal", "stole", "stolen"],
    "pegar": ["stick", "stuck", "stuck"],
    "barrer": ["sweep", "swept", "swept"],
    "nadar": ["swim", "swam", "swum"],
    "coger/tomar": ["take", "took", "taken"],
    "enseñar": ["teach", "taught", "taught"],
    "contar": ["tell", "told", "told"],
    "pensar": ["think", "thought", "thought"],
    "lanzar": ["throw", "threw", "thrown"],
    "entender": ["understand", "understood", "understood"],
    "despertar": ["wake", "woke", "woken"],
    "llevar puesto": ["wear", "wore", "worn"],
    "ganar": ["win", "won", "won"],
    "escribir": ["write", "wrote", "written"]
}

def validar_respuesta(respuesta_usuario, respuesta_correcta):
    respuesta_usuario = respuesta_usuario.lower().strip()
    respuesta_correcta = respuesta_correcta.lower()
    
    # ✅ COINCIDENCIA EXACTA (caso general)
    if respuesta_usuario == respuesta_correcta:
        return True
    
    # ⚠️ CASO ESPECIAL: "was/were" debe escribirse LITERALMENTE
    if respuesta_correcta == "was/were":
        return False
    
    # ✅ CASO ESPECIAL: "gotten/got" acepta también solo "got"
    if respuesta_correcta == "gotten/got" and respuesta_usuario == "got":
        return True
    
    # ✅ Para otras respuestas con "/" como "learnt/learned" o "shone/shined", aceptar cualquiera
    if "/" in respuesta_correcta:
        opciones = [opcion.strip() for opcion in respuesta_correcta.split("/")]
        if respuesta_usuario in opciones:
            return True
    
    return False

# Inicializar estado de sesión
if 'nivel_seleccionado' not in st.session_state:
    st.session_state.nivel_seleccionado = None
if 'ronda' not in st.session_state:
    st.session_state.ronda = 1
if 'baraja' not in st.session_state:
    st.session_state.baraja = []
if 'verbos_usados' not in st.session_state:
    st.session_state.verbos_usados = []
if 'puntuacion' not in st.session_state:
    st.session_state.puntuacion = 0
if 'total_preguntas' not in st.session_state:
    st.session_state.total_preguntas = 0
if 'indice_verbo_actual' not in st.session_state:
    st.session_state.indice_verbo_actual = 0
if 'cantidad_verbos' not in st.session_state:
    st.session_state.cantidad_verbos = 0
if 'inicio' not in st.session_state:
    st.session_state.inicio = False
if 'errores_ronda' not in st.session_state:
    st.session_state.errores_ronda = []

def seleccionar_nivel(nivel):
    st.session_state.nivel_seleccionado = nivel
    st.session_state.inicio = False
    st.session_state.ronda = 1
    st.session_state.baraja = []
    st.session_state.verbos_usados = []
    st.session_state.puntuacion = 0
    st.session_state.total_preguntas = 0
    st.session_state.indice_verbo_actual = 0
    st.session_state.cantidad_verbos = 0
    st.session_state.errores_ronda = []

def iniciar_nueva_sesion(cantidad):
    verbos = VERBOS_1_2 if st.session_state.nivel_seleccionado == "1-2" else VERBOS_3_4
    st.session_state.baraja = list(verbos.items())
    random.shuffle(st.session_state.baraja)
    st.session_state.baraja = st.session_state.baraja[:cantidad]
    st.session_state.verbos_usados = []
    st.session_state.puntuacion = 0
    st.session_state.total_preguntas = 0
    st.session_state.indice_verbo_actual = 0
    st.session_state.cantidad_verbos = cantidad
    st.session_state.errores_ronda = []
    st.session_state.inicio = True

def resetear_todo():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.ronda = 1
    st.session_state.nivel_seleccionado = None

def mostrar_repaso_errores():
    """Muestra los verbos en los que el usuario falló"""
    st.markdown("---")
    st.markdown("## 📚 Repaso de Errores")
    
    if not st.session_state.errores_ronda:
        st.success("🎉 ¡Perfecto! No tuviste ningún error en esta ronda.")
        return
    
    st.markdown(f"""
    <div class='error-review'>
        <h3>⚠️ Verbos que necesitas practicar ({len(st.session_state.errores_ronda)} errores)</h3>
        <p>Repasa estos verbos para mejorar tu puntuación en la próxima ronda:</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Agrupar errores por verbo
    verbos_con_errores = {}
    for error in st.session_state.errores_ronda:
        verbo = error['verbo_espanol']
        if verbo not in verbos_con_errores:
            verbos_con_errores[verbo] = []
        verbos_con_errores[verbo].append(error)
    
    # Mostrar cada verbo con sus errores
    for verbo, errores in verbos_con_errores.items():
        st.markdown(f"""
        <div class='error-item'>
            <div class='error-verb'>📌 {verbo.upper()}</div>
        </div>
        """, unsafe_allow_html=True)
        
        for error in errores:
            st.markdown(f"""
            <div style='margin-left: 20px; margin-bottom: 10px;'>
                <div class='error-detail'>
                    <span class='field-name'>{error['campo']}:</span><br>
                    ❌ Tu respuesta: <span class='wrong-answer'>{error['respuesta_usuario']}</span><br>
                    ✅ Correcto: <span class='correct-answer'>{error['respuesta_correcta']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("")

# ==================== PANTALLA DE SELECCIÓN DE NIVEL ====================
if st.session_state.nivel_seleccionado is None:
    st.title("🎓 Entrenador de Verbos en Inglés")
    st.markdown("---")
    
    st.markdown("""
    <div style='text-align: center; padding: 30px;'>
        <h2 style='color: #2196F3;'>👋 ¡Bienvenido!</h2>
        <p style='font-size: 18px; color: #666;'>Selecciona tu nivel para comenzar a practicar</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Dos columnas: cada una con botón + características debajo
    col_nivel1, col_nivel2 = st.columns(2)
    
    with col_nivel1:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #e8f5e9; border-radius: 15px; margin: 10px;'>
            <h3 style='color: #4CAF50;'>📘 Nivel 1º-2º ESO</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📘 1º-2º ESO", use_container_width=True, key="btn_nivel_1_2", type="primary"):
            seleccionar_nivel("1-2")
            st.rerun()
        
        st.markdown("""
        <div style='text-align: center; padding: 15px; margin-top: 15px; background-color: #f5f5f5; border-radius: 10px;'>
            <p style='color: #333;'><strong>✅ 65 verbos</strong> esenciales</p>
            <p style='color: #333;'>✅ Los más comunes y utilizados</p>
            <p style='color: #333;'>✅ Ideal para empezar</p>
            <p style='color: #333;'>✅ Verbos del día a día</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_nivel2:
        st.markdown("""
        <div style='text-align: center; padding: 20px; background-color: #fff3e0; border-radius: 15px; margin: 10px;'>
            <h3 style='color: #FF9800;'>📙 Nivel 3º-4º ESO</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📙 3º-4º ESO", use_container_width=True, key="btn_nivel_3_4", type="primary"):
            seleccionar_nivel("3-4")
            st.rerun()
        
        st.markdown("""
        <div style='text-align: center; padding: 15px; margin-top: 15px; background-color: #f5f5f5; border-radius: 10px;'>
            <p style='color: #333;'><strong>✅ 75 verbos</strong> (incluye 1º-2º)</p>
            <p style='color: #333;'>✅ Verbos más avanzados</p>
            <p style='color: #333;'>✅ Más experiencia requerida</p>
            <p style='color: #333;'>✅ Verbos menos comunes</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.info("⌨️ **Consejo:** Enter cambia de casilla | Tab también funciona")

# ==================== PANTALLA DE JUEGO ====================
else:
    # Determinar qué verbos usar según el nivel
    verbos_actuales = VERBOS_1_2 if st.session_state.nivel_seleccionado == "1-2" else VERBOS_3_4
    nombre_nivel = "1º-2º ESO" if st.session_state.nivel_seleccionado == "1-2" else "3º-4º ESO"
    clase_nivel = "nivel-1-2" if st.session_state.nivel_seleccionado == "1-2" else "nivel-3-4"
    
    # Título con badge de nivel
    st.title("🎓 Entrenador de Verbos en Inglés")
    st.markdown(f"<span class='nivel-badge {clase_nivel}'>📚 Nivel: {nombre_nivel}</span>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Botón para cambiar de nivel (siempre visible)
    if st.button("🔄 Cambiar de Nivel", key="btn_cambiar_nivel"):
        resetear_todo()
        st.rerun()
    
    if not st.session_state.inicio:
        # Pantalla de configuración de cantidad
        st.markdown("### ¡Perfecto! Ahora configura tu sesión")
        st.markdown(f"**Total de verbos disponibles ({nombre_nivel}):** {len(verbos_actuales)}")
        st.markdown("")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            cantidad = st.number_input(
                "¿Cuántos verbos deseas practicar?",
                min_value=1,
                max_value=len(verbos_actuales),
                value=min(10, len(verbos_actuales)),
                step=1,
                key="cantidad_input"
            )
        
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🚀 Comenzar", type="primary", key="btn_comenzar"):
                iniciar_nueva_sesion(int(cantidad))
                st.rerun()
        
        st.markdown("---")
        st.info("💡 **Consejo:** Cuando veas '/' en la respuesta, puedes escribir cualquiera de las opciones (ej: 'learnt' o 'learned')")
        st.info("⚠️ **Excepción:** 'was/were' debe escribirse completo con la barra")
        st.markdown("⌨️ **Enter** cambia de casilla | **Tab** también funciona")

    else:
        # Barra de progreso
        progreso = st.session_state.indice_verbo_actual / st.session_state.cantidad_verbos
        st.progress(progreso)
        st.markdown(f"**Progreso:** {st.session_state.indice_verbo_actual}/{st.session_state.cantidad_verbos} | Ronda #{st.session_state.ronda}")
        
        # Verificar si terminó la sesión
        if st.session_state.indice_verbo_actual >= len(st.session_state.baraja):
            # Mostrar estadísticas
            st.markdown("<div class='success-box'>", unsafe_allow_html=True)
            st.markdown("## 🎉 ¡Sesión Completada!")
            st.markdown(f"**Verbos perfectos:** {st.session_state.puntuacion} de {st.session_state.total_preguntas}")
            
            if st.session_state.total_preguntas > 0:
                porcentaje = (st.session_state.puntuacion / st.session_state.total_preguntas) * 100
                st.markdown(f"**Porcentaje de éxito:** {porcentaje:.1f}%")
            
            st.markdown("</div>", unsafe_allow_html=True)
            
            # 📚 MOSTRAR REPASO DE ERRORES
            mostrar_repaso_errores()
            
            st.markdown("---")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 Otra Ronda", type="primary", key="btn_otra_ronda"):
                    st.session_state.ronda += 1
                    iniciar_nueva_sesion(st.session_state.cantidad_verbos)
                    st.rerun()
            with col2:
                if st.button("🏠 Cambiar Nivel", type="secondary", key="btn_inicio"):
                    resetear_todo()
                    st.rerun()
        
        else:
            # Mostrar verbo actual
            espanol, respuestas_correctas = st.session_state.baraja[st.session_state.indice_verbo_actual]
            
            st.markdown(f"<div class='verb-card'>", unsafe_allow_html=True)
            st.markdown(f"### {espanol.upper()}")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # Crear IDs únicos para los inputs
            input_keys = {
                'inf': f"inf_{st.session_state.indice_verbo_actual}",
                'past': f"past_{st.session_state.indice_verbo_actual}",
                'part': f"part_{st.session_state.indice_verbo_actual}"
            }
            
            # Formulario para respuestas
            with st.form(key=f"forma_verbo_{st.session_state.indice_verbo_actual}", clear_on_submit=False):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    resp_infinitivo = st.text_input("Infinitivo", key=input_keys['inf'], autocomplete="off")
                with col2:
                    resp_pasado = st.text_input("Pasado Simple", key=input_keys['past'], autocomplete="off")
                with col3:
                    resp_participio = st.text_input("Pasado Participio", key=input_keys['part'], autocomplete="off")
                
                submitted = st.form_submit_button("✅ Verificar Respuesta", type="primary", use_container_width=True)
                
                if submitted:
                    respuestas_usuario = [resp_infinitivo, resp_pasado, resp_participio]
                    nombres_campos = ["Infinitivo", "Pasado Simple", "Pasado Participio"]
                    
                    st.markdown("---")
                    st.markdown("### Resultados:")
                    
                    aciertos = 0
                    errores_en_verbo = []
                    
                    for i in range(3):
                        if validar_respuesta(respuestas_usuario[i], respuestas_correctas[i]):
                            st.success(f"✅ {nombres_campos[i]}: '{respuestas_usuario[i]}' - Correcto")
                            aciertos += 1
                        else:
                            st.error(f"❌ {nombres_campos[i]}: '{respuestas_usuario[i]}' - Incorrecto")
                            st.info(f"→ Respuesta correcta: {respuestas_correctas[i]}")
                            
                            # Guardar el error
                            errores_en_verbo.append({
                                'verbo_espanol': espanol,
                                'campo': nombres_campos[i],
                                'respuesta_usuario': respuestas_usuario[i] if respuestas_usuario[i] else '(vacío)',
                                'respuesta_correcta': respuestas_correctas[i]
                            })
                    
                    # Añadir errores a la lista global de errores
                    if errores_en_verbo:
                        st.session_state.errores_ronda.extend(errores_en_verbo)
                    
                    st.session_state.total_preguntas += 1
                    if aciertos == 3:
                        st.balloons()
                        st.markdown("<div class='success-box'>", unsafe_allow_html=True)
                        st.markdown("### 🌟 ¡Perfecto! 3/3 aciertos")
                        st.markdown("</div>", unsafe_allow_html=True)
                        st.session_state.puntuacion += 1
                    else:
                        st.warning(f"📊 Resultado: {aciertos}/3")
                    
                    st.session_state.verbos_usados.append(espanol)
                    st.session_state.indice_verbo_actual += 1
                    st.rerun()

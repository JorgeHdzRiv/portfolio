import streamlit as st
import pandas as pd
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="DS Portfolio",
    page_icon="🚀",
    layout="wide"
)

# 2. NAVEGACIÓN CON ICONOS
with st.sidebar:
    st.title("📂 Menú")
    opcion = st.radio(
        "Ir a:",
        ["👤 Sobre Mí", "🛠️ Habilidades", "💻 Catálogo de Proyectos", "📧 Contacto"],
        index=0 # Empezar en Proyectos por defecto
    )

# ==========================================
# SECCIÓN: SOBRE MÍ
# ==========================================
if "Sobre Mí" in opcion:
    st.title("Jorge Hernández Rivera")
    st.markdown('<p style="font-size: 20px; color: #4B5563;">Analista de Datos | Ingeniero en Sistemas</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        Soy un Ingeniero en Sistemas especializado en el **análisis de datos, soporte IT y la automatización de procesos**. 
        Mi enfoque principal es asegurar la integridad de la información a gran escala y transformar datos complejos en 
        soluciones operativas mediante el uso de **Python y SQL**.
        
        A lo largo de mi trayectoria, he colaborado en entornos de alto rigor estadístico como el **INEGI (Censo Económico 2024 y Encuesta Intercensal 2025)**, 
        asegurando la calidad, precisión y continuidad en la recolección de grandes volúmenes de datos. Asimismo, en el sector privado, 
        he liderado la optimización logística y la creación de tableros directivos utilizando herramientas como **PowerBI y Looker Studio**.
        
        Además de mi perfil técnico, cuento con amplia experiencia en la **capacitación corporativa y soporte remoto**, 
        lo que me permite traducir conceptos técnicos complejos en herramientas accesibles para los usuarios finales, 
        facilitando la adopción tecnológica y el aprendizaje en entornos digitales.
        """)
        
    with col2:
        st.info("📍 **Ubicación:** Irapuato, Guanajuato (Disponible Remoto)")
        st.success("🎓 **Formación:** Ingeniería en Sistemas Computacionales | Ing. en Sistemas Automotrices")
        st.warning("🗣️ **Idiomas:** Español (Nativo), Inglés (B1 Intermedio)")
        
        # Botón para descargar tu CV (Opcional, muy recomendado)
        st.download_button(
             label="📄 Descargar CV",
             data=open("./docs/CV_JORGEHERNANDEZ.pdf", "rb").read(),
             file_name="CV_Jorge_Hernandez_Data_Analyst.pdf",
             mime="application/pdf"
        )
    # --- NUEVO ELEMENTO VISUAL AL FINAL ---
    st.divider() # Una línea sutil para separar el texto del gráfico
    
    st.markdown('<p class="section-header" style="font-size: 24px; font-weight: bold;">📊 Visualizando el impacto</p>', unsafe_allow_html=True)
    st.write("Un pequeño vistazo interactivo simulando tendencias de optimización y modelado predictivo.")
    
    # OPCIÓN 1: GRÁFICO INTERACTIVO NATIVO (Recomendado)
    # Generamos datos aleatorios simulando el rendimiento de un modelo a lo largo del tiempo
    chart_data = pd.DataFrame(
        np.random.randn(50, 3).cumsum(axis=0), # cumsum hace que la gráfica parezca una tendencia real
        columns=['Análisis Exploratorio', 'Modelado Predictivo', 'Optimización de Procesos']
    )
    
    # Streamlit renderiza esto como un gráfico interactivo precioso
    st.line_chart(chart_data)
    st.image("https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3hheTV5Ym5vaHdrZzRhdTV0YmJnNW81cDB2MjNnZmlzOTM0cnBuYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KX5nwoDX97AtPvKBF6/giphy.gif", width='stretch')

# ==========================================
# SECCIÓN: HABILIDADES
# ==========================================
elif "Habilidades" in opcion:
    st.title("🛠️ Mi Arsenal Tecnológico")
    st.write("Una representación visual de las herramientas, metodologías y credenciales que domino para transformar datos en impacto.")
    st.divider()
    
    # Creación de pestañas para organizar la información visualmente
    tab1, tab2, tab3 = st.tabs(["📊 Tecnologías & Código", "📜 Certificaciones", "🧠 Competencias Profesionales"])
    
    with tab1:
        st.write("### ") # Espaciador sutil
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🐍 Ciencia de Datos & Programación")
            
            st.write("**Python Avanzado** (Pandas, NumPy, Scikit-Learn)")
            st.progress(0.90)
            
            st.write("**Ecosistema de Visualización** (Plotly, Seaborn, Matplotlib)")
            st.progress(0.85)
            
            st.write("**Bases de Datos & SQL** (MySQL, Consultas complejas y extracción)")
            st.progress(0.85)
            
            st.write("**Desarrollo y Estructuras Core** (Java, HTML/CSS)")
            st.progress(0.65)
            
        with col2:
            st.markdown("#### 📈 Business Intelligence & Despliegue")
            
            st.write("**Visualización Estratégica** (PowerBI, Looker Studio, Tableau)")
            st.progress(0.90)
            
            st.write("**Análisis de Datos Tradicional** (Excel Avanzado, Tablas Dinámicas, Macros)")
            st.progress(0.85)
            
            st.write("**Aplicaciones de Datos** (Streamlit Framework)")
            st.progress(0.80)
            
            st.write("**Entornos y Control de Versiones** (Git, GitHub, Administración en Linux)")
            st.progress(0.75)
            
    with tab2:
        st.write("### ")
        st.markdown("#### 🏆 Respaldo Profesional e Internacional")
        st.write("Credenciales teóricas y prácticas obtenidas a través de academias globales e instituciones técnicas:")
        st.write("### ")
        
        # Grid de certificaciones en dos columnas
        cert_col1, cert_col2 = st.columns(2)
        
        with cert_col1:
            with st.container(border=True):
                st.markdown("🥇 **Google Data Analytics Professional Certificate**")
                st.caption("Emisor: Google & Coursera — Especialización en el ciclo completo de análisis de datos.")
                
            with st.container(border=True):
                st.markdown("🚀 **Bootcamp Data Science con I.A. Aplicada**")
                st.caption("Emisor: Alura Latam — Modelado de modelos predictivos y algoritmos avanzados.")
                
            with st.container(border=True):
                st.markdown("🐍 **PCEP: Certified Python Programmer**")
                st.caption("Emisor: Python Institute — Certificación oficial en fundamentos y lógica de programación.")
                
        with cert_col2:
            with st.container(border=True):
                st.markdown("💼 **Professional Certificate in Data Analytics**")
                st.caption("Emisor: IBM & Coursera *(En curso)* — Enfoque profundo en ciencia de datos aplicada.")
                
            with st.container(border=True):
                st.markdown("📊 **Python para Análisis de Datos**")
                st.caption("Emisor: IECA Irapuato — Desarrollo local enfocado en manipulación de dataframes.")

    with tab3:
        st.write("### ")
        st.markdown("#### 💡 Enfoque Humano y Gestión de Proyectos")
        st.write("Habilidades blandas críticas que garantizan que el trabajo técnico se traduzca en valor real:")
        st.write("### ")
        
        # Grid de tres columnas usando tarjetas de información (st.info)
        blanda_col1, blanda_col2, blanda_col3 = st.columns(3)
        
        with blanda_col1:
            st.info("**🗣️ Comunicación Asertiva**\n\nExperiencia traduciendo tecnicismos complejos a reportes directivos comprensibles.")
            st.info("**🧩 Resolución de Problemas**\n\nPensamiento crítico orientado a solucionar fallas lógicas e incidencias en menos de 24 horas.")
            
        with blanda_col2:
            st.info("**👨‍🏫 Capacitación y Mentoría**\n\nCapacidad demostrada para diseñar material educativo, manuales técnicos y guiar equipos remotos.")
            st.info("**🎯 Atención al Detalle**\n\nGarantía de calidad e integridad en el procesamiento y limpieza de bases de datos masivas.")
            
        with blanda_col3:
            st.info("**⏳ Gestión del Tiempo**\n\nMonitoreo constante y estructurado para cumplir con métricas de avance y entregables críticos.")
            st.info("**🔄 Adaptabilidad**\n\nRápida adopción de herramientas emergentes y entornos virtuales de aprendizaje continuo.")

# ==========================================
# SECCIÓN: CATÁLOGO DE PROYECTOS
# ==========================================
# ==========================================
# SECCIÓN: CATÁLOGO DE PROYECTOS
# ==========================================
elif "Catálogo" in opcion:
    st.title("💻 Catálogo de Proyectos")
    st.write("Una selección de mis trabajos más recientes aplicando Ingeniería de Software y Ciencia de Datos.")
    st.divider()

    # --- FILA 1 DE PROYECTOS ---
    col1, col2 = st.columns(2)

    with col1:
        # PROYECTO 1: FUNDACIÓN AYUDA MUTUA
        with st.container(border=True):
            st.image("./assets/login_ayudamutua.PNG", width='stretch')
            
            st.subheader("Fundación Ayuda Mutua: Segmentación Analítica")
            st.caption("🛠️ **Stack:** Python | Streamlit | PostgreSQL (Supabase) | Scikit-Learn | Plotly")
            
            st.write("""
            Plataforma integral para el tercer sector. Implementa un modelo de **Machine Learning (K-Means)** basado en variables RFM para clasificar la base de donantes, optimizando campañas de recaudación. 
            Cuenta con arquitectura relacional segura y dashboards en tiempo real.
            """)
            
            c1, c2 = st.columns(2)
            c1.link_button("📂 Ver Repositorio", "https://github.com/JorgeHdzRiv/Ayuda_Mutua_App")
            c2.link_button("🚀 Ver Despliegue", "https://ayudamutua.streamlit.app/")

    with col2:
        # PROYECTO 2: IMDB END-TO-END ANALYTICS
        with st.container(border=True):
            st.image("./assets/dashboard.jpg", width='stretch')
            
            st.subheader("IMDb: Ecosistema End-to-End")
            st.caption("🛠️ **Stack:** Python | Google BigQuery | Power BI | Streamlit")
            
            st.write("""
            Pipeline ETL completo con limpieza de datos en la nube. 
            El proyecto incluye una Web App interactiva y un dashboard analítico para la auditoría de métricas cinematográficas.
            """)

            c1, c2, c3 = st.columns(3)
            c1.link_button("📂 Código", "https://github.com/JorgeHdzRiv/IMDB-End-to-End-Analytics")
            c2.link_button("🚀 App", "https://imdbtopmovies.streamlit.app/")
            c3.link_button("📊 BI", "https://github.com/JorgeHdzRiv/IMDB-End-to-End-Analytics/raw/refs/heads/main/dashboard/imdb_analytics.pbix") 

    st.write("")

    # --- FILA 2 DE PROYECTOS ---
    col3, col4 = st.columns(2)

    with col3:
        with st.container(border=True):
            st.info("⌛ **Próximamente:** Construyendo un nuevo proyecto de datos.")

    with col4:
        with st.container(border=True):
            st.info("⌛ **Próximamente:** Construyendo un nuevo proyecto de datos.")

    # --- FILA 3 DE PROYECTOS ---
    col5, col6 = st.columns(2)

    with col5:
        with st.container(border=True):
            st.info("⌛ **Próximamente:** Construyendo un nuevo proyecto de datos.")

    with col6:
        with st.container(border=True):
            st.info("⌛ **Próximamente:** Construyendo un nuevo proyecto de datos.")

# ==========================================
# SECCIÓN: CONTACTO
# ==========================================
elif "Contacto" in opcion:
    st.title("📧 ¡Hablemos!")
    st.write("Si tienes un desafío de datos que necesitas resolver, una propuesta de colaboración o simplemente quieres conectar, no dudes en ponerte en contacto.")
    st.divider()
    
    # Columnas Grandes
    col1, col2 = st.columns([1, 1.2], gap="large")
    
    with col1:
        st.markdown("### 📌 Canales Directos")
        st.write("Puedes encontrarme y contactarme directamente a través de los siguientes medios:")
        st.write("### ")
        
        # Tarjetas de información de contacto
        with st.container(border=True):
            st.markdown("**✉️ Correo Electrónico:**")
            st.write("jorge.hdzr96@gmail.com")
            
        with st.container(border=True):
            st.markdown("**📱 Teléfono / WhatsApp:**")
            st.write("+52 462 102 0836")
            
            # API Whatsapp
            mensaje_wa = "Hola Jorge, vi tu portafolio de Ciencia de Datos y me gustaría contactarte."
            url_wa = f"https://wa.me/524621020836?text={mensaje_wa.replace(' ', '%20')}"
            
            st.link_button("💬 Enviar WhatsApp", url_wa)
            
        with st.container(border=True):
            st.markdown("**📍 Ubicación Actual:**")
            st.write("Irapuato, Guanajuato, México")
            
        st.write("### ")
        st.markdown("#### 🌐 Redes Profesionales")
        st.write("Explora mi código o conecta conmigo a nivel profesional:")
        
        c1, c2 = st.columns(2)
        c1.link_button("💼 LinkedIn", "https://linkedin.com/in/JorHdzRiv")
        c2.link_button("💻 GitHub", "https://github.com/JorgeHdzRiv")
        
    with col2:
        st.markdown("### 📝 Enviar un Mensaje")
        st.write("Completa el formulario para enviarme una propuesta o consulta de manera rápida:")
        
        # Agrupamos los elementos en un formulario nativo con st.form
        with st.form(key="contact_form", clear_on_submit=True):
            nombre = st.text_input("Nombre Completo *", placeholder="Ej. Juan Pérez")
            empresa = st.text_input("Empresa u Organización", placeholder="Ej. Empresa S.A. o Independiente")
            correo = st.text_input("Correo de Contacto *", placeholder="Ej. juan.perez@ejemplo.com")
            
            asunto = st.selectbox("Asunto del Mensaje *", [
                "Oportunidad Laboral / Vacante",
                "Proyecto / Consultoría de Datos",
                "Colaboración en Software",
                "Otro Motivo"
            ])
            
            mensaje = st.text_area("Mensaje o Propuesta *", placeholder="Escribe aquí los detalles...", height=150)
            
            # El botón de envío es obligatorio dentro de un st.form
            submit_button = st.form_submit_button(label="🚀 Enviar Mensaje")
            
            # Lógica de validación y envío al presionar el botón
            if submit_button:
                if not nombre or not correo or not mensaje:
                    st.error("Por favor, completa todos los campos marcados como obligatorios (*).")
                else:
                    with st.spinner("Enviando mensaje..."):
                        try:
                            # 1. Configurar el servidor SMTP de Gmail
                            smtp_server = "smtp.gmail.com"
                            smtp_port = 587
                            
                            # 2. Extraer credenciales seguras
                            sender_email = st.secrets["EMAIL_SENDER"]
                            sender_password = st.secrets["EMAIL_PASSWORD"]
                            receiver_email = sender_email # Te envías el correo a ti mismo
                            
                            # 3. Construir el mensaje
                            msg = MIMEMultipart()
                            msg['From'] = sender_email
                            msg['To'] = receiver_email
                            msg['Subject'] = f"Portafolio: Nuevo mensaje de {nombre} - {asunto}"
                            
                            # Cuerpo del correo con formato HTML básico
                            body = f"""
                            <h3>Nuevo mensaje desde tu portafolio web</h3>
                            <p><strong>Nombre:</strong> {nombre}</p>
                            <p><strong>Empresa:</strong> {empresa if empresa else 'No especificada'}</p>
                            <p><strong>Correo de contacto:</strong> {correo}</p>
                            <p><strong>Asunto:</strong> {asunto}</p>
                            <hr>
                            <p><strong>Mensaje:</strong></p>
                            <p>{mensaje}</p>
                            """
                            msg.attach(MIMEText(body, 'html'))
                            
                            # 4. Conectar y enviar
                            server = smtplib.SMTP(smtp_server, smtp_port)
                            server.starttls() # Encriptar la conexión
                            server.login(sender_email, sender_password)
                            server.send_message(msg)
                            server.quit()
                            
                            # 5. Confirmación al usuario
                            st.success(f"¡Muchas gracias por escribir, {nombre}! Tu mensaje ha sido enviado exitosamente. Me comunicaré contigo a la brevedad.")
                            
                        except Exception as e:
                            st.error(f"Hubo un error al enviar el mensaje. Por favor, intenta contactarme directamente al correo o por LinkedIn. Detalle técnico: {e}")
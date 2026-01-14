import streamlit as st
import yt_dlp
import pandas as pd
import time

# --- CONFIGURAÇÃO DE SEO E PÁGINA ---
st.set_page_config(
    page_title="YT Extractor Pro | Extraia Links em Segundos",
    page_icon="🎬",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/seuusuario',
        'Report a bug': "https://github.com/seuusuario",
        'About': "# Extrator de Links do YouTube\nExtraia dados de canais inteiros de forma simples e rápida."
    }
)

# --- ESTILIZAÇÃO CSS PERSONALIZADA (FRONT-END) ---
st.markdown("""
    <style>
    /* Importando fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    
    /* Cor de Fundo e Texto */
    .stApp {
        background-color: #0f0f0f;
        color: #ffffff;
    }
    
    /* Estilo do Título */
    h1 {
        color: #FF0000; /* Vermelho YouTube */
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    /* Estilo do Input */
    .stTextInput > div > div > input {
        background-color: #1e1e1e;
        color: white;
        border: 1px solid #333;
        border-radius: 10px;
        padding: 10px;
    }
    
    /* Estilo do Botão Principal */
    .stButton > button {
        background-color: #cc0000;
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #ff0000;
        box-shadow: 0px 4px 15px rgba(255, 0, 0, 0.4);
        transform: scale(1.02);
    }
    
    /* Estilo da Tabela */
    .dataframe {
        color: white !important;
    }
    
    /* Rodapé */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0f0f0f;
        color: #888;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        border-top: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.title("🎬 YT Link Extractor")
st.markdown("""
<div style="text-align: center; color: #aaa; margin-bottom: 30px;">
    Ferramenta profissional para extração de metadados de vídeos e shorts.<br>
    Ideal para criadores de conteúdo, analistas de dados e arquivistas.
</div>
""", unsafe_allow_html=True)

# --- INPUT E LÓGICA ---
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    url_canal = st.text_input("🔗 Cole a URL do canal (Aba Vídeos ou Shorts):", placeholder="Ex: https://www.youtube.com/@MrBeast/videos")
    
    extract_btn = st.button("🚀 Extrair Dados Agora")

    if extract_btn:
        if not url_canal:
            st.warning("⚠️ Por favor, insira uma URL válida antes de continuar.")
        else:
            status_text = st.empty()
            progress_bar = st.progress(0)
            
            status_text.text("🔍 Iniciando conexão com o YouTube...")
            progress_bar.progress(10)
            
            try:
                # Configurações Otimizadas do yt-dlp
                ydl_opts = {
                    'extract_flat': True,
                    'quiet': True,
                    'ignoreerrors': True,
                    'force_generic_extractor': False,
                    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
                }

                dados_videos = []
                
                status_text.text("📡 Baixando metadados (isso não consome seus dados de vídeo)...")
                progress_bar.progress(30)

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url_canal, download=False)
                    progress_bar.progress(70)
                    
                    if 'entries' in info:
                        for video in info['entries']:
                            if video:
                                titulo = video.get('title', 'N/A')
                                vid_id = video.get('id')
                                url_video = f"https://www.youtube.com/watch?v={vid_id}"
                                views = video.get('view_count', 0)
                                duration = video.get('duration', 0)
                                
                                dados_videos.append({
                                    "Título": titulo,
                                    "URL": url_video,
                                    "ID": vid_id
                                })
                
                progress_bar.progress(100)
                status_text.empty()
                progress_bar.empty()

                if dados_videos:
                    # Criação do DataFrame
                    df = pd.DataFrame(dados_videos)
                    
                    st.success(f"✅ Extração Concluída! {len(dados_videos)} vídeos encontrados.")
                    
                    # Exibição
                    with st.expander("📄 Visualizar Tabela de Dados", expanded=True):
                        st.dataframe(df, use_container_width=True, height=400)
                    
                    # Download
                    csv = df.to_csv(index=False).encode('utf-8')
                    
                    st.download_button(
                        label="📥 Baixar Relatório (CSV)",
                        data=csv,
                        file_name="relatorio_youtube_links.csv",
                        mime="text/csv",
                        key='download-csv'
                    )
                else:
                    st.error("❌ Nenhum vídeo encontrado. Verifique se o link é da aba 'Videos' ou 'Shorts'.")

            except Exception as e:
                st.error(f"❌ Erro Crítico: {e}")

# --- RODAPÉ ---
st.markdown("""
<div class="footer">
    Desenvolvido com Python & Streamlit • <a href="https://github.com/seuusuario" target="_blank" style="color: #cc0000; text-decoration: none;">Visite meu GitHub</a>
</div>
""", unsafe_allow_html=True)
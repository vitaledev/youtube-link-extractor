# 🎬 YT Link Extractor Pro

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![YouTube](https://img.shields.io/badge/YouTube_Data-FF0000?style=for-the-badge&logo=youtube&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**A ferramenta definitiva para Criadores de Conteúdo e Analistas de Dados.**

[Ver Demo Online](https://youtube-link-extractor-jterogvugmappxnsc3yzgdt.streamlit.app/) </div>

---

## 📋 Sobre o Projeto

O **YT Link Extractor Pro** é uma aplicação web desenvolvida em Python que permite extrair metadados (Títulos, URLs, IDs, Views) de **todos** os vídeos ou shorts de um canal do YouTube em segundos.

Diferente de scrapers comuns, esta ferramenta utiliza o motor do `yt-dlp` otimizado para extração de metadados (`extract_flat`), garantindo velocidade e evitando o bloqueio por tráfego excessivo. O projeto conta com uma interface moderna (Dark Mode) construída com **Streamlit**.

---

## 🚀 Funcionalidades

* ✅ **Extração Ilimitada:** Lê canais inteiros, sejam 10 ou 1.000 vídeos.
* ✅ **Suporte Híbrido:** Funciona perfeitamente nas abas **Vídeos** e **Shorts**.
* ✅ **Ultra Rápido:** Não baixa vídeos, apenas lê os dados estruturados.
* ✅ **Exportação CSV:** Gera planilhas formatadas prontas para Excel, Google Sheets ou Pandas.

---

## 🛠️ Tecnologias Utilizadas

* **[Streamlit](https://streamlit.io/)**: Interface web interativa.
* **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: Motor de extração de dados do YouTube.
* **[Pandas](https://pandas.pydata.org/)**: Manipulação de dados e exportação CSV.

---

## 💻 Instalação e Uso Local

Siga os passos abaixo para rodar o projeto no seu computador:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/youtube-link-extractor.git](https://github.com/SEU_USUARIO/youtube-link-extractor.git)
    cd youtube-link-extractor
    ```

2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute a aplicação:**
    ```bash
    python -m streamlit run app.py
    ```

4.  **Acesse:** O navegador abrirá automaticamente em `http://localhost:8501`.

---

## 🤝 Contribuição

Contribuições são o que tornam a comunidade open source um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1.  Faça um **Fork** do projeto.
2.  Crie uma Branch para sua Feature (`git checkout -b feature/MinhaFeatureIncrivel`).
3.  Faça o **Commit** das suas mudanças (`git commit -m 'Adicionei a MinhaFeatureIncrivel'`).
4.  Faça o **Push** para a Branch (`git push origin feature/MinhaFeatureIncrivel`).
5.  Abra um **Pull Request**.

---

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

Isso significa que você é livre para usar, copiar, modificar, mesclar, publicar, distribuir, sublicenciar e/ou vender cópias do Software, desde que mantenha os créditos do autor original.

---

<div align="center">
  <sub>Desenvolvido com ☕ e Python por <a href="https://github.com/vitaledev">VitaleDev</a></sub>
</div>

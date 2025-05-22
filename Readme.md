<h1 align="center">🚀 MagicAI Platform</h1>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blueviolet?style=for-the-badge&logo=OpenAI" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Streamlit+React-Frontend-orange?style=for-the-badge&logo=react" />
</p>

<p align="center">
  🌟 <strong>Multi-provider AI Platform</strong> with credit-based access and ad-supported usage model.
</p>

---

## 🧠 About the Project

**MagicAI** is a modular, scalable, multi-AI-provider platform designed to serve high volumes of traffic and provide various AI tools like:

- 📝 Text Generation
- 🖼️ Image Creation
- 🗣️ Speech-to-Text & Text-to-Speech
- 🎞️ Video Intelligence *(optional)*

---

## 📐 Architecture Overview

```mermaid
graph LR
A[User Interface] --> B[FastAPI Backend]
B --> C[AI Model APIs]
B --> D[DynamoDB / PostgreSQL]
B --> E[Redis Cache]
B --> F[Ad System]
B --> G[Prompt Marketplace]

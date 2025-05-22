<h1 align="center">✨ MagicAI — Your One-Stop Generative AI Platform ✨</h1>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blueviolet?style=for-the-badge&logo=openai" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-orange?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Multi%20Provider%20Support-Enabled-blue?style=for-the-badge" />
</p>

<p align="center">
  <strong>All-in-one credit-based AI utility platform integrating text, image, audio, and video capabilities with monetization and marketplace support.</strong>
</p>

---

## 📑 Table of Contents

- [🚀 Project Overview](#-project-overview)
- [📦 Features](#-features)
- [🧠 System Architecture](#-system-architecture)
- [🛠️ Tech Stack](#️-tech-stack)
- [🧪 Modules Included](#-modules-included)
- [📸 Screenshots](#-screenshots)
- [🛠️ Setup Instructions](#-setup-instructions)
- [📬 Contact](#-contact)

---

## 🚀 Project Overview

**MagicAI** is a scalable and modular generative AI platform designed to:

- Serve users across multiple AI capabilities (Text, Image, Audio, and more)
- Integrate with multiple LLM providers (OpenAI, Hugging Face, Mistral, DeepSeek)
- Provide a credit system for usage control
- Monetize through ad-based free usage and prompt sharing
- Offer a prompt marketplace and user analytics

---

## 📦 Features

- 🧠 **AI as a Service**: Text, image, and audio generation with multiple LLM support.
- 🧾 **Prompt Marketplace**: Curated prompt library with sharing features.
- 📺 **Ad Monetization**: Earn credits by watching ads or sharing prompts.
- 🛂 **Auth + Credits**: Secure login with JWT and credit wallet system.
- 📊 **Admin Panel**: Dashboard to monitor usage and traffic.

---

## 🧠 System Architecture

### 🌐 High-Level Architecture

```mermaid
graph TD
A[User (Web/App)] --> B[Frontend (Streamlit / React)]
B --> C[Backend API - FastAPI]
C --> D[LLM APIs (OpenAI, HF, etc.)]
C --> E[Redis Cache]
C --> F[Database (PostgreSQL / DynamoDB)]
C --> G[Prompt Marketplace]
C --> H[Ad Engine]






### 🧩 Modular Services Flow

graph LR
A[Frontend] --> B[Auth Service]
A --> C[Credit Manager]
A --> D[AI Gateway]
A --> E[Prompt Library]
A --> F[Ad Tracker]

B --> G[JWT Tokens]
C --> H[Credit Wallet]
D --> I[LLM Selector]
D --> J[Text/Image/Speech]
F --> K[Ad Frequency Logic]




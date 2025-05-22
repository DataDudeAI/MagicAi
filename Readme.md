<h1 align="center" style="color:#5A67D8; text-shadow: 1px 1px 3px #ccc;">
  🚀 MegicAI Platform
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blueviolet?style=for-the-badge&logo=OpenAI" />
  <img src="https://img.shields.io/badge/Streamlit+React-Frontend-orange?style=for-the-badge&logo=react" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
</p>

<p align="center">
  🌟 <strong>Multi-provider AI Platform</strong> with credit-based access and ad-supported monetization.
</p>

---

## 🔍 Vision

> Build a **scalable, cost-efficient AI platform** that offers users access to various AI tools (Text, Image, Audio, etc.) in exchange for watching short ads. Monetization meets creativity 💡

---

## 📐 Architecture Overview

A robust and modular design to handle large-scale traffic :

```mermaid
graph LR
A[User Interface] --> B[FastAPI Backend]
B --> C[AI Model APIs]
B --> D[DynamoDB]
B --> E[Redis Cache]
B --> F[Ad System]
B --> G[Prompt Marketplace]

🧩 Core Components

| Layer            | Technologies Used                           |
| ---------------- | ------------------------------------------- |
| **Frontend**     | HTML/CSS/JS + Streamlit + React             |
| **Backend**      | FastAPI / Flask                             |
| **AI Providers** | Hugging Face, DeepSeek, OpenRouter, Mistral |
| **Database**     | DynamoDB / PostgreSQL                       |
| **Cache Layer**  | Redis / ElastiCache                         |
| **Auth**         | AWS Cognito / Auth0                         |
| **CDN**          | Cloudflare                                  |
| **Ads**          | Google AdSense / AdMob / Revcontent         |
| **Deployment**   | AWS ECS + Fargate                           |


🧮 Credit System (Gamified)
Tool Type	Ad Watch Time	Credits Earned
📝 Text Models	1 Minute	+5 Credits
🖼️ Image Models	2 Minutes	+10 Credits
🎞️ Video Models	3 Minutes	+15 Credits

🔄 Logic: Higher-resource models require longer ad views for balance and fairness.


🏗️ System Flow
✅ User selects an AI tool
✅ Platform checks credit balance
⬅️ If credits are insufficient → Show ad
💥 After watching, credits are rewarded
📡 Request processed via FastAPI → AI API
🧠 AI result stored in DynamoDB + Redis for fast access

🌟 Features
✨ Multiple AI providers with fallback logic

🧠 Credit-based access system tied to ad viewing

📦 Marketplace for user-generated prompts (users earn 2% of credits if their prompt is reused!)

🖥️ Responsive UI with animation support

🔒 Secure Auth with scalable user sessions

⚡ Fast response with smart caching

🗂️ Project Structure

GenAiToolbox/
├── app.py                   # FastAPI entrypoint
├── models.py                # Database models
├── tools.py                 # Tool configurations
├── requirements.txt
├── test_app.py              # Test cases
│
├── providers/               # AI provider integrations
│   ├── huggingface.py
│   ├── openai.py
│   ├── openrouter.py
│   └── deepseek.py
│
├── prompts/                 # Prompt templates and user customizations
│   └── marketplace_data/
│
├── static/                  # CSS/JS assets
│
├── templates/               # HTML templates
│   ├── index.html
│   ├── tool.html
│   └── result.html
│
└── ads/                     # Ad integration
    └── __init__.py

# 🛡️ Spam Detector

> A machine learning-powered spam classification system using Multinomial Naive Bayes, with **FastAPI backend** and **Docker containerization** for production-ready deployment.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Live Demo](#-live-demo)
- [Installation](#installation)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Deployment](#deployment)
- [Model Details](#model-details)

---

## Overview

This project implements an intelligent spam detection system powered by **Multinomial Naive Bayes** classification. It features a **FastAPI backend** for the prediction API and a **Streamlit web interface** for user interaction, both fully containerized with Docker.

### 🆕 What's New

- ✨ **FastAPI Backend** - High-performance REST API for predictions
- 🐳 **Docker Support** - Production-ready containerization
- 🚀 **Streamlit Frontend** - Interactive web interface
- ⚡ **Scalable Architecture** - Easy deployment on any cloud platform

### Key Statistics

- **Algorithm**: Multinomial Naive Bayes
- **Backend Framework**: FastAPI
- **Frontend Framework**: Streamlit
- **Containerization**: Docker
- **Performance**: Production-ready with optimized inference

---

## ✨ Features

- ✅ Real-time spam detection via REST API
- ✅ High-accuracy classification (Naive Bayes algorithm)
- ✅ Interactive web interface (Streamlit)
- ✅ FastAPI with automatic OpenAPI documentation
- ✅ Pre-trained model (joblib format)
- ✅ Docker containerization
- ✅ Lightweight and scalable architecture
- ✅ Easy deployment on cloud platforms

---

## 🚀 Live Demo

- **Web Interface**: [Streamlit Demo](https://spam-detector-mat.streamlit.app/)
- **Docker Hub**: [tyhan55/spam-detector-api](https://hub.docker.com/r/tyhan55/spam-detector-api)

---

## Installation

### Local Setup

#### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

#### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/tyhan-data/spam-detector.git
   cd spam-detector
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the FastAPI backend**
   ```bash
   uvicorn app.main:app --reload
   ```
   - API will be available at: `http://localhost:8000`
   - API documentation at: `http://localhost:8000/docs`

4. **Run the Streamlit frontend (in a new terminal)**
   ```bash
   streamlit run streamlit_app.py
   ```
   - Web interface will be available at: `http://localhost:8501`

---

### Docker Setup

#### Prerequisites
- Docker Desktop installed ([Download here](https://www.docker.com/products/docker-desktop))

#### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/tyhan-data/spam-detector.git
   cd spam-detector
   ```

2. **Build the Docker image**
   ```bash
   docker build -t spam-detector-api:latest .
   ```

3. **Run the container**
   ```bash
   docker run -p 8000:8000 spam-detector-api:latest
   ```

4. **Access the API**
   - API: `http://localhost:8000`
   - API Documentation: `http://localhost:8000/docs`

5. **Stop the container**
   ```bash
   docker ps  # Find the container ID
   docker stop <container_id>
   ```

#### Using Docker Hub

Pull the pre-built image from Docker Hub:

```bash
docker pull tyhan55/spam-detector-api:latest
docker run -p 8000:8000 tyhan55/spam-detector-api:latest
```

---

## 📁 Project Structure

```
spam-detector/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── schema.py               # Pydantic data models
│   └── model_service.py        # Model loading & prediction logic
├── models/
│   ├── Spam_detector.joblib    # Pre-trained Naive Bayes model
│   └── Count_Vectorizer.joblib # Feature vectorizer
├── streamlit_app.py            # Streamlit web interface
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── .dockerignore               # Docker ignore rules
├── README.md                   # This file
└── Spam Detection.ipynb        # Jupyter notebook (model training)
```

---

## 💻 Usage

### FastAPI Backend

#### Using cURL

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"Text": "Congratulations! You won a FREE iPhone. Click here to claim!"}'
```

#### Using Python

```python
import requests

response = requests.post(
    "http://localhost:8000/predict",
    json={"Text": "Your message here"}
)

print(response.json())
# Output: {"Target": "spam", "Probability": 0.95}
```

### Interactive Web Interface (Streamlit)

1. Open `http://localhost:8501`
2. Enter or paste a message
3. Click "🔍 Check Message"
4. View the prediction result and confidence score

#### Example Messages
- **Spam**: "Congratulations! You've won a FREE iPhone. Click here to claim!"
- **Ham**: "Hi, let's catch up this weekend?"

---

## 📡 API Documentation

### Endpoint: `/predict` (POST)

**Request Body:**
```json
{
  "Text": "Your message here"
}
```

**Response:**
```json
{
  "Target": "spam",
  "Probability": 0.95
}
```

**Interactive API Docs:**
- Visit `http://localhost:8000/docs` (Swagger UI)
- Visit `http://localhost:8000/redoc` (ReDoc)

---

## 🌍 Deployment

### Option 1: Docker Hub

Push your image to Docker Hub:

```bash
docker tag spam-detector-api:latest tyhan55/spam-detector-api:latest
docker push tyhan55/spam-detector-api:latest
```

### Option 2: Cloud Platforms

- **AWS**: ECR + ECS, Elastic Beanstalk, or Lambda
- **Google Cloud**: Cloud Run
- **Azure**: Container Instances, App Service
- **Heroku**: Using Docker support
- **DigitalOcean**: App Platform
- **Render**: Container deployment

### Option 3: Streamlit Cloud (Frontend Only)

1. Push repository to GitHub
2. Visit [Streamlit Cloud](https://share.streamlit.io)
3. Deploy `streamlit_app.py`
4. Configure API_URL to point to your backend

---

## 🤖 Model Details

### Algorithm: Multinomial Naive Bayes

- **Type**: Probabilistic classifier
- **Best For**: Text classification
- **Advantages**: Fast, interpretable, handles sparse data well
- **Training Data**: SMS/Email spam corpus

### Performance

- Efficient text classification into Spam/Ham categories
- Low latency predictions
- Lightweight model (~1MB)

---

## 📄 License

MIT License - See LICENSE file for details

---

## 📧 Contact

- **Author**: tyhan-data
- **Repository**: [GitHub - Spam Detector](https://github.com/tyhan-data/spam-detector)
- **Issues**: [Report a bug](https://github.com/tyhan-data/spam-detector/issues)

---

**Last Updated**: September 2026  
**Status**: ✅ Production Ready (FastAPI + Docker)

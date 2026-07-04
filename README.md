# 🛡️ Spam Detector

> A machine learning-powered spam classification system using Multinomial Naive Bayes to identify and filter unwanted messages with high accuracy.

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
- [Deployment](#deployment)
- [Model Details](#model-details)
- [Contributing](#contributing)

---

## Overview

This project implements an intelligent spam detection system that leverages **Multinomial Naive Bayes** classification to automatically identify spam messages. The model has been trained on a comprehensive dataset and is deployed as an interactive web application using Streamlit.

### Key Statistics
- **Algorithm**: Multinomial Naive Bayes
- **Primary Language**: Python (Jupyter Notebooks for development)
- **Framework**: Streamlit (Web Interface)
- **Performance**: Production-ready with optimized inference

---

## ✨ Features

- ✅ Real-time spam detection
- ✅ High-accuracy classification (Naive Bayes algorithm)
- ✅ Interactive web interface
- ✅ Pre-trained model (joblib format)
- ✅ Easy deployment on cloud platforms
- ✅ Docker containerization support
- ✅ Lightweight and scalable architecture

---

## 🚀 Live Demo

Try the application online (free): [Streamlit Cloud Demo](https://bcftchnrzapp4cgylunkqjv.streamlit.app/)

---

## Installation

### Local Setup

#### Prerequisites
- Python 3.8 or higher
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

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   Open your browser and navigate to: `http://localhost:8501`

---

### Docker Setup

#### Prerequisites
- Docker Desktop installed ([Download here](https://www.docker.com/products/docker-desktop))
- Docker daemon running on your system

#### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/tyhan-data/spam-detector.git
   cd spam-detector
   ```

2. **Build the Docker image**
   ```bash
   docker build -t spam-detection:v1 .
   ```

3. **Run the container**
   ```bash
   docker run -p 8501:8501 spam-detection:v1
   ```

4. **Access the app**
   Open your browser and navigate to: `http://localhost:8501`

5. **Stop the container**
   ```bash
   # Find the container ID
   docker ps
   
   # Stop the running container
   docker stop <container_id>
   ```

#### Understanding the Docker Commands

| Command | Explanation |
|---------|-------------|
| `docker build -t spam-detection:v1 .` | Builds a Docker image named `spam-detection` with tag `v1` from the Dockerfile in current directory |
| `docker run -p 8501:8501 spam-detection:v1` | Runs a container from the image and maps port 8501 (host) to port 8501 (container) |
| `-p 8501:8501` | Port mapping: `<host_port>:<container_port>` |

#### Advanced Docker Options

**Run in background (detached mode)**
```bash
docker run -d -p 8501:8501 --name spam-app spam-detection:v1
```

**View logs**
```bash
docker logs spam-app
```

**View running containers**
```bash
docker ps
```

**Stop container**
```bash
docker stop spam-app
```

**Remove container**
```bash
docker rm spam-app
```

**Remove image**
```bash
docker rmi spam-detection:v1
```

#### Docker Compose (Optional)

For easier management, use Docker Compose:

1. **Create a `docker-compose.yml` file** in the project root:
   ```yaml
   version: '3.8'
   services:
     spam-detector:
       build: .
       ports:
         - "8501:8501"
       container_name: spam-detector-app
       environment:
         - STREAMLIT_SERVER_HEADLESS=true
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up
   ```

3. **Run in background**
   ```bash
   docker-compose up -d
   ```

4. **View logs**
   ```bash
   docker-compose logs -f
   ```

5. **Stop the service**
   ```bash
   docker-compose down
   ```

#### Create a Dockerfile

If a Dockerfile doesn't exist, create one in the project root:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.headless=true"]
```

---

## 📁 Project Structure

```
spam-detector/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── Spam_detector.joblib            # Pre-trained model file
├── Count_Vectorizer.joblib         # Feature vectorizer
├── Dockerfile                      # Docker configuration
├── docker-compose.yml              # Docker Compose configuration (optional)
├── README.md                       # This file
└── notebooks/                      # Jupyter notebooks (analysis & training)
    └── spam_detection_notebook.ipynb
```

---

## 💻 Usage

### Running the Web Application

1. Start the application (Local or Docker)
2. Enter or paste a message in the text input field
3. Click "Classify" or "Detect Spam"
4. View the prediction result (Spam/Ham)
5. Confidence score is displayed for transparency

### Example Input
- **Spam**: "Congratulations! You've won a FREE iPhone. Click here to claim!"
- **Ham**: "Hi, let's catch up this weekend?"

---

## 🌍 Deployment

### Option 1: Streamlit Cloud (Recommended - Free)

1. Push your repository to GitHub
2. Visit [Streamlit Cloud](https://share.streamlit.io)
3. Click "New app"
4. Select your repository and branch
5. Select `app.py` as the entry point
6. Deploy!

### Option 2: Hugging Face Spaces (Free)

1. Go to [Hugging Face New Space](https://huggingface.co/new-space)
2. Select **Streamlit** as the SDK
3. Upload the following files:
   - `app.py`
   - `requirements.txt`
   - `Spam_detector.joblib`
   - `Count_Vectorizer.joblib`
4. Done! Your app is live

### Option 3: Docker (Any Cloud Provider)

Deploy using Docker on:
- **AWS**: ECR + ECS or Elastic Beanstalk
- **Google Cloud**: Cloud Run
- **Azure**: Container Instances
- **DigitalOcean**: App Platform
- **Heroku**: With Docker support
- **Self-hosted**: Any VPS with Docker installed

---

## 🤖 Model Details

### Algorithm: Multinomial Naive Bayes
- **Type**: Probabilistic classifier
- **Best For**: Text classification tasks
- **Advantages**: Fast, interpretable, works well with sparse data
- **Training Data**: SMS/Email spam corpus

### Model Performance
- Efficiently classifies text into Spam/Ham categories
- Low latency for real-time predictions
- Lightweight model size (~1MB)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 📧 Contact & Support

- **Author**: tyhan-data
- **Repository**: [GitHub - Spam Detector](https://github.com/tyhan-data/spam-detector)
- **Issues**: [Report a bug](https://github.com/tyhan-data/spam-detector/issues)

---

## 🎯 Future Enhancements

- [ ] Multi-language support
- [ ] Advanced model comparison (Random Forest, SVM, Deep Learning)
- [ ] User feedback mechanism for model improvement
- [ ] API endpoint development
- [ ] Batch processing capability
- [ ] Model retraining pipeline

---

**Last Updated**: July 2026  
**Status**: ✅ Production Ready

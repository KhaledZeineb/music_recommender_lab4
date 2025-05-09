# Music Recommender Lab

This lab guides you through building, deploying, and monitoring a complete machine learning pipeline for music recommendation. The project is divided into six modules, each focusing on a different aspect of ML deployment.

## Lab Structure

1. **Building the Machine Learning Model**
2. **Version Control with Git**
3. **Creating a Prediction Service with FastAPI**
4. **Containerization with Docker**
5. **CI/CD Pipeline with GitHub Actions**
6. **Cloud Deployment and Monitoring (Using Render)**

## Prerequisites

- Python 3.8+
- Anaconda (recommended)
- Git
- Docker
- GitHub account
- Docker Hub account
- Render account (free tier)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/music-recommender-lab.git
   cd music-recommender-lab
   ```

2. Create and activate a Conda environment:
   ```bash
   conda create -n music-recommender python=3.8
   conda activate music-recommender
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
music-recommender-lab/
├── MusicRecommender.ipynb       # Jupyter notebook for model development
├── music.csv                    # Sample dataset
├── app.py                       # FastAPI application
├── music_recommender.joblib     # Trained model
├── Dockerfile                   # Docker configuration
├── requirements.txt             # Python dependencies
├── .github/workflows/           # CI/CD pipeline configuration
│   └── ci-cd.yml
└── README.md                    # This file
```

## Usage

### 1. Running the Jupyter Notebook
```bash
jupyter notebook MusicRecommender.ipynb
```

### 2. Starting the FastAPI Service Locally
```bash
uvicorn app:app --host 0.0.0.0 --port 5000 --reload
```

### 3. Building and Running the Docker Container
```bash
docker build -t music-recommender .
docker run -p 5000:5000 music-recommender
```

### 4. Testing the API
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 21, "gender": 1}'
```

## Deployment

The CI/CD pipeline automatically builds and pushes the Docker image to Docker Hub on each push to the main branch. The application is deployed to Render from the Docker Hub image.

Live endpoint (example):
```bash
curl -X POST https://music-recommender.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"age": 21, "gender": 1}'
```

## Monitoring

View application logs in the Render dashboard under your service's "Logs" tab.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Dataset adapted from a simple example for educational purposes
- FastAPI for the web framework
- Render for cloud hosting
- GitHub Actions for CI/CD

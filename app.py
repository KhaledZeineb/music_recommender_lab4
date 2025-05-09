from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Music Recommender API",
    description="API de recommandation musicale basée sur l'âge et le genre",
    version="1.0.0"
)

# Chargement du modèle (avec gestion d'erreur)
try:
    model = joblib.load('music_recommender.joblib')
except FileNotFoundError:
    raise RuntimeError("Modèle non trouvé. Vérifiez le fichier music_recommender.joblib")

class UserInput(BaseModel):
    age: int = Field(..., example=25, gt=10, lt=100, description="Âge de l'utilisateur")
    gender: int = Field(..., example=1, ge=0, le=1, description="Genre (0=Femme, 1=Homme)")

@app.get("/", tags=["Root"])
async def root():
    """Endpoint de vérification de santé"""
    return {"status": "online", "docs": "/docs"}

@app.post('/predict', response_model=dict, tags=["Prediction"])
def predict(user_input: UserInput):
    """
    Prédit un genre musical basé sur l'âge et le genre
    
    - **age**: 10-100 ans
    - **gender**: 0 (Femme) ou 1 (Homme)
    """
    try:
        prediction = model.predict([[user_input.age, user_input.gender]])
        return JSONResponse(
            status_code=200,
            content={"genre": str(prediction[0])}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
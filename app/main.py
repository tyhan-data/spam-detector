from fastapi import FastAPI
from app.schema import SpamDetectorInput, SpamDetectorOutput
from app.model_service import load_model, model_prediction
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    
    # load the Model
    load_model()
    
    # Shutdown the process and clean all things
    yield
    
    
app = FastAPI(
    title= "Spam Detector",
    version= '2.2',
    lifespan=lifespan
)



# Creating a home page
@app.get('/')
def get_home():
    return{
        'success': True,
        'message': 'Welcome to our app'
    }
    
    
# Creating the prediction page
@app.post('/predict', response_model= SpamDetectorOutput)
def get_predict(payload: SpamDetectorInput):
    
    result = model_prediction(payload.model_dump())
    
    return SpamDetectorOutput(
            Target = result['Target'],
            Probability= result['Probability']
        )

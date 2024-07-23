from fastapi import FastAPI,HTTPException,Response,status
import joblib 
from pydantic import BaseModel
import pandas as pd
import numpy as np
import os ,uvicorn
import logging


# Informações adicionais para incluir na descrição do app
Util_info = """
Input:
- PRG: Plasma Glucose
- PL: Blood Work Result-1 (mu U/ml)
- PR: Blood Pressure (mm Hg)
- SK: Blood Work Result-2 (mm)
- TS: Blood Work Result-3 (mu U/ml)
- M11: Body Mass Index (weight in kg/(height in m)^2)
- BD2: Blood Work Result-4 (mu U/ml)
- Age: Patient's Age (years)
- Insurance: If a patient holds a valid insurance card

Output:
- Predicted Class = 0 (Negative) or 1 (positive)
- Prediction = Probability of predicted class
- Result = Positive if a patient in ICU will develop sepsis, Negative if a patient in ICU will not develop sepsis
"""

#load pipeline and encoder
pipeline  = joblib.load('./toolkit/pipeline.joblib')
encoder  = joblib.load('./toolkit/encoder.joblib')

# Configure the logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# APP
app = FastAPI(
    title='Sepsis Prediction App',
    description= Util_info
)

#Create class to define our input
class Sepsis_Feature(BaseModel):
    PRG:float
    PL:float
    PR:float
    SK:float
    TS:float
    M11:float
    BD2:float
    Age:float
    Insurance : float


#ENDPOINTS

@app.get("/")
async def home():
    return 'Bem-vindo à Previsão de Sepse App'

@app.post('/predict',status_code=status.HTTP_201_CREATED)
async def Predict_Sepsis(input:Sepsis_Feature):
 
    try:
        df = pd.DataFrame([input.model_dump()])
        prediction_probs = pipeline.predict_proba(df)
        prediction_class = pipeline.predict(df)
        decoder_prediction = encoder.inverse_transform([prediction_class])
        
        print(f"[iNFO] Input data as dataframe:\n{decoder_prediction.tolist()}")

        return {
            "data" : input,
            "predicted_class" : prediction_class[0].tolist(),
            "prediction": prediction_probs[0].tolist(),
            "result":decoder_prediction.tolist() 
        }
    
    except ValueError as e :
        logger.error(f"ValueError: {e}")
        return { "error":str(e)}
        
    except Exception as e :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f'this is a server error contact administrator {str(e)}')     

if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)
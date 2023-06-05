from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
import joblib
import numpy as np

# Define the request model
class PredictionRequest(BaseModel):
    data: list

# Create the FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load('irislogreg.pkl')

# Define the prediction endpoint
@app.post('/predict')
def predict(request: PredictionRequest):
    try:
        # Convert the incoming data to a NumPy array
        data = np.array(request.data)

        # Perform input validation
        if data.shape[1] != 4:
            raise HTTPException(status_code=400, detail="Invalid input data. Expected 4 features.")

        # Make predictions using the loaded model
        predictions = model.predict(data)

        # Perform output validation
        if not all(prediction in [0, 1, 2] for prediction in predictions):
            raise HTTPException(status_code=500, detail="Unexpected prediction results.")

        # Format the predictions as a response
        response = {
            'predictions': predictions.tolist()
        }

        return response

    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Input validation error: {e.errors()}")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


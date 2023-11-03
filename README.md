# Kagglex-final-project

## Maize-Disease-Detection-with-Computer-Vision
### Project Summary

In a study by the Food and Agriculture Organization of the United Nations (FAO), 
it was found that leaf diseases are responsible for up to 40% of maize yield losses in Africa. 
This project aims to leverage advanced computer vision models to identify and mitigate common 
maize leaf diseases, potentially increasing yields by up to 40% and positively impacting food security 
and livelihoods in Kenya.



### Prerequisites
- Install dependencies from requirements.txt
- Basic Command-line 

### Install and run 
1. Create a Python virtual environment:
   ```bash
   python3 -m venv detection_env python=3.9
2. Activate the virtual environment:
   ```bash
   source detection_env/bin/activate   # for linux
   detection_env\Scripts\activate      # for windows
4. Install the necessary requirements
   ```bash
   pip install -r requirements.txt
5. Now, run the flask app
    ```bash
    python app.py

### Project Screenshots

Flask web application interface 
![Screenshot (904)](https://github.com/Joshua-Abok/Maize-Disease-Detection-with-Computer-Vision/assets/38113323/4e9c1906-2d8d-4ba9-a160-0489d22c4edd)

Prediction Result Interface 
![prediction_result](https://github.com/Joshua-Abok/Maize-Disease-Detection-with-Computer-Vision/assets/38113323/1ae5d3b6-415c-4480-8a47-335fd5c7197a)



### MLflow Configuration

Export the following environment variables:

```bash
export MLFLOW_TRACKING_URI=[tracking_uri]

export MLFLOW_TRACKING_USERNAME=[name]

export MLFLOW_TRACKING_PASSWORD=[password]
```

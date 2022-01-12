import requests

#Get A sample of how your POST Request should look like:
response = requests.get("http://localhost:5000/image-predict")
print(response.json())

#POST Request that gets you a prediction number for your image

#To enconde an image to base64, please use this website https://base64.guru/converter/encode/image
# and copy the string into your "image" : (your string)

response = requests.post("http://localhost:5000/image-predict", 
                         json = ({"image": "iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8/fFQqAAAACXBIWXMAAA9hAAAPYQGoP6dpAAABfElEQVR4nO1W0Y2DMAw16LpFukf2aDJHmzVAqGuEroGI2m7RrlE5776aAxJoOOn6caolyxImvDw/26IgItAbrXwn2AfwA/gr+8p5qW1bAkCXy4WOx2OUN8YQESVzKcOSSykBAMwMAKjrGt57MHMy1nW9+L1FQGMMrLVgZjwej+xojFkPOGU2jClmXddlMS2eqFOz1pLWmrz3VJZlFJumoev1SgCoKAo6n8+03+/pcDiE9zabTZ6GTdMkmbVtCynlbLmccyPm2SVNaVNV1atmgBACXdeFczMXjA/e73dYa0PjvGiCyKcaD3PJOQR+ZM2dren5oeZRfuoAoJRaxYqIoLVG3/eBmTEmr6TMjN1ulw30LPlU+5kGW8ci5d57KKUCsxfdHD88nU6haXKcmUfduXrTSClxu93gnIPWGtvtFlrrkVZDz2S2XFIpZbhx3/dhruZ2a1VVueMzn3TORTsyFVfO6XxSCAEhBJRSI43WbqChzy7vv7L//0/zdsBvGrApTDvwxZ0AAAAASUVORK5CYII="
                                 ,"filename": "request_test.png"}))
print(response.json())
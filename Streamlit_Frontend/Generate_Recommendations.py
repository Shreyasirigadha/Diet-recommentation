import requests
import json

class Generator:
    def __init__(self, nutrition_input: list, ingredients: list = [], params: dict = {"n_neighbors": 5, "return_distance": False}):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def set_request(self, nutrition_input: list, ingredients: list, params: dict):
        self.nutrition_input = nutrition_input
        self.ingredients = ingredients
        self.params = params

    def generate(self):
        request = {
            "nutrition_input": self.nutrition_input,
            "ingredients": self.ingredients,
            "params": self.params
        }
        try:
            response = requests.post(
                url="http://localhost:8000/predict/",   # 👈 use 8000 instead of 8080
                json=request,                           # 👈 use json= instead of data= + dumps
                headers={"Content-Type": "application/json"},
                timeout=10
            )

            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)

            response.raise_for_status()  # raise error if status != 200
            return response.json()       # safe json parsing

        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
            return {"error": str(e)}

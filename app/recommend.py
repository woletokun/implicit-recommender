# app/recommend.py

from utils.data_preprocessing import load_and_preprocess
from models.als_model import train_als_model

matrix, df, ue, ie = load_and_preprocess("data/raw/implicit_data.csv")
model = train_als_model(matrix)

user_idx = 0  # can be taken from CLI args
recommended = model.recommend(user_idx, matrix[user_idx], N=5)
item_ids = [ie.inverse_transform([i])[0] for i, _ in recommended]
print(f"Recommended items: {item_ids}")

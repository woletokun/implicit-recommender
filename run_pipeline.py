from utils.data_preprocessing import load_and_preprocess
from models.als_model import train_als_model

matrix, df, user_encoder, item_encoder = load_and_preprocess('data/raw/implicit_data.csv')
model = train_als_model(matrix)

user_idx = 0
recommendations = model.recommend(user_idx, matrix[user_idx], N=5)
items = [item_encoder.inverse_transform([i])[0] for i, _ in recommendations]
print(f'Recommended items for user {user_idx}:', items)

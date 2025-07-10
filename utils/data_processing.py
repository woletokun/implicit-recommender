# utils/data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from scipy.sparse import coo_matrix

def load_and_preprocess(csv_path):
    df = pd.read_csv(csv_path)

    # Convert event types to weights
    weights = {'view': 1, 'click': 2, 'purchase': 5}
    df['strength'] = df['event_type'].map(weights).fillna(0)

    # Encode user/item IDs into numerical indexes
    user_encoder = LabelEncoder()
    item_encoder = LabelEncoder()
    df['user_idx'] = user_encoder.fit_transform(df['user_id'])
    df['item_idx'] = item_encoder.fit_transform(df['item_id'])

    # Create sparse matrix: rows = users, cols = items
    matrix = coo_matrix(
        (df['strength'], (df['user_idx'], df['item_idx']))
    ).tocsr()

    return matrix, df, user_encoder, item_encoder

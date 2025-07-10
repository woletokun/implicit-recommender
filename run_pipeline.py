# run_pipeline.py

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from utils.data_processing import load_and_process

# Sample input file path (adjust if needed)
csv_path = "data/raw/implicit_data.csv"

matrix, df, user_encoder, item_encoder = load_and_process(csv_path)

print("✅ Data loaded and processed successfully!")
print("🧮 Matrix shape:", matrix.shape)
print("🔢 Sample encoded users:\n", df[['user_id', 'user_idx']].drop_duplicates().head())
print("🔢 Sample encoded items:\n", df[['item_id', 'item_idx']].drop_duplicates().head())
# run_pipeline.py


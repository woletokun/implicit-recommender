# run_pipeline.py

from utils.data_preprocessing import load_and_preprocess

# Sample input file path (adjust if needed)
csv_path = "data/raw/interactions.csv"

matrix, df, user_encoder, item_encoder = load_and_preprocess(csv_path)

print("✅ Data loaded and preprocessed successfully!")
print("🧮 Matrix shape:", matrix.shape)
print("🔢 Sample encoded users:\n", df[['user_id', 'user_idx']].drop_duplicates().head())
print("🔢 Sample encoded items:\n", df[['item_id', 'item_idx']].drop_duplicates().head())
# run_pipeline.py

from utils.data_preprocessing import load_and_preprocess

# Sample input file path (adjust if needed)
csv_path = "data/raw/interactions.csv"

matrix, df, user_encoder, item_encoder = load_and_preprocess(csv_path)

print("✅ Data loaded and preprocessed successfully!")
print("🧮 Matrix shape:", matrix.shape)
print("🔢 Sample encoded users:\n", df[['user_id', 'user_idx']].drop_duplicates().head())
print("🔢 Sample encoded items:\n", df[['item_id', 'item_idx']].drop_duplicates().head())
# run_pipeline.py

from utils.data_preprocessing import load_and_preprocess

# Sample input file path (adjust if needed)
csv_path = "data/raw/interactions.csv"

matrix, df, user_encoder, item_encoder = load_and_preprocess(csv_path)

print("✅ Data loaded and preprocessed successfully!")
print("🧮 Matrix shape:", matrix.shape)
print("🔢 Sample encoded users:\n", df[['user_id', 'user_idx']].drop_duplicates().head())
print("🔢 Sample encoded items:\n", df[['item_id', 'item_idx']].drop_duplicates().head())

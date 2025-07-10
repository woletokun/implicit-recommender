# cold_start/hybrid_strategy.py

def recommend_popular_items(df, top_n=5):
    popular_items = df.groupby('item_id')['event_type'].count().sort_values(ascending=False)
    return list(popular_items.head(top_n).index)

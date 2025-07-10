# explainability/explanation_engine.py

def generate_reason(user_id, item_id, item_name=None):
    return f"User {user_id} may like {item_name or item_id} because they interacted with similar items."

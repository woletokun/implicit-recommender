# models/als_model.py

from implicit.als import AlternatingLeastSquares

def train_als_model(sparse_matrix, factors=50, regularization=0.01, iterations=15):
    model = AlternatingLeastSquares(
        factors=factors,
        regularization=regularization,
        iterations=iterations,
        use_gpu=False
    )
    model.fit(sparse_matrix.T)  # ALS expects item-user matrix
    return model

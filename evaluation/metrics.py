# evaluation/metrics.py

def precision_at_k(actual, predicted, k):
    return len(set(predicted[:k]) & set(actual)) / k

def recall_at_k(actual, predicted, k):
    return len(set(predicted[:k]) & set(actual)) / len(actual)

def mean_average_precision(actual_list, predicted_list, k=10):
    precisions = []
    for actual, predicted in zip(actual_list, predicted_list):
        precisions.append(precision_at_k(actual, predicted, k))
    return sum(precisions) / len(precisions)

import numpy as np
from ground_truth import get_ground_truth
from test_data import test_dataset
from input import extract_features, get_id


def data():
    # Ids of the songs that matter to us
    ids = get_id()

    # Training data (80% of whole data)
    train_ids = [ids[i] for i in range(7, len(ids))]
    train_data = extract_features(train_ids).astype(np.float32)

    # Validation data (20% of whole data)
    val_ids = [ids[i] for i in range(7)]
    val_data = extract_features(val_ids).astype(np.float32)

    # Test data
    test_data = test_dataset()

    # Ground truth
    output_data = get_ground_truth()

    return train_data, val_data, test_data, output_data

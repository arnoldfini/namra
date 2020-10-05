import numpy as np
import pandas as pd
from ground_truth import compute_ground_truth
from test_data import test_dataset
from avgdata import df_avg
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

    return train_data, val_data


def test_data():
    # Test data
    test_data, random_titles, random_artists = test_dataset()
    return test_data, random_titles, random_artists


def labels():

    df = df_avg()

    # Compute one hot encoding of the average stored in df_avg
    df_train = df.drop(df.index[[range(7)]])
    df_val = df.drop(df.index[[range(7, len(df))]])

    # This will be the labels of the NN
    train_labels = compute_ground_truth(df_train)
    val_labels = compute_ground_truth(df_val)

    #test_data = test_dataset()
    #test_labels = compute_ground_truth(test_data)

    return train_labels, val_labels

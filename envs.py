import os

train_test_split_value = os.environ.get('TEST_TRAIN_SPLIT', 0.8)
print(train_test_split_value)
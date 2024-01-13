import argparse


parser = argparse.ArgumentParser(description='Preprocess the data.')
parser.add_argument('--train_test_split', type=float, default=0.8, help='Train test split')
args = parser.parse_args()

print(args.train_test_split)
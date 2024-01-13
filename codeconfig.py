import os
import argparse
import toml


parser = argparse.ArgumentParser(description='Preprocess the data.')
parser.add_argument('--config', type=str, default='config.toml', help='Config file')
args = parser.parse_args()

absolute_path_to_config_file = os.path.abspath(args.config)
print('Config file: {}'.format(absolute_path_to_config_file))

config = toml.load(args.config)

print(config)
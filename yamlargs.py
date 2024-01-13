import yaml

with open("config.yaml", 'r') as stream:
    try:
        values = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

print(values)

print(values['train_test_split'])
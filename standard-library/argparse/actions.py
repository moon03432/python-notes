import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('--bar', action='store_false')
args = parser.parse_args()

print(args.foo)
print(args.bar)
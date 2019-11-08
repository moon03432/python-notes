import argparse
import os

parser = argparse.ArgumentParser()

# positional arguments
parser.add_argument('echo', nargs='*', default=None)

# optional arguments
parser.add_argument("--workspace", help="workspace", type=str)
parser.add_argument("--batch-size", help="batch size", type=int, default=60)

args = parser.parse_args()
print(args.echo)
print(type(args.echo))
if not args.echo:
    print "echo is None"
    
# print args.workspace
# print args.batch_size

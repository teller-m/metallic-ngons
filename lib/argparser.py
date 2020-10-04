import argparse

parser = argparse.ArgumentParser()
parser.add_argument('size', help="Size of regular polygon", type=int)
parser.add_argument('mean_id', help="Metallic mean to test for", type=int)
parser.add_argument('--dps', help="Decimal precision [Default: 50]", default=50, type=int)
parser.add_argument('--buffer', help="Decimal precision buffer [Default: 5]", default=5, type=int)
parser.add_argument('-s', '--show_matches', help="Show matches", default=False, action="store_true")
args = parser.parse_args()

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('n', help="# of sides for a regular polygon", type=int)
parser.add_argument('mean_id', help="metallic mean to test for", type=int)
parser.add_argument('--dps', help="decimal precision [default: 50]", default=50, type=int)
parser.add_argument('--buffer', help="decimal precision buffer [default: 5]", default=5, type=int)
parser.add_argument('-s', '--show_matches', help="show matches", default=False, action="store_true")
args = parser.parse_args()

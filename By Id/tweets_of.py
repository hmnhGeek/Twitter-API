import argparse as ap
import tweets

parser = ap.ArgumentParser()
parser.add_argument("user_id", type = str, help = "Type twitter username.")
parser.add_argument("Number", type = int, help = "Number of tweets.", default = 1)
args = parser.parse_args()

tweets.search(args.user_id, args.Number)

import argparse as ap
import tweets_web

parser = ap.ArgumentParser()
parser.add_argument("keyword", type = str, help = "Type a keyword.")
parser.add_argument("Number", type = int, help = "Number of tweets.", default = 1)
args = parser.parse_args()

tweets_web.search(args.keyword, args.Number)

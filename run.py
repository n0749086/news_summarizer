from argparse import ArgumentParser
from pathlib import Path

import config
import setting

import feedparser
import google.generativeai as genai


def parse_args():
	parser = ArgumentParser()
	parser.add_argument('config_path', type=Path)
	return parser.parse_args()

def main():
	args = parse_args()
	list_target = config.load_config(args.config_path)
	
	for url, category in list_target:
		d_atom = feedparser.parse(url)
		for elem in d_atom['entries']:
			print(elem['title'], elem['summary'])

if __name__ == '__main__':
	main()

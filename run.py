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
	genai.configure(api_key=setting.API_KEY)
	model = genai.GenerativeModel('gemini-pro')
	chat = model.start_chat(history=[])
	
	for url, category in list_target:
		d_atom = feedparser.parse(url)
		for elem in d_atom['entries']:
			title = elem['title']
			summary =  elem['summary'] if 'summary' in elem else ''
			sentence ='与えられた文書が、以下条件の内容に該当する場合1、そうでない場合は0を出力せよ。結果は、0か1かを出力すること。 \n '\
			'<条件>\n'\
			+'「' + ','.join(category) +'」のいずれかに関連する。\n' \
			'<文章>\n' \
			+ title+ '\n' +summary
			response = chat.send_message(sentence,  safety_settings={'HARASSMENT':'block_none', 'HATE_SPEECH':'block_none'})
			print(response.text)
			if response.text == '1':
				print(title, summary)

if __name__ == '__main__':
	main()

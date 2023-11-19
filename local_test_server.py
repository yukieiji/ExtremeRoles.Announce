import os
import json

from flask import Flask, jsonify, abort


JSON_FILE_DIR = f'{__file__}/Announce'

def get_data_from_file(lang, filename):
	file_path = os.path.join(JSON_FILE_DIR, lang, filename)

	with open(file_path, 'r') as file:
		data = json.load(file)
	return data

def main():

	app = Flask(__name__)


	@app.route('/Announce/<filename>', methods=['GET'])
	def allAnnounce(filename):
		with open(os.path.join(JSON_FILE_DIR, filename), 'r') as file:
			data = json.load(file)
			return jsonify(data)

	@app.errorhandler(404)
	def not_found(error):
		return jsonify({'error': 'Not found'}), 404

	@app.route('/Announce/<lang>/<filename>', methods=['GET'])
	def get_file_data(lang, filename):
		if filename not in os.listdir(os.path.join(JSON_FILE_DIR, lang)):
			abort(404)
		data = get_data_from_file(lang, filename)
		return jsonify(data)

	app.run(debug=True)


if __name__ == '__main__':
	main()
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/files', methods=['POST'])
def get_files_in_folder():
    folder_path = request.form['folder_path']
    file_list = os.listdir(folder_path)
    return render_template('index.html', files=file_list)

if __name__ == '__main__':
    app.run()

from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list_files', methods=['POST'])
def list_files():
    folder_path = request.form['folder_path']
    files = []
    folders = []
    
    try:
        for item in os.listdir(folder_path):
            if os.path.isfile(os.path.join(folder_path, item)):
                files.append(item)
            else:
                folders.append(item)
    except FileNotFoundError:
        return render_template('index.html', error='Папка не найдена')
    
    return render_template('index.html', files=files, folders=folders)

if __name__ == '__main__':
    app.run()

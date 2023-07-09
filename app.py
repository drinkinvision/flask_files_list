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

    save_path = None
    if 'file_name' in request.form:
        file_name = request.form['file_name']
        if file_name.endswith('.txt'):
            save_path = os.path.join(folder_path, file_name)
            with open(save_path, 'w') as txt_file:
                for file in file_list:
                    txt_file.write(file + '\n')

    return render_template('index.html', files=file_list, save_path=save_path)

if __name__ == '__main__':
    app.run()

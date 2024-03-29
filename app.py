from flask import Flask, render_template, request
import os
import chardet

app = Flask(__name__)


@app.route('/', methods=['GET'])
def display_file():
    file_name = request.args.get('file', 'file1.txt')
    start_line = request.args.get('start_line')
    end_line = request.args.get('end_line')

    try:
        file_path = os.path.join('files', file_name)
        with open(file_path, 'rb') as f:
            raw_data = f.read()
            encoding_result = chardet.detect(raw_data)
            encoding = encoding_result['encoding']

        with open(file_path, 'r', encoding=encoding) as f:
            lines = f.readlines()

            if start_line and end_line:
                start_line = int(start_line)
                end_line = int(end_line)
                lines = lines[start_line - 1:end_line]

            content = ''.join(lines)
            return render_template('file_content.html', content=content, file_name=file_name)
    except Exception as e:
        return render_template('error.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True)

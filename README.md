## Installation & Setup

### Clone repository:
Clone the repository:

git clone https://github.com/anishgupta1510/vetty-test.git

### Navigate to the project directory:
Change directory to `vetty-test`:

cd vetty-test

### Install dependencies:
Install the dependencies required for the project:

pip install -r requirements.txt


## Usage

### Run the Flask Application:
You can run the Flask application using the following command:

python app.py

### Test the API:
Test the API on **http://localhost:5000/**

Use the following URL parameters to customize file reading:

- `file`: Specify the name of the file to read. Default is `file1.txt`.
- `start_line`: Specify the line number to start reading from.
- `end_line`: Specify the line number to end reading at.

## Examples

Here's an example URL with parameters:

http://localhost:5000/?file=file2.txt&start_line=3&end_line=5

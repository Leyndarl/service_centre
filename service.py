from flask import Flask
app = Flask(__name__)

@app.route('/')
def Service_centre():
    return 'Service_centre'

if __name__ == '__main__':
    app.run(debug=True)

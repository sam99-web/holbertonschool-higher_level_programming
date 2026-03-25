from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Flask App</title>
</head>
<body>
    <h1>Hello from Flask!</h1>
    <p>My first Jinja2 template.</p>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
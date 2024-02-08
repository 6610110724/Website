from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tactics')
def tactics():
    # Here you could fetch tactics data from a database or other source
    # For now, let's just pass some example data
    tactics_data = [
        {'name': '4-4-2', 'description': 'This is a classic formation with four defenders, four midfielders, and two forwards.'},
        {'name': '3-5-2', 'description': 'A formation with three defenders, five midfielders, and two forwards.'},
        # Add more tactics as needed
    ]
    return render_template('tactics.html', tactics=tactics_data)

if __name__ == '__main__':
    app.run(debug=True)

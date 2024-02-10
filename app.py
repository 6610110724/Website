from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/supportus')
def supportus():
    return render_template('supportus.html')

@app.route('/tactics4')
def tactics4():
    tactics_database = [
        {'name': '4 Defenders Formations', 'description': 'The 4 defender tactics are very popular tactic because tactical balance in both defensive and offensive.'},
    ]
    return render_template('tactics4.html', tactics=tactics_database)


@app.route('/tactics5')
def tactics5():
    tactics_database = [
        {'name': '5 Defenders Formations', 'description': "The 5 defender tactics are tactic that focuses on defending and using the player's individual abilities to attack."},
    ]
    return render_template('tactics5.html', tactics=tactics_database)

@app.route('/tactics3')
def tactics3():
    tactics_database = [
        {'name': '3 Defenders Formations', 'description': 'The 3 defender tactics are tactic that focuses on the offensive and uses ball possession in midfield to create scoring chances.'},
    ]
    return render_template('tactics3.html', tactics=tactics_database)

if __name__ == '__main__':
    app.run(debug=True)
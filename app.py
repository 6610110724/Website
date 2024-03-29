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
        {'name': '4 Defenders Formations', 'description': 'The 4 defender tactics are very popular tactic because tactical balance in both defensive and offensive.  So, you can study about tactics below.'},
    ]
    return render_template('tactics4.html', tactics=tactics_database)

@app.route('/tactics5')
def tactics5():
    tactics_database = [
        {'name': '5 Defenders Formations', 'description': "The 5 defender tactics are tactic that focuses on defending and using the player's individual abilities to attack.  So, you can study about tactics below."},
    ]
    return render_template('tactics5.html', tactics=tactics_database)

@app.route('/tactics3')
def tactics3():
    tactics_database = [
        {'name': '3 Defenders Formations', 'description': 'The 3 defender tactics are tactic that focuses on the offensive and uses ball possession in midfield to create scoring chances. So, you can study about tactics below.'},
    ]
    return render_template('tactics3.html', tactics=tactics_database)

@app.route('/f343')
def f343():
    return render_template('f343.html')

@app.route('/f3412')
def f3412():
    return render_template('f3412.html')

@app.route('/f352')
def f352():
    return render_template('f352.html')

@app.route('/f442')
def f442():
    return render_template('f442.html')

@app.route('/f4312')
def f4312():
    return render_template('f4312.html')

@app.route('/f4231')
def f4231():
    return render_template('f4231.html')

@app.route('/f433')
def f433():
    return render_template('f433.html')

@app.route('/f532')
def f532():
    return render_template('f532.html')

@app.route('/f523')
def f523():
    return render_template('f523.html')

@app.route('/f541')
def f541():
    return render_template('f541.html')

if __name__ == '__main__':
    app.run(debug=True)

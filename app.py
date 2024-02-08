from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tactics4')
def tactics4():
    tactics_data = [
        {'name': '4 Defenders Formations'},
        {'description': 'The 4 defender tactics are very popular tactic because tactical balance in both defensive and offensive.'},
        {'name': '4-4-2', 'description': 'This is a classic formation with 4 defenders, 4 midfielders, and 2 forwards.'},
        {'name': '4-2-4', 'description': 'This formation apply from 4-4-2 but 4-2-4 push both wingers higher to focus on full attack.'},
        {'name': '4-2-3-1', 'description': 'This formation apply from 4-4-2 but 4-2-3-1 will drop 1 striker down to be a playmaker.'},
        {'name': '4-3-3', 'description': 'This is a modern formation with 4 defenders, 3 midfielders, 2 wingers forward and 1 target forward.'},
        {'name': '4-3-1-2', 'description': 'This formation that apply from 4-3-3 but 4-3-1-2 has 1 playmaker and 2 strikers.'},
    ]
    return render_template('tactics4.html', tactics=tactics_data)


@app.route('/tactics5')
def tactics5():
    tactics_data = [
        {'name': '5 Defenders Formations'},
        {'description': "The 5 defender tactics are tactic that focuses on defending and using the player's individual abilities to attack."},
        {'name': '5-2-3', 'description': 'This formation focuses on defending and counter attack with both wingers.'},
        {'name': '5-2-1-2', 'description': 'This formation apply from 5-2-3 but 5-2-1-2 will drop 1 striker down to be a playmaker.'},
        {'name': '5-3-2', 'description': 'This formation apply from 5-2-3 and 5-2-1-2 but 5-3-2 will drop 1 attacking player down to be a midfielders for more compact in the midfield.'},
        {'name': '5-4-1', 'description': 'This formation main focuses on defending but still managed ball prosession in the midfield with four midfielders.'},
    ]
    return render_template('tactics5.html', tactics=tactics_data)


@app.route('/tactics3')
def tactics3():
    tactics_data = [
        {'name': '3 Defenders Formations'},
        {'description': 'The 3 defender tactics are tactic that focuses on the defensive and uses ball possession in midfield to create scoring chances.'},
        {'name': '3-4-3', 'description': 'This is a classic formation with 4 defenders, 4 midfielders, and 2 forwards.'},
        {'name': '3-4-1-2', 'description': 'This formation that apply from 4-3-3 but 4-3-1-2 has 1 playmaker and 2 strikers.'},
        {'name': '3-5-2', 'description': 'This formation apply from 4-4-2 but 4-2-4 push both wingers higher to focus on full attack.'},
        {'name': '3-2-3-2', 'description': 'This formation apply from 4-4-2 but 4-2-3-1 will drop 1 striker down to be a playmaker.'},
        {'name': '3-3-3-1', 'description': 'This is a modern formation with 4 defenders, 3 midfielders, 2 wingers forward and 1 target forward.'},
    ]
    return render_template('tactics3.html', tactics=tactics_data)



if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/action/<int:num>')
def action_num(num):
    if num ==1:
        return render_template('attack.html')
    if num ==2:
        return render_template('defence.html')
    if num ==3:
        return render_template('doos.html')

if __name__ == '__main__':
    app.run(debug=True)
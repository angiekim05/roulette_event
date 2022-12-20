from flask import Flask, render_template, request

app = Flask(__name__)
    

@app.route('/')
def index(name=None):
    return render_template('index.html')

@app.route('/notice')
def notice(name=None):
    return render_template('notice.html')

@app.route('/mission1', methods = ['GET', 'POST'])
def mission1(name=None):
    # if request.method == 'POST':
    #     f = request.files['file']
    return render_template('mission1.html')

@app.route('/mission1_roulette', methods = ['GET', 'POST'])
def mission1_roulette(name=None):
    return render_template('noluck.html')

@app.route('/mission1_', methods = ['GET', 'POST'])
def mission1_(name=None):
    return render_template('mission1_.html')

@app.route('/mission1_roulette_', methods = ['GET', 'POST'])
def mission1_roulette_(name=None):
    return render_template('rbox.html')

@app.route('/mission2', methods = ['GET', 'POST'])
def mission2(name=None):
    return render_template('mission2.html')

@app.route('/mission2_', methods = ['GET', 'POST'])
def mission2_(name=None):
    return render_template('mission2_.html')

@app.route('/mission2_roulette', methods = ['GET', 'POST'])
def mission2_roulette(name=None):
    return render_template('rbox2.html')

@app.route('/mission3', methods = ['GET', 'POST'])
def mission3(name=None):
    return render_template('mission3.html')

@app.route('/mission3_roulette', methods = ['GET', 'POST'])
def mission3_roulette(name=None):
    return render_template('luck.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notice')
def notice():
    return render_template('notice.html')

@app.route('/mission1', methods = ['GET', 'POST'])
def mission1():
    # 사진 처리를 한다면 여기서
    # if request.method == 'POST':
    #     f = request.files['file']
    return render_template('mission1.html')

@app.route('/mission1_roulette', methods = ['GET', 'POST'])
def mission1_roulette():
    return render_template('noluck.html')

@app.route('/mission1_', methods = ['GET', 'POST'])
def mission1_():
    return render_template('mission1_.html')

@app.route('/mission1_roulette_', methods = ['GET', 'POST'])
def mission1_roulette_():
    return render_template('rbox.html')

@app.route('/mission2', methods = ['GET', 'POST'])
def mission2():
    return render_template('mission2.html')

@app.route('/mission2_', methods = ['GET', 'POST'])
def mission2_():
    return render_template('mission2_.html')

@app.route('/mission2_roulette', methods = ['GET', 'POST'])
def mission2_roulette():
    return render_template('rbox2.html')

@app.route('/mission3', methods = ['GET', 'POST'])
def mission3():
    return render_template('mission3.html')

@app.route('/mission3_roulette', methods = ['GET', 'POST'])
def mission3_roulette():
    return render_template('luck.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
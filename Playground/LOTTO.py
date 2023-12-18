from flask import Flask, request, render_template
import random as ran
import time

app = Flask(__name__)

def lotto(my_n) :
    list_lotto_num = [ran.randint(1,45), ran.randint(1,45), ran.randint(1,45), ran.randint(1,45), ran.randint(1,45), ran.randint(1,45)]
    c = 0
    result = "MY NUMBER : " + str(my_n) + "\n" + time.strftime("%Y LOTTO NUMBER : ", time.localtime()) + str(list_lotto_num) + "\n"
    for i in range(6) :
        if list_lotto_num[i] == int(my_n[i]) :
            c += c
            result += "O"
        else :
            result += "X"
    if c == 6 :
        result += "WOW!!!!!"
    return result

@app.route('/', methods=['GET', 'POST'])
def main() :
    if request.method == 'POST':
        my_n = request.form.get('my_n').split()
        if len(my_n) != 6:
            return "Invalid input. Please enter 6 numbers."
        return lotto(my_n)
    return render_template('LOTTO.html')  # HTML file should be in a templates folder

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for, flash, redirect,request
from form import InputForm
import numpy as np
global testing
# import algo
# app = Flask(__name__)

# app.config['SECRET_KEY'] = '51f5fbc2a979ae38655fdb65d9180e19'

# # @app.route("/")
# # @app.route("/home")
# # def home():
# #     return render_template('home.html', posts=posts)

# @app.route("/result",methods=['POST','GET'])
# def result():
#     inputs = request.form.to_dict()

#     input1 = inputs["input1"]
#     input2 = inputs["input2"]

#     result= testing(input1,input2)
#     result1= testingDATA(input1,input2)
#     result2= testingN(input1,input2)
#     result3= testingDATA1(input1,input2)
#     result4= testingDATA2(input1,input2)

#     return render_template('input.html',result = result,result1= result1,result2 = result2,result3 = result3,result4 = result4, title='result')

# @app.route("/", methods=['GET','POST'])
# def generate():
#     form = InputForm()
#     if form.validate_on_submit():
#         flash(f'Data Generated!','success')
#         return redirect(url_for('result'))
#     return render_template('input.html', title='Generate', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)    

def testing(input1,input2):
    def split(word):
        return[char for char in word]

    dna_1 = input1
    dna_2 = input2

    data_1 = split(dna_1)
    data_2 = split(dna_2)

    p = len(data_2)
    q = len(data_1)

    data = np.full((p+2, q+2), 0)
    n = np.full((p+2, q+2), "0")

    # score board:
    gap = -2
    mismatch = -1
    match = 3

    #filling in matrix:
    for k in range (p):
        for i in range (q):
            if (data_1[i]) == (data_2[k]):
                data[2+k, i+2] = match + (data[1+k, i+1])
                n[2+k, i+2] = "m"

            else:
                x = (data[1+k, i+1]) + mismatch
                y = (data[2+k, i+1]) + gap
                z = (data[1+k, i+2]) + gap

                r = max(x, y, z)
                data[2+k, i+2] = r

                if (data[2+k, i+2]) < 0:
                    data[2+k, i+2] = 0

                if r == x:
                    n[2+k, i+2] = "n"

                if r == y:
                    n[2+k, i+2] = "h"

                if r == z:
                    n[2+k, i+2] = "v"

                if data[2+k, i+2] == 0:
                    n[2+k, i+2] = "0"

    print(data)
    print(n)

    # print("The score is %s" % (np.nanmax(data)))
    result = np.nanmax(data)
    return result


def testingDATA(input1,input2):
    def split(word):
        return[char for char in word]

    dna_1 = input1
    dna_2 = input2

    data_1 = split(dna_1)
    data_2 = split(dna_2)

    p = len(data_2)
    q = len(data_1)

    data = np.full((p+2, q+2), 0)
    n = np.full((p+2, q+2), "0")

    # score board:
    gap = -2
    mismatch = -1
    match = 3

    #filling in matrix:
    for k in range (p):
        for i in range (q):
            if (data_1[i]) == (data_2[k]):
                data[2+k, i+2] = match + (data[1+k, i+1])
                n[2+k, i+2] = "m"

            else:
                x = (data[1+k, i+1]) + mismatch
                y = (data[2+k, i+1]) + gap
                z = (data[1+k, i+2]) + gap

                r = max(x, y, z)
                data[2+k, i+2] = r

                if (data[2+k, i+2]) < 0:
                    data[2+k, i+2] = 0

                if r == x:
                    n[2+k, i+2] = "n"

                if r == y:
                    n[2+k, i+2] = "h"

                if r == z:
                    n[2+k, i+2] = "v"

                if data[2+k, i+2] == 0:
                    n[2+k, i+2] = "0"

    return(data)
    print(n)

def testingN(input1,input2):
    def split(word):
        return[char for char in word]

    dna_1 = input1
    dna_2 = input2

    data_1 = split(dna_1)
    data_2 = split(dna_2)

    p = len(data_2)
    q = len(data_1)

    data = np.full((p+2, q+2), 0)
    n = np.full((p+2, q+2), "0")

    # score board:
    gap = -2
    mismatch = -1
    match = 3

    #filling in matrix:
    for k in range (p):
        for i in range (q):
            if (data_1[i]) == (data_2[k]):
                data[2+k, i+2] = match + (data[1+k, i+1])
                n[2+k, i+2] = "m"

            else:
                x = (data[1+k, i+1]) + mismatch
                y = (data[2+k, i+1]) + gap
                z = (data[1+k, i+2]) + gap

                r = max(x, y, z)
                data[2+k, i+2] = r

                if (data[2+k, i+2]) < 0:
                    data[2+k, i+2] = 0

                if r == x:
                    n[2+k, i+2] = "n"

                if r == y:
                    n[2+k, i+2] = "h"

                if r == z:
                    n[2+k, i+2] = "v"

                if data[2+k, i+2] == 0:
                    n[2+k, i+2] = "0"

    return(n)

def testingDATA1(input1,input2):
    def split(word):
        return[char for char in word]

    dna_1 = input1
    dna_2 = input2

    data_1 = split(dna_1)
    data_2 = split(dna_2)

    p = len(data_2)
    q = len(data_1)

    data = np.full((p+2, q+2), 0)
    n = np.full((p+2, q+2), "0")

    # score board:
    gap = -2
    mismatch = -1
    match = 3

    #filling in matrix:
    for k in range (p):
        for i in range (q):
            if (data_1[i]) == (data_2[k]):
                data[2+k, i+2] = match + (data[1+k, i+1])
                n[2+k, i+2] = "m"

            else:
                x = (data[1+k, i+1]) + mismatch
                y = (data[2+k, i+1]) + gap
                z = (data[1+k, i+2]) + gap

                r = max(x, y, z)
                data[2+k, i+2] = r

                if (data[2+k, i+2]) < 0:
                    data[2+k, i+2] = 0

                if r == x:
                    n[2+k, i+2] = "n"

                if r == y:
                    n[2+k, i+2] = "h"

                if r == z:
                    n[2+k, i+2] = "v"

                if data[2+k, i+2] == 0:
                    n[2+k, i+2] = "0"

    print(data)
    print(n)

    # print("The score is %s" % (np.nanmax(data)))
    result = np.nanmax(data)

    #traceback:
    def func(a, b):
        if n[a, b] == "m":
         func(a-1, b-1)

        if n[a, b] == "n":
            func(a-1, b-1)

        if n[a, b] == "v":
            data_1.insert(b-1, "-")
            func(a-1, b)

        if n[a, b] == "h":
            data_2.insert(a-1, "-")
            func(a, b-1)

        if n[a,b] == "0":
            del data_1[0:b-1]
            del data_2[0:a-1]

    for k in (range(p+2)):
        for i in (range(q+2)):
            if data[k, i] == np.nanmax(data):
                r = k
                o = i

    del data_1[o-1:]
    del data_2[r-1:]
    func(r, o)

    return(data_1)
    print(data_2)
 
def testingDATA2(input1,input2):
    def split(word):
        return[char for char in word]

    dna_1 = input1
    dna_2 = input2

    data_1 = split(dna_1)
    data_2 = split(dna_2)

    p = len(data_2)
    q = len(data_1)

    data = np.full((p+2, q+2), 0)
    n = np.full((p+2, q+2), "0")

    # score board:
    gap = -2
    mismatch = -1
    match = 3

    #filling in matrix:
    for k in range (p):
        for i in range (q):
            if (data_1[i]) == (data_2[k]):
                data[2+k, i+2] = match + (data[1+k, i+1])
                n[2+k, i+2] = "m"

            else:
                x = (data[1+k, i+1]) + mismatch
                y = (data[2+k, i+1]) + gap
                z = (data[1+k, i+2]) + gap

                r = max(x, y, z)
                data[2+k, i+2] = r

                if (data[2+k, i+2]) < 0:
                    data[2+k, i+2] = 0

                if r == x:
                    n[2+k, i+2] = "n"

                if r == y:
                    n[2+k, i+2] = "h"

                if r == z:
                    n[2+k, i+2] = "v"

                if data[2+k, i+2] == 0:
                    n[2+k, i+2] = "0"

    print(data)
    print(n)

    # print("The score is %s" % (np.nanmax(data)))
    result = np.nanmax(data)

    #traceback:
    def func(a, b):
        if n[a, b] == "m":
         func(a-1, b-1)

        if n[a, b] == "n":
            func(a-1, b-1)

        if n[a, b] == "v":
            data_1.insert(b-1, "-")
            func(a-1, b)

        if n[a, b] == "h":
            data_2.insert(a-1, "-")
            func(a, b-1)

        if n[a,b] == "0":
            del data_1[0:b-1]
            del data_2[0:a-1]

    for k in (range(p+2)):
        for i in (range(q+2)):
            if data[k, i] == np.nanmax(data):
                r = k
                o = i

    del data_1[o-1:]
    del data_2[r-1:]
    func(r, o)

    return(data_2)

app = Flask(__name__)

app.config['SECRET_KEY'] = '51f5fbc2a979ae38655fdb65d9180e19'

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template('home.html', posts=posts)

@app.route("/result",methods=['POST','GET'])
def result():
    inputs = request.form.to_dict()

    input1 = inputs["input1"]
    input2 = inputs["input2"]

    result= testing(input1,input2)
    result1= testingDATA(input1,input2)
    result2= testingN(input1,input2)
    result3= testingDATA1(input1,input2)
    result4= testingDATA2(input1,input2)

    return render_template('input.html',result = result,result1= result1,result2 = result2,result3 = result3,result4 = result4, title='result')

@app.route("/", methods=['GET','POST'])
def generate():
    form = InputForm()
    if form.validate_on_submit():
        flash(f'Data Generated!','success')
        return redirect(url_for('result'))
    return render_template('input.html', title='Generate', form=form)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')    

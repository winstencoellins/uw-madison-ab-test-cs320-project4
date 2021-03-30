# project: p4
# submitter: coellins@wisc.edu
# partner: none
# hours: 6

import pandas as pd
from flask import Flask, request, jsonify, Response
import os
import re
from matplotlib import pyplot as plt
from io import BytesIO
import random

app = Flask(__name__)
df = pd.read_csv("main.csv")

counter = 1
count_A = 0
count_B = 0

@app.route('/')
def home():
    global counter
    global count_A
    global count_B
    
    if counter <= 10:
        if counter % 2 == 0:
            counter += 1
            with open("index.html") as f:
                html = f.read()

            return html
        else:
            counter += 1
            with open("index2.html") as f:
                html = f.read()
                
            return html
    else:
        if count_A >= count_B:
            with open("index.html") as f:
                html = f.read()

            return html
        else:
            with open("index2.html") as f:
                html = f.read()
                
            return html

@app.route("/donate.html")
def donate():
    global count_A
    global count_B
    
    ver = request.args.get("from")

    if ver == "A":
        count_A += 1
    else:
        count_B += 1

    with open("donate.html") as f:
        html = f.read()

    return html

@app.route('/browse.html')
def browse():
    convert_html = df.to_html()

    f = open('browse.html', 'w')
    f.write(convert_html)
    f.close()
    
    with open('browse.html') as f:
        html = f.read()

    return "<h1>Mobile Legends: Bang Bang Character Data</h1><p>Source: Kaggle.com</p>" + html

@app.route('/email', methods=["POST"])
def email():
    email = str(request.data, "utf-8")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email): # 1
        with open("emails.txt", "a") as f: # open file in append mode
            f.write(email + "\n") # 2
            
        # Counting number of subscriber
        file = open('emails.txt', 'r')
        n = 0
        for line in file:
            if line != "\n":
                n += 1
        file.close()
        
        return jsonify("thanks, you're subscriber number {}!".format(n))
    return jsonify("Email is invalid, please make sure to enter the correct email address with format: email_address@something.something") # 3    

@app.route("/mana.svg")
def plt1():
    plt.figure(figsize=(8, 4))
    plt.scatter(df["MANA_RGN"], df["MANA"], alpha=0.8)
    plt.xlabel("Mana Regen")
    plt.ylabel("Mana")
    plt.title("Mana Regen vs Mana Relation")
    
    f = BytesIO()
    plt.savefig(f, format='svg')
    plt.savefig('mana.svg', format='svg')
    plt.close()
    
    return Response(f.getvalue(), headers={"Content-Type": "image/xml+svg"})

@app.route("/hp.svg")
def plt2():
    plt.figure(figsize=(8, 4))
    plt.scatter(df["HP_RGN"], df["HP"], alpha=0.8)
    plt.xlabel("HP Regen")
    plt.ylabel("HP")
    plt.title("HP Regen vs HP Relation")
    
    f = BytesIO()
    plt.savefig(f, format='svg')
    plt.savefig('hp.svg', format='svg')
    plt.close()
    
    return Response(f.getvalue(), headers={"Content-Type": "image/xml+svg"})

@app.route("/pAtkDfn.svg")
def plt3():
    c = request.args.get("c")
    plt.figure(figsize=(8, 4))
    plt.scatter(df["P_ATK"], df["P_DFN"], color = c, alpha=0.8)
    plt.xlabel("Physical Atk")
    plt.ylabel("Physical Dfn")
    plt.title("Physical Atk vs Physical Dfn")
    
    f = BytesIO()
    plt.savefig(f, format='svg')
    plt.savefig('pAtkDfn.svg', format='svg')
    plt.close()
    
    return Response(f.getvalue(), headers={"Content-Type": "image/xml+svg"},)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, threaded=False) # don't change this line!

# NOTE: app.run never returns (it runs for ever, unless you kill the process)
# Thus, don't define any functions after the app.run call, because it will
# never get that far.
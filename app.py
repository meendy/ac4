import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(_name_)

@app.route('/')
def numeros_primos():

    limite = 100

    c = 1
    p = 1
    numero = 3

    primos = "2,"

    while p < limite:
        primo = 1
        for i in range(2, numero):
            if numero % i == 0:
                primo = 0
                break
        if (primo):
            primos = primos + str(numero) + ","
            p += 1
            if(p%10 == 0):
                primos = primos + "<br>"
        numero+=1

    return primos

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

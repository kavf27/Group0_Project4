from flask import Flask, escape, request
import hashlib
import json

app = Flask(__name__)

@app.route('/')
def root():
    return "Hello, World!"

@app.route('/md5/<str>')
def md5_str():
    val = request.args.get("str")
    m = hashlib.md5()
    m.update(val.encode('utf8'))

    output = {
        "input": val,
        "output": m.hexdigest()
    }
    return json.dumps(output)

@app.route('/factorial/<int>')
def factorial(n):
    if n == 0:
        return 1
    else:
        return n *factorial(n-1)
n = int(input("Input a number to compute the factorial : "))
print(factorial(n))


@app.route('/fibonacci/<int>')
def Fibonacci(n):
    if n<=1:
        return n
    else:
        return(Fibonacci(n-1)+Fibonacci(n-2))
nterms = int(input("Enter an integer: "))

if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(Fibonacci(i))

@app.route('/is-prime/<int>')
def is_prime(n):
    if(n==1):
        return False
    elif(n==2):
        return True
    else:
        for x in range (2,n):
            if(n % x==0):
                return False
        return True
n = int(input("Enter a number: "))
print(is_prime(n))

if __name__=='__main__':
    app.run(host='0.0.0.0', port='5000')
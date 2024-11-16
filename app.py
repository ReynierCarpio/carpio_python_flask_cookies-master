from flask import Flask, request, make_response, jsonify

app = Flask(__name__)

@app.route('/setcookies', methods=['POST'])
def set_cookies():
    # Get the cookie value from the POST request
    cookie_value = request.form.get('cookie_value')
    response = make_response(jsonify({"message": "Cookie has been set!"}))
    # Set the cookie
    response.set_cookie('my_cookie', cookie_value)
    return response

@app.route('/getcookies', methods=['GET'])
def get_cookies():
    # Retrieve the cookie from the request
    cookie_value = request.cookies.get('my_cookie')
    if cookie_value:
        return jsonify({"cookie_value": cookie_value})
    return jsonify({"message": "No cookie found!"})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, session, jsonify, make_response

app = Flask(__name__)
app.json.compact = False

# Secret key used to sign session cookies
app.secret_key = b'?w\x85Z\x08Q\xbdO\xb8\xa9\xb65Kj\xa9_'

@app.route('/sessions/<string:key>', methods=['GET'])
def show_session(key):
    # Set default session values if not already set
    session["hello"] = session.get("hello") or "World"
    session["goodnight"] = session.get("goodnight") or "Moon"

    # Create a response with session and cookie details
    response = make_response(jsonify({
        'session': {
            'session_key': key,
            'session_value': session.get(key, None),
            'session_accessed': session.accessed,
        },
        'cookies': [
            {cookie: request.cookies[cookie]} for cookie in request.cookies
        ],
    }), 200)

    # Add a cookie to the response
    response.set_cookie('mouse', 'Cookie')

    return response

if __name__ == '__main__':
    app.run(port=5555)

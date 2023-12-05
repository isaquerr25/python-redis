from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Route to get a value by key
@app.route('/get/<key>', methods=['GET'])
def get(key):
    value = redis_client.get(key)
    if value is None:
        return jsonify({'error': 'Key not found'}), 404
    return jsonify({key: value.decode('utf-8')})

# Route to set a value for a key
@app.route('/set', methods=['POST'])
def set():
    data = request.get_json()
    key = data['key']
    value = data['value']
    redis_client.set(key, value)
    return jsonify({'success': True})

# Route to update an existing value
@app.route('/update', methods=['PUT'])
def update():
    data = request.get_json()
    key = data['key']
    value = data['value']
    if redis_client.exists(key):
        redis_client.set(key, value)
        return jsonify({'success': True})
    else:
        return jsonify({'error': 'Key not found'}), 404

# Route to delete a key
@app.route('/delete/<key>', methods=['DELETE'])
def delete(key):
    if redis_client.exists(key):
        redis_client.delete(key)
        return jsonify({'success': True})
    else:
        return jsonify({'error': 'Key not found'}), 404

# Route to get all values
@app.route('/getall', methods=['GET'])
def getall():
    keys = redis_client.keys('*')
    data = {key.decode('utf-8'): redis_client.get(key).decode('utf-8') for key in keys}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

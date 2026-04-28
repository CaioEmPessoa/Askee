from main import app

@app.route('/users', methods=['POST'])
def new_user():
    pass

@app.route('/users', methods=['GET'])
def list_users():
    pass

@app.route('/users/<id>', methods=['GET'])
def list_user(id):
    pass

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    pass

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    pass
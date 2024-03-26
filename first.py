from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

dbb=[]

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']


@app.route("/")
def get():
    return jsonify(dbb)


@app.route('/create', methods=['POST'])
def create():
        data = request.json
        result = collection.insert_one(data)
        return jsonify({'message': 'Data created successfully', 'id': str(result.inserted_id)}), 201


@app.route('/read',methods=['POST'])
def read():
    data=request.json
    print(data["name"])
    dbb.append(data)
    return "avs"


# @app.route('/update/<id>', methods=['PUT'])
# def update(id):
#     data = request.json
#     result = collection.update_one({'_id': id}, {'$set': data})
#     if result.modified_count:
#         return jsonify({'message': 'Data updated successfully'}), 200
#     else:
#         return jsonify({'message': 'Data not found'}), 404


        
@app.route("/delete/<id>", methods=["DELETE"])
def delete(id):
    j=0
    for i in dbb:
        print(i)
        if i.id == id:
            print("found")
    return id








if __name__ == '__main__':
    app.run(debug=True)

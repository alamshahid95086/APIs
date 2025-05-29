from flask import Flask, jsonify,request
from flask import Flask

app = Flask(__name__)  # ✅ This is correct


shirt_db=[
    {
        'pack for': 1,
        'brand':'mufti',
        'pricr':1399,
        'size': 'M',
        'fabric':'cotton',
        'sleeve':'Full sleeve',
        'patterd':'solid',
        'collor':'spread'

        },

        {
        'brand':'sparky',
        'pricr':899,
        'size': 'M',
        'fabric':'cotton',
        'sleeve':'half',
        'patterd':'solid',
        'collor':'red'

        }
]
# retrive all the item
@app.route('/shirts')
def shirt_details():
    return jsonify({'shirts':shirt_db})



#retrive one item
@app.route('/shirt/<string:brand>')
def one_item(brand):
    for  shirt in shirt_db:
        if shirt['name']==brand:
            return jsonify(shirt)
    return jsonify({'message':'note found'})

# create item
@app.route('/shirt', methods=['POST'])
def create ():
    Item=request.get_json()
    shirt_db.append(Item)
    return jsonify({'message': 'item addede'})


app.run(port=5000)
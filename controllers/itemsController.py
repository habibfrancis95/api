from flask import request
from flask import jsonify
from flask import make_response
from businessLogic.items import Items
from helpers.generalHelper import GeneralHelper
import json

def initController(flaskApp):
    
    @flaskApp.route('/items', methods=['POST'])
    def addItem():
        json_data = request.get_json()
        result = Items.addItem(json_data['name'], json_data['price'], json_data['categoryId'])
        return json.dumps(result, default=vars), GeneralHelper.getHttpStatusCode(result.code), {'Content-Type':'application/json'}

    @flaskApp.route('/items/<int:id>', methods=['PUT'])
    def updateItem(id):
        json_data = request.get_json()
        result = Items.updateItem(id, json_data['name'], json_data['price'], json_data['categoryId'])
        return json.dumps(result, default=vars), GeneralHelper.getHttpStatusCode(result.code), {'Content-Type':'application/json'}

    @flaskApp.route('/items/<int:id>', methods=['DELETE'])
    def deleteItem(id):
        result = Items.deleteItem(id)
        return json.dumps(result, default=vars), GeneralHelper.getHttpStatusCode(result.code), {'Content-Type':'application/json'}

    @flaskApp.route('/items/<int:id>', methods=['GET'])
    def getItem(id):
        result = Items.getItem(id)
        return json.dumps(result, default=vars), GeneralHelper.getHttpStatusCode(result.code), {'Content-Type':'application/json'}

    @flaskApp.route('/items', methods=['GET'])
    def getItemsList():
        args = request.args
        result = Items.getList(args.get("pageSize", default=10, type=int), args.get("pageNumber", default=1, type=int))
        return json.dumps(result, default=vars), GeneralHelper.getHttpStatusCode(result.code), {'Content-Type':'application/json'}




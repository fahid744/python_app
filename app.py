import json, config
from flask import Flask, request, jsonify
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
# //app.config["DEBUG"] = True


client = Client(config.API_KEY, config.API_SEC, tld='us')

def order(side, quantity, symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print(f"sending order {order_type} - {side} {quantity} {symbol}")
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print("an exception occured - {}".format(e))
        return False

    return True




@app.route("/")
def index():
    return "<h1>Hello WORLD!</h1>"


@app.route("/webhook", methods=['POST'])
def webhook():
    # print(request.data)
    data = json.loads(request.data)
    if data['passphrase'] != config.WEBHOOK_PASSPHRASE_SEC:
        return{
            "code": "error", "message":"Nice Tr, invald phrase"}
        
        
    print (data['ticker'])
    print (data['bar'])

    order_response =order("BUY", 100, DOGEUSD)
    print (order_response)
    return {
        "code": "success",
        "message": data
    
    
    }



# if __name__ == "__app__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)
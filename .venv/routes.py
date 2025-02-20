from flask import jsonify, request, abort
from atm import Get_Balance, Withdraw, Deposite

def init_routes(app):
    @app.route('/accounts/<account_number>/balance', methods = ['GET'])
    def Balance(account_number):
        try:
            balance = Get_Balance(account_number)

            return jsonify({"account" : account_number, "balance" : balance})

        except ValueError as error:
            abort(400, description = error)

    @app.route('/accounts/<account_number>/withdraw', methods = ['POST'])
    def Withdraw_Money(account_number):
        if request.content_type != 'application/json':
            abort(415, description="Content-Type must be application/json")

        try:
            data = request.get_json(silent=True) # Tells Flask to not raise an error if the incoming JSON is invalid.
                                                 # Meant for customize errors

            if not data:
                abort(400, description = "Request body is missing or not valid JSON")

            if "amount" not in data:
                abort(400, description = "Missing 'amount' field in request body")

            amount = data["amount"]

            if not isinstance(amount, (int, float)):
                abort(400, description = "Invalid amount, must be a number")

            updated_balance = Withdraw(account_number, amount)

            return jsonify({"account" : account_number, "balance" : updated_balance})

        except ValueError as error:
            abort(400, description=error)

    @app.route('/accounts/<account_number>/deposit', methods = ['POST'])
    def Deposit_Money(account_number):
        if request.content_type != 'application/json':
            abort(415, description="Content-Type must be application/json")

        try:
            data = request.get_json(silent=True)

            if not data:
                abort(400, description="Request body is missing or not valid JSON")

            if "amount" not in data:
                abort(400, description="Missing 'amount' field in request body")

            amount = data["amount"]

            if not isinstance(amount, (int, float)):
                abort(400, description="Invalid amount, must be a number")

            updated_balance = Deposite(account_number, amount)

            return jsonify({"account" : account_number, "balance" : updated_balance})

        except ValueError as error :
            abort(400, description = error)
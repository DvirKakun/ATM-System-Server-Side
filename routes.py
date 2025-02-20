from flask import jsonify, request, abort
from database import account_manager

def init_routes(app):
    """
      Initializes the API routes for the ATM system.

      Args:
          app (Flask): The Flask application instance.

      Routes:
          GET /accounts/<account_number>/balance
              - Retrieves the balance of a given account.

          POST /accounts/<account_number>/withdraw
              - Withdraws a specified amount from the given account.

          POST /accounts/<account_number>/deposit
              - Deposits a specified amount into the given account.
      """

    @app.route('/accounts/<account_number>/balance', methods = ['GET'])
    def Balance(account_number):
        """
        Retrieves the balance for a given account.

        Args:
            account_number (str): The account number passed in the URL.

        Returns:
            JSON response containing the account number and its balance.

        Raises:
            400 Bad Request: If the account number is invalid or not found.
        """

        try:
            account_number = int(account_number)
            balance = account_manager.Get_Balance(account_number)

            return jsonify({"account" : account_number, "balance" : balance})

        except ValueError as error:
            abort(400, description = error)

    @app.route('/accounts/<account_number>/withdraw', methods = ['POST'])
    def Withdraw_Money(account_number):
        """
        Withdraws money from a given account.

        Args:
            account_number (str): The account number passed in the URL.

        Request Body:
            JSON object with the following structure:
            {
                "amount": <number>
            }

        Returns:
            JSON response containing the updated balance of the account.

        Raises:
            400 Bad Request: If the account number is invalid, the request body is missing, or the amount is invalid.
            415 Unsupported Media Type: If the request Content-Type is not application/json.
        """

        if request.content_type != 'application/json':
            abort(415, description="Content-Type must be application/json")

        try:
            account_number = int(account_number)
            data = request.get_json(silent=True) # Tells Flask to not raise an error if the incoming JSON is invalid.
                                                 # Meant for customize errors

            if not data:
                abort(400, description = "Request body is missing or not valid JSON")

            if "amount" not in data:
                abort(400, description = "Missing 'amount' field in request body")

            amount = data["amount"]

            if not isinstance(amount, (int, float)):
                abort(400, description = "Invalid amount, must be a number")

            updated_balance = account_manager.Withdraw(account_number, amount)

            return jsonify({"account" : account_number, "balance" : updated_balance})

        except ValueError as error:
            abort(400, description=error)

    @app.route('/accounts/<account_number>/deposit', methods = ['POST'])
    def Deposit_Money(account_number):
        """
        Deposits money into a given account.

        Args:
            account_number (str): The account number passed in the URL.

        Request Body:
            JSON object with the following structure:
            {
                "amount": <number>
            }

        Returns:
            JSON response containing the updated balance of the account.

        Raises:
            400 Bad Request: If the account number is invalid, the request body is missing, or the amount is invalid.
            415 Unsupported Media Type: If the request Content-Type is not application/json.
        """

        if request.content_type != 'application/json':
            abort(415, description="Content-Type must be application/json")

        try:
            account_number = int(account_number)
            data = request.get_json(silent=True)

            if not data:
                abort(400, description="Request body is missing or not valid JSON")

            if "amount" not in data:
                abort(400, description="Missing 'amount' field in request body")

            amount = data["amount"]

            if not isinstance(amount, (int, float)):
                abort(400, description="Invalid amount, must be a number")

            updated_balance = account_manager.Deposite(account_number, amount)

            return jsonify({"account" : account_number, "balance" : updated_balance})

        except ValueError as error :
            abort(400, description = error)
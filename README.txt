ATM System Server-Side

1. Approach, Design Decisions, and Challenges

I began this project by thoroughly reading the assignment document and understanding the requirements and constraints.
Before starting to code, I focused on determining the tools and technologies that would best fit the project.
Specifically, I had to decide on the programming language, relevant packages, and modules.
After evaluating my options, I chose Python, as it is well-suited for quick development, has excellent libraries, and provides great support for both object-oriented programming (OOP) and web APIs.

When I was ready to begin the implementation, I focused on the design and architecture of the system. My main goal was to create a readable and maintainable structure that would allow for future extensions or changes without major rewrites.
I decided that the best way to structure the project was by using OOP principles.

To organize the data, I created an Account class, which represents a single account.
This class holds the account details such as account number and balance, and it also includes methods for transactions like deposits, withdrawals, and balance retrieval.

For managing multiple accounts, I created an AccountManager class.
This class serves as the main controller for the application - It stores the collection of accounts in a dictionary and provides methods for adding accounts, depositing money, withdrawing money, and retrieving account balances.
It also ensures that account numbers are unique when adding new accounts.

After completing the backend logic, I moved on to implementing the API.
For this, I chose the Flask package, which is lightweight, intuitive, and well-documented - Flask's simplicity made it an ideal choice for this project, allowing me to quickly define endpoints and handle HTTP requests.

When designing the API, I focused on ensuring it was both user-friendly and error-resilient.
I considered the common usage patterns for the API, ensuring that users could easily interact with it without confusion.
For the Withdraw and Deposit endpoints, I required users to provide the account number as part of the URL, and the transaction amount as part of the request body, formatted in JSON.
This design made the API easy to use and ensured all necessary data was available.

A major challenge I faced was handling edge cases and errors.
While the system worked as expected for most requests, I encountered issues where users might send incorrect inputs, such as invalid amounts or account numbers.
To address these issues, I reviewed all potential edge cases, implemented error handling logic, and used the HTTPException class from the werkzeug.exceptions module to return custom error messages in JSON format.
This improved the user experience by providing clear and informative error responses.

The next challenge was testing and deployment.
For testing, I used Postman, a widely used API testing tool, to simulate requests and examine how the API handles edge cases.
For deployment, I chose Render, a platform that allows easy hosting of web applications.
I had to configure a few settings, including the correct build and run commands for Flask, and structure the project folders to ensure Render could find and execute the necessary files.
After linking my GitHub repository to Render, I successfully deployed the app using the gunicorn server.

Once deployed, I performed another round of testing using Postman to ensure that everything worked as expected.

Throughout the development process, I kept the Separation of Concerns principle in mind, ensuring that each file had a specific role and responsibility.
This approach made the codebase easy to read and maintain.
The project structure consists of six files: main.py, account.py, account_manager.py, database.py, routes.py, and error_handler.py.
This modular structure allows for easy updates and extensions in the future.

2. API Instructions

Get Balance
    URL: GET https://atm-system-server-side.onrender.com/accounts/{account_number}/balance
    Parameters:
        account_number: An integer between 1 and 5 representing the account number.

    Response: Returns the balance of the specified account.

Withdraw
    URL: POST https://atm-system-server-side.onrender.com/accounts/{account_number}/withdraw
    Parameters:
        account_number: An integer between 1 and 5 representing the account number.
    Body (required):
        The request body must contain a JSON object with the following structure:
        {
            "amount": <number>
        }
        amount: A positive number representing the amount to withdraw.

    Response: Returns the updated balance after the withdrawal.

Deposit
    URL: POST https://atm-system-server-side.onrender.com/accounts/{account_number}/deposit
    Parameters:
        account_number: An integer between 1 and 5 representing the account number.
    Body (required):
        The request body must contain a JSON object with the following structure:
        {
            "amount": <number>
        }
        amount: A positive number representing the amount to deposit.

    Response: Returns the updated balance after the deposit.
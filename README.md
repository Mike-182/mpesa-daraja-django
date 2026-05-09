# Django M-Pesa Daraja API Integration (STK Push)

A professional implementation of Safaricom's Daraja API using the Django framework. This project demonstrates how to initiate STK Push (Lipa Na M-Pesa Online) and handle asynchronous callbacks.

Features
* **OAuth 2.0 Authentication:** Securely generates access tokens.
* **STK Push Initiation:** Triggers the M-Pesa PIN prompt on the user's mobile device.
* **Secure Callbacks:** A dedicated webhook to receive and process transaction results from Safaricom.
* **Environment Security:** Uses `.env` to protect sensitive API credentials.

Tech Stack
* **Backend:** Python / Django
* **API Integration:** django-daraja
* **Security:** python-dotenv

Logic Flow
1. **Request:** The user enters their phone number and amount on the frontend.
2. **Handshake:** The system authenticates with Daraja using Consumer Keys.
3. **Push:** An STK Push request is sent to the Safaricom Gateway.
4. **User Action:** The user enters their PIN on their phone.
5. **Callback:** Safaricom sends a JSON response to our `callback_url` to confirm if the payment was successful or cancelled.

Setup
1. Clone the repo: `git clone <your-repo-url>`
2. Install requirements: `pip install -r requirements.txt`
3. Create a `.env` file and add your `DARAJA_CONSUMER_KEY`, `DARAJA_CONSUMER_SECRET`, and `DARAJA_PASSKEY`.
4. Run migrations: `python manage.py migrate`
5. Start server: `python manage.py runserver`

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://127.0.0.1:5500")  # Replace with your frontend URL

@app.route('/submit', methods=['POST', 'OPTIONS'])
def handle_form_data():
    if request.method == 'POST':
        # Get form data
        gender = request.form.get('gender')
        age = int(request.form.get('age'))  # Convert age to integer
        icu_nicu = request.form.get('icu_nicu')
        admission = request.form.get('admission')
        insurance = request.form.get('insurance')
        religion = request.form.get('religion')
        ethnicity = request.form.get('ethnicity')
        marital_status = request.form.get('marital_status')

        # Get data from numeric input fields (assuming all are required)
        blood = int(request.form.get('blood'))
        circulatory = int(request.form.get('circulatory'))
        congenital = int(request.form.get('congenital'))
        digestive = int(request.form.get('digestive'))
        endocrine = int(request.form.get('endocrine'))
        genitourinary = int(request.form.get('genitourinary'))
        infectious = int(request.form.get('infectious'))
        injury = int(request.form.get('injury'))
        mental = int(request.form.get('mental'))
        misc = int(request.form.get('misc'))
        muscular = int(request.form.get('muscular'))
        neoplasms = int(request.form.get('neoplasms'))
        nervous = int(request.form.get('nervous'))
        pregnancy = int(request.form.get('pregnancy'))
        prenatal = int(request.form.get('prenatal'))
        respiratory = int(request.form.get('respiratory'))
        skin = int(request.form.get('skin'))

        # Now you have all the form data
        # You can process, store, or display the data as needed
        print(f"Gender: {gender}")
        print(f"Age: {age}")
        # ... (print other data similarly)

        # You can also return a response to the client
        return "Form data received successfully!"
    elif request.method == 'OPTIONS':
        # Respond to CORS preflight request
        response = app.make_default_options_response()
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

if __name__ == '__main__':
    app.run(debug=True)

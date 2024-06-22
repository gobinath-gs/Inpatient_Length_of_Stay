from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the machine learning model
model = joblib.load('model.pkl')


def convert(result):
    # Calculate the number of days
    days = int(result)
    
    # Calculate the remaining hours
    hours = round((result - days) * 24)
    
    # Return the result as a string
    return f"{days} days and {hours} hours"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        
        # Extracting values from form inputs
        insurance_input = request.form['insurance'].lower()
        religion_input = request.form['religion'].lower()
        ethnicity_input = request.form['ethnicity'].lower()
        marital_status_input = request.form['marital_status'].lower()

        # Converting 'insurance' input to dictionary
        insurance = {
            "INS_Government": 1 if insurance_input == "government" else 0,
            "INS_Medicaid": 1 if insurance_input == "medicaid" else 0,
            "INS_Medicare": 1 if insurance_input == "medicare" else 0,
            "INS_Private": 1 if insurance_input == "private" else 0,
            "INS_Self Pay": 1 if insurance_input == "selfpay" else 0
        }

        # Converting 'religion' input to dictionary
        religion_columns = {
            "REL_NOT SPECIFIED": 1 if religion_input == "not specified" else 0,
            "REL_RELIGIOUS": 1 if religion_input == "religious" else 0,
            "REL_UNOBTAINABLE": 1 if religion_input == "unobtainable" else 0
        }

        # Converting 'ethnicity' input to dictionary
        ethnicity_columns = {
            "ETH_ASIAN": 1 if "asian" in ethnicity_input else 0,
            "ETH_BLACK/AFRICAN AMERICAN": 1 if "black" in ethnicity_input or "african american" in ethnicity_input else 0,
            "ETH_HISPANIC/LATINO": 1 if "hispanic" in ethnicity_input or "latino" in ethnicity_input else 0,
            "ETH_OTHER/UNKNOWN": 1 if "other" in ethnicity_input or "unknown" in ethnicity_input else 0,
            "ETH_WHITE": 1 if "white" in ethnicity_input else 0
        }

        # Converting 'marital_status' input to dictionary
        marital_status_columns = {
            "MAR_DIVORCED": 1 if "divorced" in marital_status_input else 0,
            "MAR_LIFE PARTNER": 1 if "life partner" in marital_status_input else 0,
            "MAR_MARRIED": 1 if "married" in marital_status_input else 0,
            "MAR_SEPARATED": 1 if "separated" in marital_status_input else 0,
            "MAR_SINGLE": 1 if "single" in marital_status_input else 0,
            "MAR_UNKNOWN (DEFAULT)": 1 if "unknown" in marital_status_input else 0,
            "MAR_WIDOWED": 1 if "widowed" in marital_status_input else 0
        }

        # Collecting form data
        form_data = {
            'gender': 1 if request.form['gender'].lower() == "female" else 0,
            'age_newborn': 1 if int(request.form['age']) <= 14 else 0,
            'age_young_adult': 1 if 14 < int(request.form['age']) <= 34 else 0,
            'age_middle_adult': 1 if 34 < int(request.form['age']) <= 50 else 0,
            'age_senior': 1 if int(request.form['age']) > 50 else 0,
            'icu': 1 if request.form['icu_nicu'].lower() == "icu" else 0,
            'nicu': 1 if request.form['icu_nicu'].lower() == "nicu" else 0,
            'admission': {
        "ADM_ELECTIVE": 1 if request.form['admission'] == "elective" else 0,
        "ADM_EMERGENCY": 1 if request.form['admission'] == "emergency" else 0,
        "ADM_NEWBORN": 1 if request.form['admission'] == "newborn" else 0,
        "ADM_URGENT": 1 if request.form['admission'] == "urgent" else 0
    },
            'insurance': insurance,
            'religion': religion_columns,
            'ethnicity': ethnicity_columns,
            'marital_status': marital_status_columns,
            'blood': float(request.form['blood']),
            'circulatory': float(request.form['circulatory']),
            'congenital': float(request.form['congenital']),
            'digestive': float(request.form['digestive']),
            'endocrine': float(request.form['endocrine']),
            'genitourinary': float(request.form['genitourinary']),
            'infectious': float(request.form['infectious']),
            'injury': float(request.form['injury']),
            'mental': float(request.form['mental']),
            'misc': float(request.form['misc']),
            'muscular': float(request.form['muscular']),
            'neoplasms': float(request.form['neoplasms']),
            'nervous': float(request.form['nervous']),
            'pregnancy': float(request.form['pregnancy']),
            'prenatal': float(request.form['prenatal']),
            'respiratory': float(request.form['respiratory']),
            'skin': float(request.form['skin']),
        }
        
        print(form_data)


        

# Extracting individual values from form_data dictionary
        gender = form_data['gender']
        age_newborn = form_data['age_newborn']
        age_young_adult = form_data['age_young_adult']
        age_middle_adult = form_data['age_middle_adult']
        age_senior = form_data['age_senior']
        icu = form_data['icu']
        nicu = form_data['nicu']
        admission = form_data['admission']

        # Creating the DataFrame
        user_data = pd.DataFrame({
            "GENDER": gender,
            "AGE_newborn": age_newborn,
            "AGE_young_adult": age_young_adult,
            "AGE_middle_adult": age_middle_adult,
            "AGE_senior": age_senior,
            "ICU": icu,
            "NICU": nicu,
            **admission,
            **form_data['insurance'],
            **form_data['religion'],
            **form_data['ethnicity'],
            **form_data['marital_status'],
            'BLOOD': form_data['blood'],
            'CIRCULATORY': form_data['circulatory'],
            'CONGENITAL': form_data['congenital'],
            'DIGESTIVE': form_data['digestive'],
            'ENDOCRINE': form_data['endocrine'],
            'GENITOURINARY': form_data['genitourinary'],
            'INFECTIOUS': form_data['infectious'],
            'INJURY': form_data['injury'],
            'MENTAL': form_data['mental'],
            'MISC': form_data['misc'],
            'MUSCULAR': form_data['muscular'],
            'NEOPLASMS': form_data['neoplasms'],
            'NERVOUS': form_data['nervous'],
            'PREGNANCY': form_data['pregnancy'],
            'PRENATAL': form_data['prenatal'],
            'RESPIRATORY': form_data['respiratory'],
            'SKIN': form_data['skin']
        }, index=[0])
        # Creating DataFrame from form data
        

        # Making prediction using the model
        prediction = model.predict(user_data)

        # Rendering the prediction result
        return render_template('predict.html', prediction=convert(prediction[0][0]))

if __name__ == '__main__':
    app.run(debug=True)

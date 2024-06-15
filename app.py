from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Function to read data from uploaded file
def read_data(file_path):
    df = pd.read_excel(file_path)  # Use pd.read_csv() for CSV files
    return df

# Read data from the uploaded file
file_path = "C:\\Users\\Administrator\\Pictures\\Certificate verification project\\InternshipCertificates.xlsx"  # Replace with the actual file path
certificate_data = read_data(file_path)

# Endpoint to render the verification HTML page
@app.route('/verification')
def verification_page():
    return render_template('index.html')  # Render the HTML template from the 'templates' folder

# Endpoint to verify certificate
@app.route('/verify_certificate', methods=['GET'])
def verify_certificate():
    unique_id = request.args.get('unique_id')
    row = certificate_data.loc[certificate_data['Unique ID'] == unique_id]

    if row.empty:
        return jsonify({'error': 'Certificate not found'})

    name = row['Name'].values[0]
    domain = row['Domain'].values[0]
    task_level = row['Task Level'].values[0]

    return jsonify({'name': name, 'domain': domain, 'task_level': task_level})

if __name__ == '__main__':
    app.run(debug=True)

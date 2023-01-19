import pandas as pd
from echa.impactanalysis import impact_analysis
from echa.echa_scrapper import element_ref_link, REACH_STATUS
from echa.exception import ECHAException
import sys
import pandas as pd
from flask import Flask, render_template, request
from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, request, render_template, jsonify, url_for


app = Flask(__name__)

def single_query(sub:str):
    substance = sub
    try:
        impact_status = impact_analysis(m=substance)
        return impact_status
        
    except Exception as e:
        raise ECHAException(e, sys)
    
def batch_query():
    batch_input_file = pd.read_csv(r"C:\Users\soshukla\Desktop\ECHA\Batch_Input.csv")
    input = input = [i for i in batch_input_file["PART NUMBER"]]
    try:
        batch_out_put =[]
        for i in input[0:100]:
            impact_stsus = impact_analysis(i)
            batch_out_put.append(impact_stsus)
                
        df = pd.DataFrame(batch_out_put, columns= ["PART NUMBER","REACH STATUS", "FOT", "PART DESCRIPTION", "COMMENT"])
        df["PART NUMBER"] = pd.DataFrame(input)
        df.to_excel('Batch_output.xlsx', sheet_name='Batch_Output_DataSheet')
        return print("Batch query completed, download excel file")
        
    except Exception as e:
        raise ECHAException(e, sys)
    
def substance_status(substance):
    sub = substance
    try:
        links = element_ref_link(sub)
        element_status = REACH_STATUS(ref=links)
        return element_status
        
    except Exception as e:
        raise ECHAException(e, sys)
    
@app.route("/")
def Home():

 return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/preAssessment")
def preAssesment():
    return render_template("preAssessment.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    #app.run(debug=True)
    # Call for single query >>>>>>>>
    PN, STATUS,_,_,_= single_query('NSA5120B10')
    print(f"PART NUMBER:", {PN},"\nPART STATUS: ", {STATUS})
    
    # Call for batch query >>>>>>>>>
    #batch_Q = batch_query()
    
    # Call for substance REACH Impact analysis
    #substance_info = substance_status("Chromium trioxide")
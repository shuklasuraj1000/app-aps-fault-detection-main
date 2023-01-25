import pandas as pd
from echa.impactanalysis import impact_analysis
from echa.echa_scrapper import element_ref_link, REACH_STATUS
from echa.exception import ECHAException
import sys
import pandas as pd
from flask import Flask, render_template, request
from flask import Flask, render_template, url_for, flash, redirect
from flask import Flask, request, render_template, jsonify, url_for
from echa.impactanalysis import impact_analysis
from echa.echa_scrapper import element_ref_link, REACH_STATUS
from echa.exception import ECHAException
from flask_cors import CORS, cross_origin

app = Flask(__name__)

#@app.route('/single_query',methods=['POST','GET']) # route to show channel name, videos title (max 329), and URL of videos in a web UI
#@cross_origin()
#def single_query(sub:str):
    #if request.method == 'POST':
        #substance = sub
        #substance = request.form['pno']
        #try:
            #impact_status = impact_analysis(m=substance)
            #print(impact_status)
            #return render_template('index.html', impact_status)
            
        #except Exception as e:
            #raise ECHAException(e, sys)


#Single Query SearchFunction
def single_query(sub:str):
    substance = sub
    try:
        impact_status = impact_analysis(m=substance)
        #print (impact_status)
        return  impact_status
        
    except Exception as e:
        raise ECHAException(e, sys)


#Sinngle_Query Function Mapping TO Index Page
@app.route('/test', methods = ['POST', 'GET'])
@cross_origin()
def fun():
    if request.method == 'POST':
      user  = request.form['pno']
      res =single_query(user)
    if user == res :
      #res = single_query(user)
        return  render_template("index.html", res)
   
    else:
      return  render_template("index.html", res =single_query(user))



def batch_query():
    batch_input_file = pd.read_csv(r"C:\Users\soshukla\Desktop\ECHA\Batch_Input.csv")
     #batch_input_file = pd.read_csv(r"C:\Users\pdhayarkar\Downloads\ECHA\ECHA\Batch_Input.csv")
    input = input = [i for i in batch_input_file["PART NUMBER"]]
    try:
        batch_out_put =[]
        for i in input:
            impact_stsus = impact_analysis(i)
            batch_out_put.append(impact_stsus)
        df = pd.DataFrame(batch_out_put, columns= ["PART NUMBER","REACH STATUS"])
        return df
        
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




@app.route("/",methods = ['POST', 'GET'])
@cross_origin()
def Home():
 return render_template("index.html")        

@app.route("/about")
@cross_origin()
def about():
    return render_template("about.html",single_query=single_query)

@app.route("/preAssessment")
@cross_origin()
def preAssesment():
    return render_template("preAssessment.html")

@app.route("/contact")
@cross_origin()
def contact():
    return render_template("contact.html")

@app.route("/index")
@cross_origin()
def index():
    return render_template("index.html")
    
    

if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
    app.run(debug=True)
    # Call for single query >>>>>>>>
    #echa = single_query('ASNA2352')
    #print(echa)
    
    
    # Call for batch query >>>>>>>>>
    #batch_Q = batch_query()
    #print(batch_Q)
    
    # Call for substance REACH Impact analysis
    #substance_info = substance_status("Cadmium")
    


    

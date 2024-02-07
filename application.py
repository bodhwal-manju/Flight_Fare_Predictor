from flask import Flask,request,render_template,jsonify
# from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd  
import os
application=Flask(__name__)

model=pickle.load(open("flight_rf.pkl","rb"))
#with open("flight_price_pred_new.pkl", 'rb') as model1:
        # data=model.read(1000)
       # model= pickle.load(model1)





@application.route("/predict",methods=["GET","POST"])
# @cross_origin()


def predict():
    if request.method=="POST":
        # Date of Journey
        date_dep=request.form["Dep_Time"]
        Journey_day=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").day)
        Journey_month=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").month)

        # print("Journey Date:",Journey_day,Journey_month)

        #Departure
        Dep_hour=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").hour)
        Dep_min=int(pd.to_datetime(date_dep,format="%Y-%m-%dT%H:%M").minute)

        #print("Departure:",Dep_hour,Dep_min)

        #Arrival
        date_arr=request.form["Arrival_Time"]
        Arrival_hour=int(pd.to_datetime(date_arr,format="%Y-%m-%dT%H:%M").hour)
        Arrival_min=int(pd.to_datetime(date_arr,format="%Y-%m-%dT%H:%M").minute)
        # print("Arrival:",Arrival_hour,Arrival_min)

        #Duration
        dur_hour=abs(Arrival_hour-Dep_hour)
        dur_min=abs(Arrival_min-Dep_min)
        # print("Duration:",dur_hour,dur_min)

        #Total Stops

        Total_stops=int(request.form["stops"])
        #print(Total_stops)

        #Airline
        #Air Asia=0(not in column)

        airline=request.form['airline']
        if(airline=='Jet Airways'):
            Jet_Airways=1
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=='Indigo'):
            Jet_Airways=0
            Indigo=1
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0    

        elif(airline=='Air India'):
            Jet_Airways=0
            Indigo=0
            Air_India=1
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=='Multiple_carriers'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=1
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0        

        elif(airline=='SpiceJet'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=1
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=='Vistara'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=1
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0


        elif(airline=='GoAir'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=1
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0    

        elif(airline=='Multiple carriers Premium Economy'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=1
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=='Jet Airways Business'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=1
            Vistara_Premium_economy=0
            Trujet=0

        elif(airline=='Vistara Premium Economy'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=1
            Trujet=0


        elif(airline=='Trujet'):
            Jet_Airways=0
            Indigo=0
            Air_India=0
            Multiple_carriers=0
            SpiceJet=0
            Vistara=0
            GoAir=0
            Multiple_carriers_Premium_economy=0
            Jet_Airways_Business=0
            Vistara_Premium_economy=0
            Trujet=1                        

        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        
        elif (Source == 'Kolkata'):
            s_Delhi = 0
            s_Kolkata = 1
            s_Mumbai = 0
            s_Chennai = 0
   
        elif (Source == 'Mumbai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 1
            s_Chennai = 0
        
        elif (Source == 'Chennai'):
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 1
   
        else:
            s_Delhi = 0
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
   

        Source = request.form["Destination"]
        if (Source == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        
        elif (Source == 'Delhi'):
            d_Cochin = 0
            d_Delhi = 1
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'New_Delhi'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 1
            d_Hyderabad = 0
            d_Kolkata = 0

        elif (Source == 'Hyderabad'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 1
            d_Kolkata = 0

        elif (Source == 'Kolkata'):
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 1

        else:
            d_Cochin = 0
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        


        prediction=model.predict([[
            Total_stops,
            Journey_day,
            Journey_month,
            Dep_hour,
            Dep_min,
            Arrival_hour,
            Arrival_min,
            dur_hour,
            dur_min,
            Air_India,
            GoAir,
            Indigo,
            Jet_Airways,
            Multiple_carriers,
            SpiceJet,
            Vistara,
            Vistara_Premium_economy,
            s_Chennai,
            s_Kolkata,
            s_Mumbai,
            d_Cochin,
            d_Delhi,
            d_Hyderabad,
            d_Kolkata
        
        ]])

        output=round(prediction[0],2)

        # return render_template('home.html',prediction_text="Your Flight price is Rs. {}".format(output))
        return jsonify({"prediction_text": "Your Flight price is Rs. {}".format(output)})


    return render_template("home.html")
@application.route("/")
# @cross_origin()

def home():
    return render_template('home.html')




if __name__ == "__main__":
    application.run(debug=True)
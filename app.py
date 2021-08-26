# Please refer below excel file, which has 512 records with six API's (
#       X axis (180 angle)	Y axis (90 angle)	Diagonal (45 angle)	Diagonal (135 angle)	All (all)	None
# ) to be created, so in the frontend if the user clicks on X axis (180 angle) they only see the images (File Name) = 1 
# for this column and not any other columns so in this case there will be 40 records.

from flask import Flask, app, request
import pandas as pd
from pandas.core.frame import DataFrame

app = Flask(__name__)

@app.route('/')
def index():     
    return "Hello There!!"

@app.route("/images")
def getImages():
    response = ""
    headers = request.headers
    try:
        response = process_data(headers['Image-Name'])
    except Exception as ex:
        response = "An Error Occured:" + str(ex) 
    
    return response    
        

def process_data(column):
    if column == "X axis (180 angle)" or "Y axis (90 angle)" or "Diagonal (45 angle)" or "Diagonal (135 angle)" or "All (all)" or "None" :
        row_data = pd.read_excel('test.xlsx')
        dataframe = pd.DataFrame(row_data)
        processed_data = dataframe[dataframe[column] == 1][["Id","File Name", column]].to_json(orient = 'records')
        return processed_data
    else:
        return "Invalid Column type!"
    
    
if __name__ == "__main__":
    app.run(debug = True)
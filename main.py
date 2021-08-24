from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import numpy as np
from flask import Flask, request, render_template
import pickle
import logging

logging.basicConfig(filename="logs/logdata.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

logger.setLevel(logging.INFO)

app = Flask(__name__)


# Creates Connection with the database.
cloud_config = {
    'secure_connect_bundle': 'secure-connect-storesalespredictor.zip'
}
auth_provider = PlainTextAuthProvider('zOZtyozAakSXvUxsyxLoktUw',
                                      'AhSpbJ,f_84-vay_buAntESDL_iyDB+-wUjduUX8,a3P4n8qDOU7WWWPkDH5cOSFJs.x+A-zDYur9cjFHHzdwLDtz97zTmQ+bv0vSfcPeKZaOGLk_jrw6NsAZc+,C55s')
cluster = Cluster(protocol_version=3, cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


session.execute("USE ds")
row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")


try:
    logging.info("Creating Table In DataBase...")
    session.execute("CREATE TABLE Sales(id uuid PRIMARY KEY,Item_Weight float,Item_MRP float,Outlet_Location_Type text,Item_Visibility float,Item_Fat_Content text,Item_type text,Outlet_Size text,Outlet_Type text);")
except:
    logging.info("Table Already Created...")


@app.route('/')
def home():
    return render_template("sales.html")


# prediction function


def ValuePredictor(to_predict_list):
    logging.info("Scaling Data...")
    to_predict = np.array(to_predict_list, dtype="float")
    lst = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype="float")
    # Item Weight
    lst[0] = to_predict[0]
    # Item MRP
    lst[1] = to_predict[1]
    # Outlet Location Type
    lst[2] = to_predict[2]
    # Item Visibility
    lst[3] = to_predict[3]

    # Item Fat content
    if to_predict[4] == 0:
        lst[4] = 1
    else:
        lst[5] = 1

    # Item Type
    if to_predict[5] == 0:
        lst[6] = 1
    elif to_predict[5] == 1:
        lst[7] = 1
    else:
        lst[8] = 1

    # Outlet Size
    if to_predict[6] == 2:
        lst[9] = 1
    elif to_predict[6] == 1:
        lst[10] = 1
    else:
        lst[11] = 1

    # Outlet Type
    if to_predict[7] == 0:
        lst[12] = 1
    elif to_predict[7] == 1:
        lst[13] = 1
    elif to_predict[7] == 2:
        lst[14] = 1
    else:
        lst[15] = 1

    lst = np.array(lst).reshape(1, 16)
    logging.info("Loading model...")
    loaded_model = pickle.load(open("sales_flask.pkl", "rb"))
    logging.info("Model Loaded Successfully...")
    logging.info("Predicting Output...")
    result = loaded_model.predict(lst)
    return result[0]


def storeData(pl):
    if pl[2] == "1":
        pl[2] = "Type 1"
    if pl[2] == "2":
        pl[2] = "Type 2"
    if pl[2] == "3":
        pl[2] = "Type 3"

    if pl[4] == "0":
        pl[4] = "Low Fat"
    if pl[4] == "1":
        pl[4] = "Regular"

    if pl[5] == "0":
        pl[5] = "Drinks"
    if pl[5] == "1":
        pl[5] = "Food"
    if pl[5] == "2":
        pl[5] = "Others"

    if pl[6] == "0":
        pl[6] = "Small"
    if pl[6] == "1":
        pl[6] = "Medium"
    if pl[6] == "2":
        pl[6] = "High"

    if pl[7] == "0":
        pl[7] = "Grocery Store"
    if pl[7] == "1":
        pl[7] = "Supermarket Type 1"
    if pl[7] == "2":
        pl[7] = "Supermarket Type 2"
    if pl[7] == "3":
        pl[7] = "Supermarket Type 3"
    column = "id, Item_Weight, Item_MRP,Outlet_Location_Type, Item_Visibility, Item_Fat_Content, Item_Type,Outlet_Size, Outlet_Type"
    value = "{0},{1},{2},'{3}',{4},'{5}','{6}','{7}','{8}'".format('uuid()', pl[0],
                                                                   pl[1], pl[2],
                                                                   pl[3], pl[4],
                                                                   pl[5], pl[6],
                                                                   pl[7])

    logging.info("Inserting Data To DataBase...")
    insert = "INSERT INTO DS.Sales ({}) VALUES ({});".format(column, value)
    session.execute("USE ds")
    session.execute(insert)
    ins = "Data Inserted : {}".format(value)
    logging.info(ins)


# Output page

@app.route('/result', methods=["POST"])
def result():
    if request.method == "POST":
        logger.info(" ")

        logger.info("Collecting Data From User...")
        to_predict_list = request.form.to_dict()
        logger.info("Data Collected From User...")
        to_predict_list = list(to_predict_list.values())

        try:
            pl = to_predict_list.copy()
            try:
                storeData(pl)
            except:
                logging.info("Data Not Inserted...")
            to_predict_list = list(map(float, to_predict_list))
        except:
            logging.error("Invalid Data Entered...")
            return render_template("error.html")

        result = round(ValuePredictor(to_predict_list), 2)
        p1 = round(result - (result*0.32), 2)
        p2 = round(result + (result*0.21), 2)
        logging.info("Process Completed....")
        return render_template("result.html", prediction1=p1, prediction2=p2)


# Main function
if __name__ == "__main__":
    app.run(debug=True)
    app.config["TEMPLATES_AUTO_RELODE"] = True

from flask import Flask, render_template, request, redirect, url_for
import os
from os.path import join, dirname, realpath
import pandas as pd
from Model import db, Restaurant, RestaurantSchema

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    UPLOAD_FOLDER = 'static/files'
    app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
    
    @app.route('/')
    def index():
        # se renderiza el templeate para subir el archivo'
        return render_template('uploas_csv.html')

    @app.route("/", methods=['POST'])
    def uploadFiles():
        # se optiene el file y se guarda
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            uploaded_file.save(file_path)
            parseCSV(file_path)
            # se guarda el csv
        return redirect(url_for('index'))

    def parseCSV(filePath):
        
        # se lee con pandas el archivo
        csvData = pd.read_csv(filePath)
        # Lse van guardando, los restaurantes, si exite no se guarda
        for i,row in csvData.iterrows():
            try:
                restaurant = Restaurant(_id=row[0],
                    rating=row[1],
                    name=row[2],
                    site=row[3],
                    email=row[4],
                    phone=row[5],
                    street=row[6],
                    city=row[7],
                    state=row[8],
                    lat=row[9],
                    lng=row[10]
                )
                db.session.add(restaurant)
                db.session.commit()
            except:
                print("already exist")
   
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/restaurants')

    from Model import db
    db.init_app(app)

    return app


app = create_app("config")
if __name__ == "__main__":
    app = create_app("config")
    app.run(debug=False)
    
    
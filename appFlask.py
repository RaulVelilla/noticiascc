import pandas as pandas
import numpy as np
import sklearn
import joblib
from flask import Flask,render_template,request
app=Flask(___name___)

@app.route("/")
def index():
  return render_template('index.html')
@app.route('/prediccion',methods=['GET','POST'])
def predict():
  if request.method =='POTS':
    try:
      var_1=float(request.from["var_1"])
      

      pred_args=[var_1]
      pred_arr=np.array(pred_args)
      preds=pred_arr.reshape(1,-1)
      modelo=open("./modelo.pkl","rb")
      modelo_clas=joblib.load(modelo)
      prediccion_modelos=modelo_clas.predict(preds)
      prediccion_modelo=round(float(prediccion_modelo) ,2)
      if prediccion_modelo == 1.0:
        predicción_modelo = "La Noticia es verdadera"
      else:
        prediccion_modelo= "La Noticia es falsa"
    except ValueError:
        return "por favor escriba la Noticia"
    return render_template('prediccion.html',prediccion=prediccion_modelo)
  if ___name___=='__main__':
    app.run(debug=True)
    

    






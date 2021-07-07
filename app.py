from flask import Flask,request,jsonify
from flask_cors import CORS
import recommendation
app=Flask(__name__)
CORS(app)
@app.route('/movies',methods=['GET'])
def recommend_movies():
    tit=request.args.get('title')
    gen=request.args.get('genres')
    res=recommendation.give_result(tit,gen)
    return jsonify(res)
if __name__=='__main__':
    app.run(port=5000,debug=True)

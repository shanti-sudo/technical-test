import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/gene-suggest')
def gene_suggest():
  try:
    query = request.args.get('query')
    species = request.args.get('species')
    limit = request.args.get('limit')
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    statement = "SELECT display_label, species FROM gene_autocomplete where display_label like %(label)s and species like %(species)s"
    params = {'label':query+'%','species':species+'%'}
    cursor.execute(statement,params)
    empRows = cursor.fetchall()
    respone = jsonify(empRows)
    respone.status_code = 200
    return respone
  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone

if __name__ == "__main__":
    app.run()
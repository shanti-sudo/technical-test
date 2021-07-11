
import pymysql
from app import app
from config import mysql
from flask import (
  abort,
  json,
  jsonify,
  render_template,
  Response,
  request,
)
from werkzeug.exceptions import HTTPException

@app.route('/')
def form():
  return render_template('explore-api.html')

@app.route('/gene-suggest',methods=['GET'])
def gene_suggest():
  query = request.args.get('query',type=str)
  species = request.args.get('species',type=str)
  cap = request.args.get('max',type=int)
  if (query or species or cap) is None:
    abort(404)
  if (cap < 1 or query.isalnum()==False or species.isalnum()==False):
    abort(400)
  try:
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    statement = "SELECT display_label, species FROM gene_autocomplete where display_label like %(label)s and species like %(species)s limit %(limit)s"
    params = {'label':query+'%','species':species+'%','limit':cap}
    cursor.execute(statement,params)
    gRows = cursor.fetchall()
    respone = jsonify(gRows)
    respone.status_code = 200
    return respone
  except Exception as e:
    print(e)
  finally:
    cursor.close()
    conn.close()

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

if __name__ == "__main__":
    app.run()
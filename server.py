from flask import Flask, request, abort, jsonify
from flask_cors import CORS
import mysql.connector
import redis
import json

app = Flask(__name__)
CORS(app)

mydb = mysql.connector.connect(
  host="insert_db_host",
  user="insert_db_user",
  password="insert_db_password",
  database="insert_db_name"
)

redisObject = redis.Redis(host='insert_caching_host', port=6379, db=0)

cursor = mydb.cursor()

@app.route("/search", methods=['get'])
def search():
  # 1. get query parameter from web call
  query_string = request.args.get('q')

  # try to get wording in caching
  search_from_cache = redisObject.get(query_string)

  # check in caching
  if search_from_cache is not None: 
    # if already in caching
    result = json.loads(search_from_cache)
  else:
    # if not found in caching

    # query from db with search string
    sql = '''SELECT * FROM tweet WHERE tweet like '%{}%' '''.format(query_string)
    cursor.execute(sql)
    result_query = cursor.fetchall()

    # clear caching
    redisObject.flushdb()

    # set new records query to caching
    redisObject.set(query_string, json.dumps(result_query))
    result = result_query

  # return type json to web
  return jsonify(result = result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5001)

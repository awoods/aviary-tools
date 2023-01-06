import requests
import os
import uuid
import argparse
from uuid import uuid4
from dotenv import load_dotenv


CHUNK_SIZE = 1000000
load_dotenv()

def read_in_chunks(file_object, CHUNK_SIZE):
  while True:
    data = file_object.read(CHUNK_SIZE)
    if not data:
      break
    yield data


def upload(file, rsrc_id, url):
  content_name = str(file)
  content_path = os.path.abspath(file)
  content_size = os.stat(content_path).st_size

  print(content_name, content_path, content_size)

  f = open(content_path, "rb")

  index = 0
  offset = 0
  headers = {}

  for chunk in read_in_chunks(f, CHUNK_SIZE):
    offset = index + len(chunk)
    headers['Content-Range'] = 'bytes %s-%s/%s' % (index, offset -1, content_size)
    headers['access-token'] = os.getenv('access-token')
    headers['client'] = os.getenv('client')
    headers['uid'] = os.getenv('uid')
    index = offset

    try:
      params = {"collection_resource_id": rsrc_id ,"access": "true","filename": content_name ,"is_360": "false", "title": str(index)}
      files = {"media_file": chunk}
      r = requests.post(url=url, files=files,params=params, headers=headers)
      print(r.json())
      print("r: %s, Content-Range: %s" % (r, headers['Content-Range']))
    except Exception as e:
      print(e)


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-f', '--filename', required = True, help = 'Name of file to upload from current dir')
ap.add_argument('-r', '--resource_id', required = True, help = 'Aviary media resource ID')
args = vars(ap.parse_args())

# Load the files and convert them to images
file    = args['filename']
rsrc_id = args['resource_id']


upload(file, rsrc_id, "https://hlavmass.lib.harvard.edu/api/v1/media_files")

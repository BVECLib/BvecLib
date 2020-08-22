from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from flask import abort
import mimetypes
import os

gauth = GoogleAuth()

gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

def up(filename, fid):
  mime = mimetypes.MimeTypes().guess_type(filename)[0]
  file1 = drive.CreateFile({"mimeType": mime, "parents": [{"kind": "drive#fileLink", "id": fid}]})
  file1.SetContentFile(filename)
  file1.Upload() # Upload the file.
  os.remove(filename)
  print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))


def folder(fid):
  f = drive.ListFile({"q": "'" + fid + "' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
  fol = dict()
  i = 1
  for folder in f:
    fol[i] = {}
    fol[i]['title'] = folder['title']
    fol[i]['id'] = folder['id']
    i+=1

  if fol == None:
    abort(200)
  else:
    return fol
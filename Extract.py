from zipfile import ZipFile
file_name = "/content/drive/MyDrive/GPE/gpe.zip"
to_path = "/content/drive/MyDrive/GPE/"
with ZipFile(file_name, 'r') as zip:
  zip.extractall(to_path)
  print('Done')

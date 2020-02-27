import pandas as pd
import urllib
import tempfile
import shutil
import zipfile
import urllib.request

temp_dir = tempfile.mkdtemp()
data_source = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip'
zipname = temp_dir + '/Bike-Sharing-Dataset.zip'
urllib.urlretrieve(data_source, zipname)

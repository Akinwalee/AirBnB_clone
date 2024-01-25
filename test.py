#!/usr/bin/env python3
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

fs = FileStorage()
file_path = "file.json"
try:
    file_path = FileStorage._FileStorage__file_path
except:
    pass
try:
    os.remove(file_path)
except:
    pass
try:
    fs._FileStorage__objects.clear()
except:
    pass
ids = []

# First create
for i in range(2):
    bm = BaseModel()
    bm.updated_at = datetime.utcnow()
    fs.new(bm)
    ids.append(bm.id)

try:
    os.remove(file_path)
except:
    pass
fs.save()
try:
    fs._FileStorage__objects.clear()
except:
    pass
fs.reload()

all_reloaded = fs.all()

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload 1")

for id in ids:
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 1 {}".format(id))

from models import storage
storage.reload()

# Second create
for i in range(2):
    bm = BaseModel()
    bm.save()
    ids.append(bm.id)
try:
    os.remove(file_path)
except:
    pass
print("all before save")
print(storage.all())
storage.save()
print("all after save")
print(storage.all())
try:
    fs._FileStorage__objects.clear()
except:
    pass
storage.reload()
print("all after reload")
print(storage.all())

all_reloaded2 = storage.all()
print("All ids is: ")
print(ids)

if len(all_reloaded2.keys()) != len(ids):
    print("Missing after reload 2")

for id in ids:
    if all_reloaded2.get(id) is None and all_reloaded2.get("{}.{}".format("BaseModel", id)) is None:
        print("Missing 2 {}".format(id))

try:
    os.remove(file_path)
except Exception as e:
    pass

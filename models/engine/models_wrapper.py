from ..base_model import BaseModel
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State
from ..user import User

def to_model(objs_dict):
    objects = {}
    for key, value in objs_dict.items():
        if value["__class__"] == "BaseModel":
            model = BaseModel(value)
        elif value["__class__"] == "User":
            model = User(value)
        elif value["__class__"] == "State":
            model = State(value)
        elif value["__class__"] == "City":
            model = City(value)
        elif value["__class__"] == "Amenity":
            model = Amenity(value)
        elif value["__class__"] == "Place":
            model = Place(value)
        else:
            model = Review(value)
        objects.update({key: model})
    return (objects)
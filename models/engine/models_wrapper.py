# models_wrapper.py


from ..base_model import BaseModel
from ..user import User
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..place import Place
from ..review import Review

def to_model(objs_dict):
    objects = {}

    for key, value in objs_dict.items():
        class_name = value["__class__"]

        # Use the imported classes directly
        if class_name == "BaseModel":
            model = BaseModel(value)
        elif class_name == "User":
            model = User(value)
        elif class_name == "State":
            model = State(value)
        elif class_name == "City":
            model = City(value)
        elif class_name == "Amenity":
            model = Amenity(value)
        elif class_name == "Place":
            model = Place(value)
        elif class_name == "Review":
            model = Review(value)
        objects[key] = model

    return objects

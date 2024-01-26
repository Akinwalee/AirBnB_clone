# models_wrapper.py


def to_model(objs_dict):
    objects = {}

    for key, value in objs_dict.items():
        class_name = value["__class__"]

        # Lazy loading: import the class only when needed
        # if class_name == "BaseModel":
        #     from ..base_model import BaseModel
        #     model = BaseModel(value)
        # elif class_name == "User":
        #     from ..user import User
        #     model = User(value)
        # elif class_name == "State":
        #     from ..state import State
        #     model = State(value)
        # elif class_name == "City":
        #     from ..city import City
        #     model = City(value)
        # elif class_name == "Amenity":
        #     from ..amenity import Amenity
        #     model = Amenity(value)
        # elif class_name == "Place":
        #     from ..place import Place
        #     model = Place(value)
        # elif class_name == "Review":
        #     from ..review import Review
        #     model = Review(value)
        # objects[key] = model

        print("key: {}\n obj: {}".format(key, value))

    return (objects)


def to_model(objs_dict):
    objects = {}
    for key, value in objs_dict.items():
        class_name = value["__class__"]

        # Lazy loading: import the class only when needed
        if model_class_name == "BaseModel":
            from ..base_model import BaseModel
            model_class = BaseModel
        elif model_class_name == "User":
            from ..user import User
            model_class = User
        elif model_class_name == "State":
            from ..state import State
            model_class = State
        elif model_class_name == "City":
            from ..city import City
            model_class = City
        elif model_class_name == "Amenity":
            from ..amenity import Amenity
            model_class = Amenity
        elif model_class_name == "Place":
            from ..place import Place
            model_class = Place
        elif model_class_name == "Review":
            from ..review import Review
            model_class = Review

        model = model_class(value)
        objects[key] = model

    return objects


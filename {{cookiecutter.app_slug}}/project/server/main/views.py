# project/server/main/views.py
from flask import render_template, Blueprint
from flask import jsonify,request
from project.server.pickle_builder import DataScienceModelsPersistor


models_persistor=DataScienceModelsPersistor()
main_blueprint = Blueprint("main", __name__)



@main_blueprint.route("/")
def home():
    return render_template("main/home.html")


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")


@main_blueprint.route("/models/")
def get_models():
    payload={'commit':models_persistor.commit, 'creation_date':models_persistor.creation_date}
    for model_name, model in models_persistor.models.items():
        payload.update({model_name:model.meta})

    return jsonify(payload)


@main_blueprint.route("/models/<model_name>")
def get_model(model_name):

    payload={model_name:models_persistor.models.get(model_name).meta}

    return jsonify(payload)


@main_blueprint.route("/models/<model_name>/data")
def get_data_interface(model_name):

    model=models_persistor.models.get(model_name)
    data_interface=model.data_interface.astype('str')
    return jsonify(data_interface.to_dict())


@main_blueprint.route("/models/<model_name>/predict")
def get_prediction(model_name):
    req_data = request.get_json()

    model=models_persistor.models.get(model_name)


    return jsonify(model.payload_predict(req_data))
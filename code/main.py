import data_preparation 
import build_model as build
import model_inspection as inspection
import predictions

if __name__ == "__main__":
    num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()
    model = build.build_model(num_classes, input_shape)
    build.train_model(x_train, y_train, model)
    inspection.save_model(model)
    loaded_model = inspection.load_model()
    inspection.evaluate_loaded_model(x_test, y_test, loaded_model)
    predictions.predict_on_data(x_test, y_test, loaded_model)
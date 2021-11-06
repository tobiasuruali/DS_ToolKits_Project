import data_preparation 
import build_model as build
import model_inspection as inspection

if __name__ == "__main__":
    num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()
    model = build.build_model(num_classes, input_shape)
    build.train_model(x_train, y_train, model)
    inspection.evaluate_model(x_test, y_test, model)
    inspection.save_model(model)
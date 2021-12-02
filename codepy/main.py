import data_preparation 
import build_model as build
import model_inspection as inspection
import predictions
import database_pg

if __name__ == "__main__":
    data_preparation.initialize_wandb()
    num_classes, input_shape, x_train, y_train, x_test, y_test = data_preparation.prepare_data()
    #Comment form here..
    model = build.build_model(num_classes, input_shape)
    build.train_model(x_train, y_train, x_test, y_test, model)
    inspection.save_model(model)
    #..To here for testing purposes 
    loaded_model = inspection.load_model()
    inspection.evaluate_loaded_model(x_test, y_test, loaded_model)
    # predictions.predict_on_data(x_test, y_test, loaded_model)
    database_pg.create_milestone3_db()
    database_pg.create_input_pred_db()
    random_img_x, squeezed_random_img_x, img_from_db = database_pg.insert_load_random_image()
    database_pg.predict_and_persist(img_from_db, loaded_model)

    
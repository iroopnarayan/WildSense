from data_processing import load_data
from model import build_model, train_model
from utils import load_best_model, predict_image, detect_live

if __name__ == "__main__":
    data_dir = 'E:\\MCA\\3 SEM\\WildSense\\data'
    
    try:
        train_gen, val_gen = load_data(data_dir)
        print("Data loaded successfully.")
        
        model = build_model()
        train_model(model, train_gen, val_gen)
        
        # Load the best model for predictions
        model = load_best_model('models/best_model.keras')
        
        # Uncomment below to predict from an image
        print(predict_image(model, 'E:\\MCA\\3 SEM\\WildSense\\data\\image1.jpg'))

        # Uncomment below to detect from live camera feed
        # detect_live(model)

    except Exception as e:
        print(f"An error occurred: {e}")










# from data_processing import load_data
# from model import build_model, train_model
# from utils import load_best_model, predict_image, detect_live

# from keras.callbacks import ModelCheckpoint

# model_checkpoint = ModelCheckpoint('models/best_model.keras', save_best_only=True)

# if __name__ == "__main__":
#     # data_dir = 'E:\\MCA\\3 SEM\\WildSense\\data\1.jpg'  # Path to your dataset
#     data_dir = 'E:\\MCA\\3 SEM\\WildSense\\data'
#     train_gen, val_gen = load_data(data_dir)
    
#     model = build_model()
#     train_model(model, train_gen, val_gen)

#     # Load the best model for predictions
#     model = load_best_model('models/best_model.h5')

#     # Uncomment below to predict from an image
#     print(predict_image(model, 'E:\\MCA\\3 SEM\\WildSense\\data\\1.jpg'))

#     # Uncomment below to detect from live camera feed
#     detect_live(model)




# # from data_processing import load_data
# # from model import build_model, train_model
# # from utils import load_best_model, predict_image, detect_live
# # import os
# # os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 

# # if __name__ == "__main__":
# #     # Define the path to your dataset
# #     data_dir = r'E:\MCA\3 SEM\WildSense\data'  # Use raw string for Windows paths

# #     # Load training and validation data
# #     try:
# #         train_gen, val_gen = load_data(data_dir)
# #         print("Data loaded successfully.")
# #     except Exception as e:
# #         print(f"Error loading data: {e}")
# #         exit(1)  # Exit if data loading fails

# #     # Build and train the model
# #     try:
# #         model = build_model()
# #         print("Model built successfully.")
# #         train_model(model, train_gen, val_gen)
# #         print("Model trained successfully.")
# #     except Exception as e:
# #         print(f"Error during model training: {e}")
# #         exit(1)  # Exit if training fails

# #     # Load the best model for predictions
# #     try:
# #         model_path = 'models/best_model.h5'
# #         if os.path.exists(model_path):
# #             model = load_best_model(model_path)
# #             print("Best model loaded successfully.")
# #         else:
# #             print(f"Model file not found: {model_path}")
# #             exit(1)  # Exit if model file does not exist
# #     except Exception as e:
# #         print(f"Error loading best model: {e}")
# #         exit(1)  # Exit if loading fails

# #     # Uncomment below to predict from an image
# #     # try:
# #     #     image_path = 'data/1.jpg'  # Use raw string for Windows paths
# #     #     prediction = predict_image(model, image_path)
# #     #     print(f"Prediction for image {image_path}: {prediction}")
# #     # except Exception as e:
# #     #     print(f"Error predicting image: {e}")

# #     # Uncomment below to detect from live camera feed
# #     try:
# #         detect_live(model)
# #     except Exception as e:
# #         print(f"Error detecting live feed: {e}")
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense # type: ignore
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(5, activation='softmax')  # Update this based on your actual class count
    ])
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def train_model(model, train_generator, validation_generator):
    early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
    model_checkpoint = ModelCheckpoint('models/best_model.keras', save_best_only=True)
    
    model.fit(
        train_generator,
        validation_data=validation_generator,
        epochs=50,
        callbacks=[early_stopping, model_checkpoint]
    )











# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# # def build_model():
# #     model = Sequential([
# #         Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
# #         MaxPooling2D(pool_size=(2, 2)),
# #         Conv2D(64, (3, 3), activation='relu'),
# #         MaxPooling2D(pool_size=(2, 2)),
# #         Flatten(),
# #         Dense(128, activation='relu'),
# #         Dense(5, activation='softmax')  # Adjust output size based on your classes
# #     ])
# #     model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# #     return model

# def build_model():
#     model = Sequential([
#         Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
#         MaxPooling2D(pool_size=(2, 2)),
#         Conv2D(64, (3, 3), activation='relu'),
#         MaxPooling2D(pool_size=(2, 2)),
#         Flatten(),
#         Dense(128, activation='relu'),
#         Dense(2, activation='softmax')  # Update this line to match the number of classes
#     ])
#     model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#     return model

# # def train_model(model, train_generator, validation_generator):
# #     early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
# #     model_checkpoint = ModelCheckpoint('models/best_model.h5', save_best_only=True)

# #     model.fit(
# #         train_generator,
# #         validation_data=validation_generator,
# #         epochs=50,
# #         callbacks=[early_stopping, model_checkpoint]
# #     )


# def train_model(model, train_generator, validation_generator):
#     early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
#     model_checkpoint = ModelCheckpoint('models/best_model.keras', save_best_only=True)

#     model.fit(
#         train_generator,
#         validation_data=validation_generator,
#         epochs=50,
#         callbacks=[early_stopping, model_checkpoint]
#     )
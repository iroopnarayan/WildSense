import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_data(data_directory):
    datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest',
        validation_split=0.2  # Ensure this is set for splitting data
    )

    train_generator = datagen.flow_from_directory(
        data_directory,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        subset='training'  # For training data
    )

    validation_generator = datagen.flow_from_directory(
        data_directory,
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical',
        subset='validation'  # For validation data
    )

    return train_generator, validation_generator

# import numpy as np
# from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore

# def load_data(data_directory):
#     datagen = ImageDataGenerator(
#         rescale=1./255,
#         rotation_range=20,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest',
#         validation_split=0.2
#     )

#     train_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='training'
#     )

#     validation_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='validation'
#     )

#     return train_generator, validation_generator

# import numpy as np
# from tensorflow.keras.preprocessing.image
# import ImageDataGenerator
# def load_data(data_directory):
#     datagen = ImageDataGenerator(
#         rescale=1./255,
#         rotation_range=20,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest',
#         validation_split=0.2
#     )

#     train_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='training'
#     )

#     validation_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='validation'
#     )

#     return train_generator, validation_generator

# import numpy as np
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# def load_data(data_directory):
#     datagen = ImageDataGenerator(
#         rescale=1./255,
#         rotation_range=20,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest',
#         validation_split=0.2
#     )

#     train_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='training'
#     )

#     validation_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='validation'
#     )

#     return train_generator, validation_generator




# import numpy as np
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

# def load_data(data_directory, encoding='utf-8'):
#     datagen = ImageDataGenerator(
#         rescale=1./255,
#         rotation_range=20,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest',
#         validation_split=0.2
#     )

#     train_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='training',
#         encoding=encoding
#     )

#     validation_generator = datagen.flow_from_directory(
#         data_directory,
#         target_size=(64, 64),
#         batch_size=32,
#         class_mode='categorical',
#         subset='validation',
#         encoding=encoding
#     )

#     return train_generator, validation_generator
















# # import numpy as np
# # from tensorflow.keras.preprocessing.image import ImageDataGenerator

# # # def load_data(data_directory):
# # #     datagen = ImageDataGenerator(
# # #         rescale=1./255,
# # #         rotation_range=20,
# # #         width_shift_range=0.2,
# # #         height_shift_range=0.2,
# # #         shear_range=0.2,
# # #         zoom_range=0.2,
# # #         horizontal_flip=True,
# # #         fill_mode='nearest',
# # #         validation_split=0.2
# # #     )

# # #     train_generator = datagen.flow_from_directory(
# # #         data_directory,
# # #         target_size=(64, 64),
# # #         batch_size=32,
# # #         class_mode='categorical',
# # #         subset='training'
# # #     )

# # #     validation_generator = datagen.flow_from_directory(
# # #         data_directory,
# # #         target_size=(64, 64),
# # #         batch_size=32,
# # #         class_mode='categorical',
# # #         subset='validation'
# # #     )

# # #     return train_generator, validation_generator




# # def load_data(data_directory, encoding='utf-8'):
# #        datagen = ImageDataGenerator(
# #            rescale=1./255,
# #            rotation_range=20,
# #            width_shift_range=0.2,
# #            height_shift_range=0.2,
# #            shear_range=0.2,
# #            zoom_range=0.2,
# #            horizontal_flip=True,
# #            fill_mode='nearest',
# #            validation_split=0.2
# #        )

# #        train_generator = datagen.flow_from_directory(
# #            data_directory,
# #            target_size=(64, 64),
# #            batch_size=32,
# #            class_mode='categorical',
# #            subset='training',
# #            encoding=encoding
# #        )

# #        validation_generator = datagen.flow_from_directory(
# #            data_directory,
# #            target_size=(64, 64),
# #            batch_size=32,
# #            class_mode='categorical',
# #            subset='validation',
# #            encoding=encoding
# #        )

# #        return train_generator, validation_generator
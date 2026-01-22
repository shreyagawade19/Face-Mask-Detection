import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix

# Paths
MODEL_PATH = "mask_detector.model"
DATASET_PATH = "dataset"

# Image parameters (must match training)
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# Load model
print("[INFO] Loading model...")
model = load_model(MODEL_PATH)

# Data generator
datagen = ImageDataGenerator(rescale=1.0/255)

test_generator = datagen.flow_from_directory(
    DATASET_PATH,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical",
    shuffle=False
)

# Predictions
print("[INFO] Evaluating model...")
predictions = model.predict(test_generator)
y_pred = np.argmax(predictions, axis=1)
y_true = test_generator.classes

# Results
print("\nClassification Report:")
print(classification_report(y_true, y_pred, target_names=test_generator.class_indices))

print("\nConfusion Matrix:")
print(confusion_matrix(y_true, y_pred))

# Accuracy
accuracy = np.mean(y_pred == y_true)
print(f"\nOverall Accuracy: {accuracy * 100:.2f}%")

import os
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image
import matplotlib.pyplot as plt
from ela_utils.ela_converter import convert_to_ela_image
from models.cnn_model import build_model
from tensorflow.keras.models import load_model

# Load and preprocess images
def load_images(dataset_path):
    images, labels = [], []
    for label, category in enumerate(['authentic', 'tampered']):
        folder = os.path.join(dataset_path, category)
        for filename in os.listdir(folder):
            path = os.path.join(folder, filename)
            ela_image = convert_to_ela_image(path)
            ela_image = ela_image.resize((128, 128))
            images.append(np.array(ela_image) / 255.0)
            labels.append(label)
    return np.array(images), np.array(labels)

print("Loading images...")
X, y = load_images('dataset')
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)

# Train model
print("Building model...")
model = build_model()
history = model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10)

# Save model
model.save('saved_models/cnn_ela_model.h5')

# Plot accuracy
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.legend()
plt.savefig('results/training_plot.png')
plt.show()

import os

# Ensure the setup script is executable
os.system("chmod +x setup/install_dependencies.sh")

# Run the setup script
os.system("bash setup/install_dependencies.sh")

# Import and run the training script
from training.train import train_model

if __name__ == "__main__":
    train_model()

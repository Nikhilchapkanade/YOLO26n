from ultralytics import YOLO

def main():
    # 1. Load the YOLO26 model (nano version for speed)
    # This will automatically download 'yolo26n.pt' if you don't have it
    model = YOLO('yolo26n.pt') 

    print("Downloading VisDrone dataset and starting training...")
    print("Note: This dataset is large (~6GB). Ensure you have good WiFi.")

    # 2. Train using the built-in 'VisDrone.yaml' configuration
    # The 'data' argument automatically finds, downloads, and unzips the VisDrone data
    results = model.train(
        data='VisDrone.yaml',  # Magic keyword that triggers auto-download
        epochs=10,             # Keep it low for a first test run
        imgsz=640,
        batch=16,
        device='cpu',            
        project='runs/train',  # Where to save results
        name='yolo26_visdrone' # Name of this specific run
    )

    print("Training Complete! Best model saved in runs/train/yolo26_visdrone/weights/best.pt")

if __name__ == '__main__':
    main()
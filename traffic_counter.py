import cv2
from ultralytics import YOLO
from collections import defaultdict

def main():
    # --- CONFIGURATION ---
    path_to_video = r"C:\Users\nikhi\Downloads\Infinite_Car_Running_Video_Generation.mp4"
    path_to_model = "models/best.pt"
    # ---------------------

    # 1. Load Model
    model = YOLO(path_to_model)
    
    # 2. Open Video
    cap = cv2.VideoCapture(path_to_video)
    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

    # 3. Define Counting Line (Horizontal line at 50% height)
    line_y = h // 2
    
    # Store track history to detect crossing
    track_history = defaultdict(lambda: [])
    # Sets to keep track of counted IDs (so we don't double count)
    crossed_ids = set()

    # Create a video writer to save the output (Optional)
    # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    # out = cv2.VideoWriter('output.mp4', fourcc, fps, (w, h))

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        # 4. Run YOLO26 Tracking
        # persist=True is crucial for keeping ID same across frames
        results = model.track(frame, persist=True, show=False, verbose=False)

        if results[0].boxes.id is not None:
            # Get the boxes and track IDs
            boxes = results[0].boxes.xywh.cpu()
            track_ids = results[0].boxes.id.int().cpu().tolist()
            class_ids = results[0].boxes.cls.int().cpu().tolist()

            # Visualize the Line
            cv2.line(frame, (0, line_y), (w, line_y), (0, 255, 0), 2)
            cv2.putText(frame, "Counting Line", (10, line_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Loop through detected objects
            for box, track_id, class_id in zip(boxes, track_ids, class_ids):
                x, y, w_box, h_box = box
                
                # Append current position to history
                track = track_history[track_id]
                track.append((float(x), float(y))) 
                
                # Keep history short (last 30 frames) to save memory
                if len(track) > 30: 
                    track.pop(0)

                # --- COUNTING LOGIC ---
                # Check if object has moved across the line
                # We look at the previous position (track[-2]) and current (track[-1])
                if len(track) > 2:
                    prev_y = track[-2][1]
                    curr_y = track[-1][1]

                    # If it crossed from Above to Below (or vice versa)
                    if track_id not in crossed_ids:
                        if (prev_y < line_y and curr_y >= line_y) or (prev_y > line_y and curr_y <= line_y):
                            crossed_ids.add(track_id)
                            # Optional: Draw a red flash line to show detection
                            cv2.line(frame, (0, line_y), (w, line_y), (0, 0, 255), 3)

                # Draw Bounding Box & ID
                cv2.rectangle(frame, (int(x - w_box/2), int(y - h_box/2)), (int(x + w_box/2), int(y + h_box/2)), (255, 0, 0), 2)
                cv2.putText(frame, f"ID: {track_id}", (int(x - w_box/2), int(y - h_box/2 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # 5. Display Count
        count_text = f"Total Vehicles: {len(crossed_ids)}"
        cv2.putText(frame, count_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Show Result
        cv2.imshow("YOLO26 Advanced Counter", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
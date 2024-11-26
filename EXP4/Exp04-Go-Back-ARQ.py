import time
import random

# Main logic for Go-Back-N protocol
window_size = 4
total_frames = 10
current_frame = 0  # Tracks the next frame to send

while current_frame < total_frames:
    # Send frames within the window
    for i in range(window_size):
        if current_frame + i < total_frames:
            print(f"Sending frame {current_frame + i}")
        time.sleep(0.5)

    # Simulate ACKs for frames in the window
    for i in range(window_size):
        if current_frame < total_frames:
            ack = random.choice([True, False])  # Randomly simulate ACK success/failure
            if ack:
                print(f"ACK received for frame {current_frame}")
                current_frame += 1
            else:
                print(f"Frame {current_frame} lost, resending from this frame")
                break  # Stop processing and resend from the current frame
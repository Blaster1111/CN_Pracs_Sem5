import random
import time

window_size = int(input("Number of frames that can be sent before needing an ACK: "))
total_frames = int(input("Total number of frames to send: "))
timeout = int(input("Timeout in seconds: "))

successful_transmissions = set()  # Track successfully transmitted frames

def send_frame(frame_number):
    print(f"Sending frame {frame_number}")
    success = random.choice([True, False])  # Randomly decide if the frame is successfully sent
    if success:
        successful_transmissions.add(frame_number)
    return success

def receive_ack(expected_frame):
    time.sleep(1)  # Simulate delay
    # Randomly decide if we receive an ACK, even if the frame was successfully sent
    if random.choice([True, False]):
        if expected_frame in successful_transmissions:
            return expected_frame  # Return the expected frame as ACK if it was successfully sent
        return None  # Simulate no ACK for frames that weren't transmitted
    return None  # Simulate ACK loss or timeout

def go_back_n_arq():
    base = 0  # Tracks the oldest unacknowledged frame
    next_frame_to_send = 0  # Next frame to send

    while base < total_frames:
        # Send frames within the window
        while next_frame_to_send < base + window_size and next_frame_to_send < total_frames:
            if send_frame(next_frame_to_send):
                print(f"Frame {next_frame_to_send} sent successfully.")
            else:
                print(f"Frame {next_frame_to_send} lost.")
            next_frame_to_send += 1

        # Simulate receiving ACKs
        ack = receive_ack(base)
        if ack is not None:
            print(f"Received ACK for frame {ack}")
            base = ack + 1  # Move the base forward
        else:
            print("ACK lost or timeout occurred, resending from base frame")
            next_frame_to_send = base  # Reset next frame to send

if __name__ == "__main__":
    go_back_n_arq()

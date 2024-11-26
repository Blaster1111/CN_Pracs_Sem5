import random
import time

window_size = int(input("Number of frames that can be sent before needing an ACK: "))
total_frames = int(input("Total number of frames to send: "))
timeout = int(input("Timeout in seconds: "))

def send_frame(frame_number):
    print(f"Sending frame {frame_number}")
    return random.choice([True, False])  # Simulate whether frame is sent successfully

def receive_ack(expected_frame):
    time.sleep(1)  # Simulate a delay in receiving ACK
    if random.choice([True, False]):
        return expected_frame  # Simulate receiving an ACK
    else:
        return None  # Simulate no ACK received (ACK lost)

def selective_repeat_arq():
    base = 0  # Tracks the oldest unacknowledged frame
    next_frame_to_send = 0  # Next frame to send
    ack_received = [-1] * total_frames  # Array to track which frames have been acknowledged

    while base < total_frames:
        # Send frames within the window
        while next_frame_to_send < base + window_size and next_frame_to_send < total_frames:
            if send_frame(next_frame_to_send):
                print(f"Frame {next_frame_to_send} sent successfully.")
            else:
                print(f"Frame {next_frame_to_send} lost.")
            next_frame_to_send += 1
        
        # Attempt to receive ACKs for frames in the window
        for i in range(base, min(base + window_size, total_frames)):
            if ack_received[i] == -1:  # If the frame hasn't been acknowledged yet
                ack = receive_ack(i)
                if ack is not None:
                    print(f"Received ACK for frame {ack}")
                    ack_received[ack] = 1  # Mark this frame as acknowledged
                else:
                    print(f"ACK lost or timeout occurred for frame {i}, resending it")
                    send_frame(i)  # Resend the frame that didn't receive an ACK
        
        # Move base forward when ACK for base frame is received
        while base < total_frames and ack_received[base] == 1:
            base += 1

if __name__ == "__main__":
    selective_repeat_arq()

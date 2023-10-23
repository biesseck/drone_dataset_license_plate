import cv2
import os, sys
import argparse

def extract_frames(video_path):
    # Get the video file name without the extension
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = f"frames_{video_name}"
    path_output_folder = os.path.join(os.path.dirname(video_path), output_folder)

    # Create the output folder if it doesn't exist
    if not os.path.exists(path_output_folder):
        os.mkdir(path_output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frame_count = 0

    # Read and save each frame as a PNG image
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Save the frame as a PNG image
        frame_filename = os.path.join(path_output_folder, f"frame_{frame_count:04d}.png")
        print(f'Saving frame {frame_count} at \'{path_output_folder}\'', end='\r')
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"{frame_count} frames extracted and saved to {output_folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from a video and save as PNG images.")
    parser.add_argument("-input", required=True, help="Path to the input video file")
    args = parser.parse_args()

    video_path = args.input
    extract_frames(video_path)

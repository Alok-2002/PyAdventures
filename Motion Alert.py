import cv2
import time
import winsound
import os

# Get the path to the user's "Documents" directory
output_directory = os.path.join(os.path.expanduser('~'), 'Documents')

cap = cv2.VideoCapture(0)

prev_frame = None

alarm_duration = 2
alarm_frequency = 2500
alarm_duration_ms = 1000

output_file_path = os.path.join(output_directory, 'motion_detection_output.mp4')
output_file = cv2.VideoWriter(output_file_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (640, 480))

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if prev_frame is None:
        prev_frame = gray
        continue

    frame_diff = cv2.absdiff(prev_frame, gray)

    thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        winsound.Beep(alarm_frequency, alarm_duration_ms)

        time.sleep(alarm_duration)

    output_file.write(frame)

    cv2.imshow('Motion Alert', frame)

    prev_frame = gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
output_file.release()

cv2.destroyAllWindows()

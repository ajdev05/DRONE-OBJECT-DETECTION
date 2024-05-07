# Drone Object Detection
 
This project aims to perform object detection on live video footage captured by the Tello drone using computer vision techniques. It leverages the power of OpenCV and a pre-trained YOLO object detection model.
   
## Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
 
To run this project, you need to have Python 3 and PIP installed on your system. Additionally, ensure you have the Tello drone and a compatible device for communication (e.g., laptop, smartphone).

### Installing

You can install the project locally using Git and pip. Follow the steps below:

1. Clone the repository to your local machine:
 
```bash
git clone https://github.com/ajdev05/DRONE-OBJECT-DETECTION.git
```

2. Navigate to the project directory:

```bash
cd DRONE-OBJECT-DETECTION
```

3. Install and activate virtual environment:

```bash
pip install virtualenv
virtualenv env
source env/bin/activate 
```

4. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### Connecting to the drone

Turn on the drone and connect to it using WiFi. To control the drone manually download the "Tello" app on your mobile device.


5. When everything is connected, run:

```bash
python3 main.py
```


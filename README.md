# Facial Recognition Office Door

A facial recognition system that grants access to an office door when the person is authorized to enter.

How it works:
1) Person stands infront of camera
2) If person is granted access: Relay triggered to open office door, LCD screen welcomes the person
   If not denied access: Relay does not trigger, system continues to determine if the person is authorized
   
Steps to get the system up and running:
1) Take images of the person whose identity is to be trained by running "datagathering.py"
2) Train the system with the images taken with "trainer.py"
3) Start the facial recognition system with "recognizer.py"

HardWare:
- Raspberry Pi 3 Model B+
- Raspberry Pi Camera Module
- HD44780 I2C LCD (16×02 Character)
- Relay

Takeaway:
- Using FileZilla as SSH for FTP with Raspberry Pi
- SSH into Raspberry Pi and working remotely through MACOS terminal
- Terminal commands
- Python programming language
- Integrating OpenCV Library
- Introduction to Object Detection
- Steps involved in machine learning
- How a relay works
- Running Python files through ShellScript on boot



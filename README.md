# Harrypotter
It's an invisible cloak that harry used several times to not get noticed while he was exploring Hogwarts with his mates. 

- Invisibility Cloak using OpenCV -
This Python project uses the magic of computer vision with OpenCV to create a real-time invisibility effect! It detects a specific colored cloth in the video feed and replaces it with a static background image, making the person under the cloth appear invisible.

- Features - 
Real-time video processing to create a seamless invisibility illusion.
User-friendly color selection menu at the start to choose your cloak's color.
Supports multiple colors: Red, Green, Blue, and Black are pre-configured.
Robust Color Detection using the HSV color space.
Noise Reduction using morphological transformations for a cleaner output.

- How It Works - 
The magic is achieved through a simple, yet effective, computer vision technique:
Background Capture: When the program starts, it first captures a few seconds of video to record a static background image of the scene without you or the cloak in it.
Color Detection (Masking): In the live video feed, the program converts the colors from the BGR space to the HSV (Hue, Saturation, Value) space. HSV is much better for detecting specific colors. It then creates a "mask" that isolates only the pixels matching the chosen cloak color of your choice.

- Image Segmentation: Using the mask, the program segments the live video into two parts:
The area covered by the invisibility cloak.
The rest of the scene (everything else).

The Magic!: The final step is to combine the images. The program takes the "cloak area" from the static background image and combines it with the "everything else" area from the live video feed. This creates the illusion that you can see right through the cloak to the background behind it!

- Requirements
Python 3.x
A webcam
  The following Python libraries:
    OpenCV
    NumPy

- How to Run
  Clone the repository:
  Bash
  git clone https://github.com/tusharisunique/Harrypotter.git
  cd Harrypotter
  Install the required libraries:
  Bash
  pip install opencv-python numpy
  Run the script:
  Bash
  python your_script_name.py
  
- Follow the on-screen instructions:
  * First, a color menu will appear. Type your chosen cloak color (red, green, blue, or black) into the terminal and press Enter.
  * The program will then capture the background. Move out of the camera's view for a few seconds.
  * Once the background is captured, a message will appear in the terminal. You can now step into the frame wearing your colored cloak!
  * To stop the program, press the 'q' key.

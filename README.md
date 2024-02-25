# Brickhack-X-Project

## Contributors:
- Ryan Lembo-Ehms
- Mark Luskiewicz
- Ethan Battaglia

## Notes
### Inspiration
We really wanted to do something that uses Computer Vision for our first hackathon!
### What it does
Simple! It takes your computer's camera, throws it onto a game screen, and lets you play pong with your hands! (more specifically, your index fingers)
### How we built it
We used Python to build our project. More specifically, we used OpenCV to get the camera input and transform & color it, then we used MediaPipe's machine learning solution for detecting hands in an image or video capture. To make it into a playable game, we brought the camera's output into a PyGame window and then drew the game's components on top of the display capture.
### Challenges we ran into
Firstly, it was difficult to install MediaPipe on our machines. It was also somewhat hard to find a good amount of documentation to successfully utilize MediaPipe's broad use cases, as we were previously completely unfamiliar with both OpenCV and MediaPipe. Lastly, finding out how to draw our desired shapes in PyGame and add collision to the ball took us a while.
### Accomplishments that we're proud of
We're really proud when our fingers directly caused each Paddle to move up and down! Another exciting point for us was successfully drawing out our entire PyGame interface and seeing everything work together for the final product!
### What we learned
A lot. We came in here expecting to learn, too! But we went through a lot of struggle, and in the end, we were able to brush up on our basic Python and PyGame syntax and learn the steps it takes to convert camera input to video output!
### What's next for CV Pong
We have plans of expanding our CV experience into more games. By utilizing this technology, we could even find a specific gesture that the player does with their hand to perform a specific function in ANY game, based on the gesture.

## Requirements to run
 - OpenCV library
 - MediaPipe library
 - Python ver 3.7 - 3.10

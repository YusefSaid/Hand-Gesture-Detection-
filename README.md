# ikt213 machine vision

The Hand Gesture Detection project was developed by a group of 5 individuals. We created two solutions during the project: the Mediapipe solution and the YOLOv4 solution. The Mediapipe solution is a versatile digital-based approach that allows for simple expansion. However, it can be challenging to apply to complex or multiple gestures. On the other hand, the YOLOv4 model was highly successful but requires retraining for each new gesture using a well-developed dataset.

Bellow is an illustration on how it turned out:
![image](https://github.com/YusefSaid/Hand-Gesture-Detection-/assets/77720622/f8de2da1-00e0-492c-8d9a-8e31241ba587)

To enhance the project's scalability, we planned to integrate our solution with robotic hands. We aimed to utilize Gazebo, a 3D simulator, to test our code on various robot models integrated with the ROS2 Operating system. Gazebo enabled us to simulate the behavior of a digital robotic hand in response to our hand gesture movements. Although we made progress in setting up the work environment and workspace, the full integration was not achieved due to time constraints, limited experience, and lack of assistance.

Below is a snapshot from Gazebo showcasing the robotic arm we intended to control by integrating our Hand Gesture Detection solutions. The robotic hand would imitate our hand movements based on recorded gestures:
![image](https://github.com/YusefSaid/Hand-Gesture-Detection-/assets/77720622/f330d962-ce4f-4093-be40-283bc3ac2ebb)

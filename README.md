# ros_dev_practice

[blanch] **feature/get-reduced-LaserScan-value**

## What I want to do.

### Subscribing the LIDAR's values

- I want to receive the /scan values of the LIDAR on turtlebot3(simulator).

### Making my original (cylindrical) world

- I want to make **the cylindrical wolrd** on gazebo.
  - The world is useful for checking the whole of the /scan values as shown in the below figures. 

> <img src="https://raw.githubusercontent.com/t-yokota/ros_dev_practice/feature/get-reduced-LaserScan-value/figures/fig1_cylindrical_world.png" width="300"> <img src="https://raw.githubusercontent.com/t-yokota/ros_dev_practice/feature/get-reduced-LaserScan-value/figures/fig2_scan_value.png" width="308">

### Publishing the down-sampled LIDAR's value

- I want to publish only **a part of the /scan values** of the LIDAR. 
  - Now, I want only sensor values obtained by scanning the forward of the robot.
  - It is not nessesary to use the all /scan values for avoiding the collision while the automatic running.

> <img src="https://raw.githubusercontent.com/t-yokota/ros_dev_practice/feature/get-reduced-LaserScan-value/figures/fig3_scan_value_front.png" width="308">
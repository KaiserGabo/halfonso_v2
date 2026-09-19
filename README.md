<!-- ## License

This project is licensed under MIT License.
For previous licensing history, see [LICENSE.previous.md](https://github.com/KaiserGabo/halfonso/blob/main/LICENSE.previous.md)

<br>

<div align="center">
	<img src="https://github.com/KaiserGabo/halfonso/blob/main/visual_demos/robot_visual.png" height="350">
	<br>
	<h2> Differential Drive Robot using ROS 2 Jazzy Jalisco </h2>
	<a href="https://github.com/KaiserGabo/halfonso/blob/main/LICENSE">
		<img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=blue&style=flat-square" height="20">
  	</a>
	<a href="https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview">
		<img src="https://img.shields.io/static/v1.svg?label=Ubuntu&message=24.04%20LTS&color=orange&style=flat-square" height="20">
  	</a>
	<a href="https://docs.ros.org/en/jazzy/index.html">
	    <img src="https://img.shields.io/static/v1.svg?label=ROS%202&message=Jazzy%20Jalisco&color=0059b3&style=flat-square" height="20">
  	</a>
	<br><br>		
</div>

Hi everyone! Today I would like to share my project implementing a fundamental differential drive robot using <ins>**ROS2 Jazzy Jalisco**</ins> and <ins>**Raspberry Pi 5**</ins>, with features including Gazebo simulation, ros2_control, teleoperation, SLAM, and Navigation2.

This project also represents my learning journey following tutorials from [Articulated Robotics](https://articulatedrobotics.xyz/):

- Forum: https://articulatedrobotics.xyz/tutorials/mobile-robot/project-overview/
- Forum beta (has update instructions for more recent versions of ROS 2 (Humble, Jazzy, etc)): https://beta.articulatedrobotics.xyz/tutorials/mobile-robot/project-overview/
- Tutorial playlist: https://youtube.com/playlist?list=PLunhqkrRNRhYAffV8JDiFOatQXuU-NnxT&si=1N9GNN6gRnet5heK

You can see the demo [here](https://github.com/KaiserGabo/halfonso/blob/main/README.md#demo)

<br> -->

## Getting Started

Before we start, make sure you are using [Ubuntu 24.04](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) and have [ROS 2 Jazzy Jalisco](https://docs.ros.org/en/jazzy/index.html) installed in your server machine (which is your desktop or laptop).

Make sure to install git:

    sudo apt install git ros-dev-tools -y

Make sure VScode is installed, it can be found in Ubuntu App Center. Some extensions that I have installed are listed below:

- C/C++ Extension Pack (Microsoft)
- Python (Microsoft)
- YAML (Red Hat)
- Remote - SSH (Microsoft)

<!-- Additionally, consider installing[tmux](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#terminator), which is a useful tool to use with ROS 2. -->

<br>

## Setting Up ROS 2 Workspace and Installed Required Packages

Before we start, see [ROS 2 Packages: A Brief Introduction](https://https://github.com/KaiserGabo/halfonso/blob/main/Package_Installation_Instruction.md#introduction) for the differences between the <ins>**binary installation**</ins> and <ins>**build from source**</ins>

### Creating a Workspace `ros_ws`

1.  Open a terminal using `ctrl + alt + t`, create a workspace named `ros_ws` with a folder named `src`:

        mkdir -p ~/ros_ws/src

    - Replace `ros_ws` with the name you want to put as your workspace name.

2.  Follow to the instructions at [**Install ROS 2 Packages**](https://https://github.com/KaiserGabo/halfonso/blob/main/Package_Installation_Instruction.md#install-ros-2-package) to install all the necessary packages.
<br>

<!-- ## Launch Simulation

1.  Once Everything is set, go to `your_workspace` and source the workspace:

        cd ros_ws/
        source install/setup.bash

    - When a new terminal is opened, ensure that terminal sourced the workspace also:

2.  Launch the simulation\*:

        ros2 launch halfonso sim.launch.py

    - This will launch the `robot description`, `gazebo`, `rviz2`, `ros2_control` etc.

\*The URDF file for this robot is not working properly for simulation purposes. Treads are not properly design so the don't move with the motor gears, and since the motor gears are not touching the ground movement is basically impossible. Until I'm able to rebuild the URDF with proper caterpillar treads and motor gears with their respective joints I will not focus on the simulation aspect of the robot. If you want to test the robot but can't build it yourself please go to [the original repository](https://github.com/YJ0528/minibot) this project is based on. -->

<!-- 3.  Launch Simulation Control and SLAM

    The `sim_control_station.launch.py` will launch all control features for the simulation, inclduing `teleop`, `slam_toolbox`, `nav2 stack`.

    - To run the control with `online_async_slam` from `slam_toolbox`, open a new terminal, source the local workspace and enter:

          ros2 launch minibot sim_control_station.launch.py use_slam_option:=online_async_slam

    - For `mapper_params_localization` from `slam_toolbox`:

          ros2 launch minibot sim_control_station.launch.py use_slam_option:=mapper_params_localization

      - To change the map to load, open the params file at [`./src/minibot/config/mapper_params_localization.yaml`](https://github.com/YJ0528/minibot/blob/aa18371856751b270af9280b53b87c7f5f3a6bcf/config/mapper_params_localization.yaml#L18), replace the value corresponding `map_file_name` with the desired directory.

    - For `AMCL` from `nav2`:

          ros2 launch minibot sim_control_station.launch.py use_slam_option:=amcl map:=./src/minibot/maps/sample_map.yaml

      - To change the map to load, replace the default value corresponding to [`map`](https://github.com/YJ0528/minibot/blob/aa18371856751b270af9280b53b87c7f5f3a6bcf/launch/sim_control_station.launch.py#L27) with the desired directory.

4.  Alternatively, we can just run the teleoperation only using:

        ros2 launch minibot joystick_teleop.launch.py -->

<!-- ### Additional Notes:

Refer to:

- [ros_gz_bridge](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#ros_gz_bridge) if a topic could not be send or recived between ROS 2 and Gazebo.
- [How a ROS 2 Topic Is Received By a Node](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#how-a-ros-2-topic-is-received-by-a-node) if you suspect topics are not being published or subscribed to properly
- [How to Check ROS 2 Node Parameter Name using Command Line](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#how-to-check-ros-2-node-parameter-name-using-command-line) if you want to check if the parameters from `.yaml` file is loaded to the node properly. -->

<br>
<br>

<!-- <div align="center">
	<h2> Setting Up the Robot </h2>
	<img src="https://github.com/KaiserGabo/halfonso/blob/main/visual_demos/robot_hardware.jpg" height="500">
	<p>Robot Hardware and Circuit Connection Setup</p>
</div> -->

<!-- s -->
## Lisf of Hardwares:

- Raspberry Pi 5
- YDLiDAR T-Mini Plus
- Tank chassis ([this is the one I used](https://www.amazon.com/XiaoR-Geek-Aluminum-Raspberry-Absorbing/dp/B09C7TK9Y9?s=industrial))
- 12V DC motor with encoders ([two of them](https://www.amazon.com/Encoder-Magnetic-Gearbox-Bracket-Reduction/dp/B07X5P1584), buy them just in case your chassis doesn't come with them)
- Arduino Nano Type C
- 5cm x 7cm pref board
- Female pin headers
- L298N motor driver
- 3S lipo battery\*
- Step down converter (I'm using this [DROK Buck Converter 12v to 5v, 5A](https://www.amazon.com/Converter-DROK-Regulator-Inverter-Transformer/dp/B01NALDSJ0?th=1))

This are the main components used for my project. If you want more information, please refer to
[Build a Mobile Robot with ROS: Bill of Materials](https://articulatedrobotics.xyz/tutorials/mobile-robot/project-overview/#bill-of-materials) by [Articulated Robotics](https://articulatedrobotics.xyz/)

see also: [Recommanded Components for Wiring and Robot Chasis (Optional)](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#recommanded-components-for-wiring-and-robot-chasis-optional).

\*I recommend getting a high capacity battery (at least 3000mah) since most of the components used here consume a considerable amount of energy.

<!-- <br> -->

## Configuring the Raspberry Pi:

Make sure you are using [Ubuntu 24.04](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) and have [ROS 2 Jazzy Jalisco](https://docs.ros.org/en/jazzy/index.html) installed in the Raspberry Pi.

**<ins>Install Ubuntu in Raspberry Pi using rpi-imager**</ins>

- Make sure you have a Micro SD Card with at least 32GB, but a Micro SD with <ins>**64GB or more**</ins> is recommanded.
- If you've never install Ubuntu 24.04 using rpi-imager before, see: [RPI5: Flash Ubuntu to SD Card](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#rpi5-flash-ubuntu-to-sd-card).

**<ins>Install ROS 2 in Raspberry Pi</ins>**

- For ROS 2 installation, you can select `ROS-Base Install` instead of `Desktop Install`.
- If you wish to run `RViz` in Raspberry Pi, consider `Desktop Install` or binary install via bash using `sudo apt install ros-jazzy-rviz2`.

**<ins>Configuring the Raspberry Pi 5 to Accept a Non-PD Power Supply</ins>**

If the Raspberry Pi 5 cannot identify a USB Power Delivery (PD) chip, it assumes the power supply cannot deliver 5A. Consequently, it restricts the total USB port current from 1600mA to 600mA and limits CPU power consumption to 3A. To resolve this issue, follow these steps:

**Increase the total USB current**

1.  Open a terminal and type this command:

        sudo nano /boot/firmware/config.txt

2.  Add the following line to the file:

        usb_max_current_enable=1

**Force the Raspberry Pi 5 to think it is using a 5A power supply**

1.  Open Terminal and type:

        sudo -E rpi-eeprom-config --edit

2.  Add this to the file (allowable options at 3000 or 5000):

        PSU_MAX_CURRENT=5000

**Warning: Only disable this safety feature if you are certain your power supply can deliver sufficient power without relying on the required PD standard. Operating without this protection on an inadequate power supply risks damaging your Raspberry Pi.**

<br>

## Installing Packages for Raspberry Pi and Flashing Code to Arduino Nano

<ins>**Creating a Workspace `robot_ws` in Your SBC (Raspberry Pi)**</ins>

1.  Open a terminal using `ctrl + alt + t`, create a workspace named `robot_ws` with a folder named `src`:

        mkdir -p ~/robot_ws/src

    - Replace `robot_ws` with the name you want to put as your workspace name.

2.  Follow to the insturction at [**Install ROS 2 Packages**](https://https://github.com/KaiserGabo/halfonso/blob/main/Package_Installation_Instruction.md#install-ros-2-package) to install all the necessary packages in Raspberry Pi.

<ins>**Flashing Code to Arduino Nano**</ins>

In addition, you need to Flash the driver code to your Arduino Nano, see [Install and Flash Microcontroller Driver code](https://https://github.com/KaiserGabo/halfonso/blob/main/Package_Installation_Instruction.md#install-and-flash-microcontroller-driver-code)

<br>

## Operating the Robot

1.  Ensure the Raspberry Pi USB device port number matched the value declared:

    - `/dev/ttyUSB0` for the lidar serial; located at [`./src/ydlidar_ros2_driver/params/ydlidar.yaml/ydlidar_ros2_driver_node`](https://github.com/KaiserGabo/ydlidar_ros2_driver/blob/main/params/ydlidar.yaml#L4)
    - `/dev/ttyUSB1` for the Arduino Nano; located at [`./src/halfonso/description/ros2_control.xacro/RobotSystem/device`](https://github.com/KaiserGabo/halfonso/blob/main/description/ros2_control.xacro#L11)
    - To check or troubleshoot the USB connection in Raspberry Pi, see [RPI5: Add USB Access for Raspberry Pi](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#rpi5-add-usb-access-for-raspberry-pi).

    - I do recommend matching the device ports either `by-id` (the individual ID of the device itself) or `by-path` (the actual USB port the device is connected to). To get this values, open terminal and type:

            ls /dev/serial/by-id*
            #or
            ls /dev/serial/by-path*

2.  Connect to the Raspberry Pi from your server machine using `openssh-server`. Open a terminal in the server machine, enter:

        ssh <remote_username>@<remote_ip_address>

    - If you never install or use `openssh-server` before, see [SSH Access to Remote Machine- Connect Remote Machine via Terminal](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#connecting-to-the-remote-machine-in-terminal).

3.  In order to let the nodes to be discoverable between the server and the remote machine, We need to set `ROS_DOMAIN_ID` to the same for both of the machine:

        # The ID is 0 by default, but can be any number between 0 between 101
        export ROS_DOMAIN_ID=1

    - For the Raspberry Pi, we can add `export ROS_DOMAIN_ID=1` to the `.bashrc` file instead using:

          echo "export ROS_DOMAIN_ID=1" >> ~/.bashrc
          source ~/.bashrc

    - To check the `ROS_DOMAIN_ID` set, enter `echo ${ROS_DOMAIN_ID}` in terminal.
    - II both your remote machine and robot share the same `ROS_DOMAIN_ID` but still cannot communicate with each other, a firewall is likely blocking data transmission. To resolve this issue, allow the ROS 2 UDP port range corresponding to your domain ID through your firewall. ([You can find the values of your ID using this calculator](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Domain-ID.html#domain-id-to-udp-port-calculator)):
  
            # Allow the ROS 2 UDP port range
		    sudo ufw allow 7400:7500/udp #Values depend on the range of your ID
		    # Reload the rules
		    sudo ufw reload

4.  Once Everything is set, go to `your_workspace` and source the workspace:

        source ros_ws/install/setup.bash

    - When a new terminal is opened, ensure that terminal sourced the workspace also:

5.  Run the robot:

        ros2 launch halfonso_v2 robot.launch.py

    - This will launch `robot description`,`ros2_control`, etc.

6.  Launch the RVIZ interface:

        ros2 launch halfonso_v2 rviz.launch.py

7.  Launching SLAM algorithm:

        ros2 launch slam_gmapping slam_gmappin.launch.py

    - This will launch the `slam_gmapping` algorithm with RVIZ, however you can also use `slam_toolbox` as an alternative with this command:
            
            ros2 launch slam_toolbox online_async_launch.py

8.  Launch the Autonomous Exploration:

    - First you must launch de `nav2` stack for navigation

            ros2 launch nav2_bringup navigation_launch use_sim_time:=False

    - After that, you can launch the `explorer` node for autonomous exploration

            ros2 run custom_explorer explorer

9.  Alternatively, we can just run the teleoperation only using:

        ros2 launch halfonso_v2 joystick_teleop.launch.py

<br>

<!-- ## Demo: -->

<!-- Some visual demostration:

<div align="center">
	<h3> SLAM with Joystick Teleoperation (5x speed with defualt parameter) </h3>
	<img src="https://github.com/KaiserGabo/halfonso/blob/main/visual_demos/SLAM_demostration-ezgif.com-video-to-gif-converter.gif" height="400">
	<br><br>
 	<h3> Nav2 Navigation using SLAM Toolbox Localization (5x speed)</h3>
	<img src="https://github.com/KaiserGabo/halfonso/blob/main/visual_demos/Nav2_demostration-ezgif.com-video-to-gif-converter.gif" height="400">
</div>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`global_costmap/global_costmap/ros__parameters/inflation_layer/cost_scaling_factor`= 1.0

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`global_costmap/global_costmap/ros__parameters/inflation_layer/inflation_radius`= 0.05 -->

<!-- ## TO DO (maybe, perhaps, more probable than not):

- Improve the odometry of the robot (is not that precise for mapping).
- Integrate a GPS module and display the coordinates on RVIZ.
- Design a custom PCB for power delivery and one that combines the micro controller and the motor driver.
- Improve the autonomous exploration algorithm.
- Make a proper URDF for the treads so I can simulate this thing (if someone else can do it I will appreciate it for life).
- Desinging a better enclosure so no component is exposed. -->
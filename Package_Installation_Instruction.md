### List of Content:

- [Introduction](https://github.com/KaiserGabo/halfonso_v2/blob/6558e4d5b8d42392bfdf5a7e03758e528c2fcc80/Package_Installation_Instruction.md#introduction)
- [Install ROS 2 Packages](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#install-ros-2-package)
- [Install and Flash Microcontroller Driver code](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#install-and-flash-microcontroller-driver-code)
- [Extra Notes](https://github.com/KaiserGabo/halfonso_v2/blob/6558e4d5b8d42392bfdf5a7e03758e528c2fcc80/Package_Installation_Instruction.md#extra-notes)

## Introduction

There are 2 ways to install ROS2 package, either via binary installation or build from source. Most of the stable-released standard ROS2 package can be installed via binary, while building the package from source allows more flexibility in modifying the package(s) content, or to install additional third-party package(s).

For more information, see:

- [Explaination on ROS 2 Packages](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#explanation-on-ros-2-packages)
- [Configuring your ROS 2 environment](https://docs.ros.org/en/eloquent/Tutorials/Configuring-ROS2-Environment.html#background)

<br>

# Install ROS 2 Package:

The directory for the instruction to install required packages are listed below:

<!-- **For simulation only:**

- [ros_gz](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#ros_gz)
- [ros2_control](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#ros2_control)
- [nav2 stack](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#nav2c)
- [slam_gmapping](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#slam_gmapping)
- [custom_explorer](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#custom_explorer)
- [twist_mux](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#twist_mux)
- [twist_stamper](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#twist_stamper) -->

<!-- **For driver and hardware interface (in addition to the file listed for simulation, except `ros_gz`):**

- [diffdrive_arduino](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#diffdrive_arduino)
- [serial](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#twist_stamper)
- [ydlidar_ros2_driver](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#ydlidar_ros2_driver) -->

<!-- ### Third-party Packages Repository -->

<!-- Among the above listed packages, the following are third-party packages: -->
- [ros2_control](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#ros2_control)
- [nav2 stack](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#nav2)
- [slam_gmapping](https://github.com/KaiserGabo/slam_gmapping.git)
- [custom_explorer](https://github.com/KaiserGabo/Autonomous-Explorer-and-Mapper-ros2-nav2)
- [twist_mux](https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#twist_mux)
- [twist_stamper](https://github.com/joshnewans/twist_stamper.git)
- [diffdrive_arduino](https://github.com/KaiserGabo/ros_arduino_bridge) (forked from [here](https://github.com/YJ0528/diffdrive_arduino))
- [serial](https://github.com/joshnewans/serial.git)
- [ydlidar_ros2_driver](https://github.com/KaiserGabo/ydlidar_ros2_driver)

<!-- ## ros_gz

ROS2 Jazzy Jalisco supports Gazebo Harmonic (LTS), see [Summary of Compatible ROS and Gazebo Combinations](https://gazebosim.org/docs/harmonic/ros_installation/#summary-of-compatible-ros-and-gazebo-combinations).

### Binary Installation

- Install the **default gazebo/ROS pairing** by following the instruction given [Installing the Default Gazebo/ROS Pairing](https://gazebosim.org/docs/harmonic/ros_installation/#installing-the-default-gazebo-ros-pairing).

      sudo apt-get install ros-${ROS_DISTRO}-ros-gz

### Build from source

- Install the required **gazebo packages** by following the instruction given [here](https://github.com/gazebosim/ros_gz/tree/jazzy?tab=readme-ov-file#install) (optional, if create node is not available) .

In order to build ros_gz from source, sufficient RAM is essential to avoid the machine from getting crashed.
If the machine consist of 8GB RAM or less, expanding the virtual RAM with the instruction [How to Increase Virtual Memory](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#how-to-increase-virtual-memory).

<br> -->

## ros2_control

### Binary Installation

- Install ros2_control for Jazzy Jalisco using:

      sudo apt install ros-jazzy-ros2-control

### Build from source

- Install ros2_control from source following the instruction [here](https://control.ros.org/jazzy/doc/getting_started/getting_started.html#building-from-source) (optional, in case the spawner.py is not found).

<br>

## nav2

### Binary Installation

- Install nav2 stack for Jazzy Jalisco using:

      sudo apt install ros-jazzy-navigation2 ros-jazzy-nav2-bringup

<br>

## slam_gmapping

### Build from source

1.  Clone the package from github in you `home` directory:

        https://github.com/KaiserGabo/slam_gmapping_ros2.git

2.  Move the folders inside the cloned folder into your `ros_ws/src` folder

        cd slam_gmaping
        mv openslam_gmapping ~/ros_ws/src
        mv slam_gmapping ~/ros_ws/src

3.  Build the packages:

        ##Remove <--packages-select your_package> to build all other packages

        colcon build --symlink-install --packages-select slam_gmapping openslam_gmapping

<br>


## custom_explorer

This package is a contribution from [Arka Ghosh](https://github.com/AniArka/Autonomous-Explorer-and-Mapper-ros2-nav2). While the original package says is for ROS 2 Humble, it compiles on Jazzy without problems.

### Build from source

1.  Go the the workspace src:

        ##Example:
        cd ros_ws/
        cd src/

2.  Clone the package from github:

        https://github.com/KaiserGabo/Autonomous-Explorer-and-Mapper-ros2-nav2.git

3.  Build the package:

        ##Remove <--packages-select twist_stamper> to build all other packages

        colcon build --symlink-install --packages-select Autonomous-Explorer-and-Mapper-ros2-nav2

<br>

## twist_mux

### Binary installation

The recently updated version (4.4.0) supports stamped cmd_vel, which can be installed directly:

    sudo apt install ros-jazzy-twist-mux

**The following version is not tested yet so the parameter name could be different.**

<!-- - To check the parameter name, see [Useful Tips: Check node parameter name in command line](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#how-to-check-ros-2-node-parameter-name-using-command-line) -->

### Build from source

Alternatively, if user wish to build from source:

1.  Go the the workspace src:

        ##Example:
        cd ros_ws/
        cd src/

2.  Clone the package from github:

        https://github.com/KaiserGabo/twist_mux.git

    - Alternatively, user can still convert unstamped cmd_vel to stamped using [twist_stamper](https://https://github.com/KaiserGabo/halfonso_v2/blob/73d7fda2b1881797845e8b4fddb37570d108c938/Package_Installation_Instruction.md#ros2_control#twist_stamper).

3.  Build the package:

        ##Remove <--packages-select twist_stamper> to build all other packages

        colcon build --symlink-install --packages-select twist_mux

<br>

## twist_stamper

twist_stamper is a third-party package contributed by [Josh Newans](https://github.com/joshnewans), [niemsoen](https://github.com/niemsoen), and [Rick-v-E](https://github.com/Rick-v-E). Since it is not an official ROS 2 package, it can only build from source.

#### Build from source

1.  Go the the workspace src:

        ##Example:
        cd ros_ws/
        cd src/

2.  Clone the package from github:

        git clone https://github.com/joshnewans/twist_stamper.git

3.  Build the package:

        ##Remove <--packages-select your_package> to build all other packages

        colcon build --symlink-install --packages-select twist_stamper

<br>

## diffdrive_arduino

#### Build from source

1.  Go the the workspace src:

        ##Example:
        cd ros_ws/
        cd src/

2.  Clone the package from github:

        git clone https://github.com/KaiserGabo/diffdrive_arduino.git

3.  Build the package:

        ##Remove <--packages-select your_package> to build all other packages

        colcon build --symlink-install --packages-select diffdrive_arduino

<br>

## serial

#### Build from source

1.  Go the the workspace src:

        ##Example:
        cd ros_ws/
        cd src/

2.  Clone the package from github:

        git clone https://github.com/joshnewans/serial

    <!-- - I have created a fork with the Humble branch so it could be cloned directly.
    - The pacakages works with Jazzy version although it is built for Humble. -->

3.  Build the package:

        ##Remove <--packages-select your_package> to build all other packages

        colcon build --symlink-install --packages-select serial

<br>

## ydlidar_ros2_driver

- Build the `ydlidar_ros2_driver` package from source following the instruction [here](https://github.com/KaiserGabo/ydlidar_ros2_driver).

<br>

# Install and Flash Microcontroller Driver Code

The arduino driver code repository can be found at here: [ros_arduino_bridge](https://github.com/KaiserGabo/ros_arduino_bridge.git).

### A. Install Arduino IDE

1. Make sure you have arduino installed in the machine, otherwise see [Arduino IDE 1 Installation (Linux)](https://docs.arduino.cc/software/ide-v1/tutorials/Linux/).
<!-- 2.	Open the Arduino IDE, install the ESP32 add-on in Arduino IDE, see [Installing the ESP32 Board in Arduino IDE (Windows, Mac OS X, Linux)](https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/)
2. In the Arduino IDE, install the following libraries via Tools -> Manage Libraries...
   - ESP32Encoder version 0.11.7, repository: https://github.com/madhephaestus/ESP32Encoder.git
   - Cytron Motor Drivers Library version 1.0.1, repository: https://github.com/CytronTechnologies/CytronMotorDriver -->

### B. Flashing the Driver code

1.  clone the driver code to local:

        git clone https://github.com/KaiserGabo/ros_arduino_bridge.git

    - Can place the code in any directory, as long as it can be open by the IDE.

2.  In Arduino IDE, open the cloned sketch: 
    - ros_arduino_bridge/RosArduinoBridge/[RosArduinoBridge.ino](https://github.com/KaiserGabo/ros_arduino_bridge/blob/main/ROSArduinoBridge/ROSArduinoBridge.ino).
3.  Ensure the Arduino Nano serial is connected and accessible to the machine, set the port number to the Nano dev/ttyUSB0 and flash
4.  The default port number starts from `dev/ttyUSB0`, `dev/ttyUSB0`..., check serial port using

        ls -l /dev/ttyUSB*

5.  If the Arduino Nano is plugged into the serial port but the it is not recognized by the IDE, see [RPI5: Add USB Access for Raspberry Pi](https://github.com/KaiserGabo/halfonso/blob/main/Tips_and_Troubleshooting.md#rpi5-add-usb-access-for-raspberry-pi).


<!-- 6.  Run python miniterm with echo and set serial port, and baud rate as following (assume serial port= /dev/ttyUSB0):

        python3 -m serial.tools.miniterm -e /dev/ttyUSB0 576000 -->

### Extra notes

- **ESP32 & Cytron MDD3A Support:** Compatibility for the ESP32 microcontroller and Cytron MDD3A motor driver was contributed by [YJ0528](https://github.com/YJ0528/ros_arduino_bridge.git). This project utilizes the default configuration from [Josh Newans ](https://github.com/joshnewans/ros_arduino_bridge.git)' repository. If you are using these components, follow the Microcontroller Driver Setup Instructions.
- **3.3V Logic Level Warning (L298N):** If you are using a 3.3V logic microcontroller (e.g., ESP32, Raspberry Pi Pico) with an L298N motor driver, a logic level shifter is strongly recommended. Although the L298N may respond to 3.3V signals during basic testing, it requires 5V logic inputs to operate reliably under normal conditions.
- **Encoder Orientation:** If a motor encoder count decreases (goes negative) while the motor is driving forward, swap the two encoder output pins (`Phase A` and `Phase B`).

<!-- ## TODO (maybe):

- Porting the `ros_arduino_bridge` to PlatformIO (I really don't like working with the Arduino IDE 1.x but it's the only available version on the Raspberry Pi, also I just prefer PLatformIO in general) -->
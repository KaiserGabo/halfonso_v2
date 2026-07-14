cmake_minimum_required(VERSION 3.5)
project(halfonso_v2)

set(CMAKE_CXX_STANDARD 17)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY config description launch worlds
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

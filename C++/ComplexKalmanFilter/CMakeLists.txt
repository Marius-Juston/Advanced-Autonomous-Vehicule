# CMakeList.txt : CMake project for Example, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.8)

add_executable(ComplexKalmanFilter "main.cpp" measurement_package.h tracking.cpp kalman_filter.cpp)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/obj_pose-laser-radar-synthetic-input.txt
        ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
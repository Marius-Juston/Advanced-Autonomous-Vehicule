# CMakeList.txt : CMake project for Example, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.8)

add_executable(ComplexKalmanFilter "main.cpp" measurement_package.h tracking.cpp kalman_filter.cpp)

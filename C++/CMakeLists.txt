cmake_minimum_required(VERSION 3.16)
project(C__)

set(CMAKE_CXX_STANDARD 14)

INCLUDE_DIRECTORIES("libraries/eigen3/Eigen")

add_subdirectory(KalmanFilter)
add_subdirectory(ComplexKalmanFilter)
add_subdirectory(CalculateJacobian)
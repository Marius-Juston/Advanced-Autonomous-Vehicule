# CMakeList.txt : CMake project for Example, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.8)

add_executable(HybridAStar "main.cpp" hybrid_breadth_first.cpp hybrid_breadth_first.h)

# CMakeList.txt : CMake project for Example, include source and define
# project specific logic here.
#
cmake_minimum_required(VERSION 3.8)

add_executable(MyNaiveBayesMotionClassifier "main.cpp" classifier.cpp classifier.h)

configure_file(${CMAKE_CURRENT_SOURCE_DIR}/test_labels.txt ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/test_states.txt ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/train_labels.txt ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)
configure_file(${CMAKE_CURRENT_SOURCE_DIR}/train_states.txt ${CMAKE_CURRENT_BINARY_DIR} COPYONLY)

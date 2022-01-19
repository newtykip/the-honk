cmake_minimum_required(VERSION 3.13)
project(the-honk)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

add_executable(pascal code/pascal.cc)
add_executable(babylonian code/babylonian.cc)
add_executable(karatsuba code/karatsuba.cc)
add_executable(dice code/dice.cc)
add_executable(binomialExpansion code/binomialExpansion.cc)
add_executable(squareForm code/squareForm.cc)

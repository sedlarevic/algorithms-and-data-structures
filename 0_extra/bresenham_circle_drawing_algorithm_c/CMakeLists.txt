cmake_minimum_required(VERSION 3.20)
project(circle C)

set(CMAKE_C_STANDARD 11)

add_executable(circle main.c)

target_include_directories(circle PRIVATE /opt/homebrew/opt/sdl2/include)
target_link_directories(circle PRIVATE /opt/homebrew/opt/sdl2/lib)
target_link_libraries(circle PRIVATE SDL2)
cmake_minimum_required(VERSION 3.16)

set(CMAKE_TOOLCHAIN_FILE ../cmake/arm-gcc-toolchain.cmake)

# set the project name and version
project(demo-nrf52-hrs VERSION 1.0 LANGUAGES C ASM)


# Location of application specific code
add_subdirectory(examples/ble_peripheral/ble_app_hrs)


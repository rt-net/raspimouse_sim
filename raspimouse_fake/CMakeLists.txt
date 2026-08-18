cmake_minimum_required(VERSION 3.20)
project(raspimouse_fake)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(lifecycle_msgs REQUIRED)
find_package(std_srvs REQUIRED)

add_library(fake_raspimouse_component SHARED
  src/fake_raspimouse_component.cpp)
target_include_directories(fake_raspimouse_component PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_definitions(fake_raspimouse_component
  PRIVATE "RASPIMOUSE_FAKE_BUILDING_DLL")
target_link_libraries(fake_raspimouse_component PUBLIC
  rclcpp::rclcpp
  rclcpp_components::component
  rclcpp_lifecycle::rclcpp_lifecycle
  lifecycle_msgs::lifecycle_msgs__rosidl_generator_cpp
  std_srvs::std_srvs__rosidl_generator_cpp)
rclcpp_components_register_nodes(fake_raspimouse_component "fake_raspimouse::Raspimouse")

ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)

ament_export_dependencies(rclcpp)
ament_export_dependencies(rclcpp_components)
ament_export_dependencies(rclcpp_lifecycle)
ament_export_dependencies(std_srvs)
ament_export_dependencies(lifecycle_msgs)

ament_export_include_directories(include)
ament_export_libraries(
  fake_raspimouse_component)

install(
  DIRECTORY include/
  DESTINATION include/
)

install(TARGETS
  fake_raspimouse_component
  EXPORT export_${PROJECT_NAME}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
  INCLUDES DESTINATION include)

install(TARGETS
  DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY
  DESTINATION share/${PROJECT_NAME}/
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

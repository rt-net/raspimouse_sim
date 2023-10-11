cmake_minimum_required(VERSION 3.5)
project(raspimouse_fake)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_components REQUIRED)
find_package(rclcpp_lifecycle REQUIRED)
find_package(lifecycle_msgs REQUIRED)
find_package(std_srvs REQUIRED)

include_directories(include)

add_library(fake_raspimouse_component SHARED
  src/fake_raspimouse_component.cpp)
target_compile_definitions(fake_raspimouse_component
  PRIVATE "RASPIMOUSE_FAKE_BUILDING_DLL")
ament_target_dependencies(fake_raspimouse_component
  rclcpp
  rclcpp_components
  rclcpp_lifecycle
  std_srvs)
rclcpp_components_register_nodes(fake_raspimouse_component "fake_raspimouse::Raspimouse")

ament_export_targets(export_${PROJECT_NAME} HAS_LIBRARY_TARGET)

ament_export_dependencies(rclcpp)
ament_export_dependencies(rclcpp_components)
ament_export_dependencies(rclcpp_lifecycle)

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

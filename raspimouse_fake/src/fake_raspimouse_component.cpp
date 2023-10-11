// The MIT License (MIT)
//
// Copyright 2023 RT Corporation <support@rt-net.jp>
//
// Permission is hereby granted, free of charge, to any person obtaining a copy of
// this software and associated documentation files (the "Software"), to deal in
// the Software without restriction, including without limitation the rights to
// use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
// the Software, and to permit persons to whom the Software is furnished to do so,
// subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
// FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
// COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
// IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
// CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#include "raspimouse_fake/fake_raspimouse_component.hpp"

#include "rclcpp/rclcpp.hpp"
#include "lifecycle_msgs/srv/change_state.hpp"
#include "std_srvs/srv/set_bool.hpp"

using namespace std::chrono_literals;
using CallbackReturn = rclcpp_lifecycle::node_interfaces::LifecycleNodeInterface::CallbackReturn;

namespace fake_raspimouse
{

Raspimouse::Raspimouse(const rclcpp::NodeOptions & options)
: rclcpp_lifecycle::LifecycleNode("fake_raspimouse", options)
{
}

CallbackReturn Raspimouse::on_configure(const rclcpp_lifecycle::State &)
{
  RCLCPP_INFO(this->get_logger(), "on_configure() is called.");

  using namespace std::placeholders;  // for _1, _2, _3...

  motor_power_service_ = create_service<std_srvs::srv::SetBool>(
    "motor_power", std::bind(&Raspimouse::handle_motor_power, this, _1, _2, _3));

  return CallbackReturn::SUCCESS;
}

CallbackReturn Raspimouse::on_activate(const rclcpp_lifecycle::State &)
{
  RCLCPP_INFO(this->get_logger(), "on_activate() is called.");

  return CallbackReturn::SUCCESS;
}

CallbackReturn Raspimouse::on_deactivate(const rclcpp_lifecycle::State &)
{
  RCLCPP_INFO(this->get_logger(), "on_deactivate() is called.");

  return CallbackReturn::SUCCESS;
}

CallbackReturn Raspimouse::on_cleanup(const rclcpp_lifecycle::State &)
{
  RCLCPP_INFO(this->get_logger(), "on_cleanup() is called.");

  return CallbackReturn::SUCCESS;
}

CallbackReturn Raspimouse::on_shutdown(const rclcpp_lifecycle::State &)
{
  RCLCPP_INFO(this->get_logger(), "on_shutdown() is called.");

  return CallbackReturn::SUCCESS;
}

void Raspimouse::handle_motor_power(
  const std::shared_ptr<rmw_request_id_t> request_header,
  const std::shared_ptr<std_srvs::srv::SetBool::Request> request,
  const std::shared_ptr<std_srvs::srv::SetBool::Response> response)
{
  (void)request_header;
  response->success = true;
  if (request->data) {
    response->message = "Motors are on";
  } else {
    response->message = "Motors are off";
  }
}

}  // namespace fake_raspimouse

#include "rclcpp_components/register_node_macro.hpp"

RCLCPP_COMPONENTS_REGISTER_NODE(fake_raspimouse::Raspimouse)

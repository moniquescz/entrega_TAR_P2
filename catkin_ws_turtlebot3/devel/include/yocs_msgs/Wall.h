// Generated by gencpp from file yocs_msgs/Wall.msg
// DO NOT EDIT!


#ifndef YOCS_MSGS_MESSAGE_WALL_H
#define YOCS_MSGS_MESSAGE_WALL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/PoseWithCovarianceStamped.h>

namespace yocs_msgs
{
template <class ContainerAllocator>
struct Wall_
{
  typedef Wall_<ContainerAllocator> Type;

  Wall_()
    : name()
    , length(0.0)
    , width(0.0)
    , height(0.0)
    , pose()  {
    }
  Wall_(const ContainerAllocator& _alloc)
    : name(_alloc)
    , length(0.0)
    , width(0.0)
    , height(0.0)
    , pose(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _name_type;
  _name_type name;

   typedef float _length_type;
  _length_type length;

   typedef float _width_type;
  _width_type width;

   typedef float _height_type;
  _height_type height;

   typedef  ::geometry_msgs::PoseWithCovarianceStamped_<ContainerAllocator>  _pose_type;
  _pose_type pose;





  typedef boost::shared_ptr< ::yocs_msgs::Wall_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::yocs_msgs::Wall_<ContainerAllocator> const> ConstPtr;

}; // struct Wall_

typedef ::yocs_msgs::Wall_<std::allocator<void> > Wall;

typedef boost::shared_ptr< ::yocs_msgs::Wall > WallPtr;
typedef boost::shared_ptr< ::yocs_msgs::Wall const> WallConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::yocs_msgs::Wall_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::yocs_msgs::Wall_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::yocs_msgs::Wall_<ContainerAllocator1> & lhs, const ::yocs_msgs::Wall_<ContainerAllocator2> & rhs)
{
  return lhs.name == rhs.name &&
    lhs.length == rhs.length &&
    lhs.width == rhs.width &&
    lhs.height == rhs.height &&
    lhs.pose == rhs.pose;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::yocs_msgs::Wall_<ContainerAllocator1> & lhs, const ::yocs_msgs::Wall_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace yocs_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::yocs_msgs::Wall_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::yocs_msgs::Wall_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::yocs_msgs::Wall_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::yocs_msgs::Wall_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::yocs_msgs::Wall_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::yocs_msgs::Wall_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::yocs_msgs::Wall_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6fba3b6a148ebf1773d978f0b5f0bde8";
  }

  static const char* value(const ::yocs_msgs::Wall_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6fba3b6a148ebf17ULL;
  static const uint64_t static_value2 = 0x73d978f0b5f0bde8ULL;
};

template<class ContainerAllocator>
struct DataType< ::yocs_msgs::Wall_<ContainerAllocator> >
{
  static const char* value()
  {
    return "yocs_msgs/Wall";
  }

  static const char* value(const ::yocs_msgs::Wall_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::yocs_msgs::Wall_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Virtual wall obstacle;\n"
"#  - Assumed to be a plan, so width is ignored by now\n"
"#  - The yaw provides the orientation of x-axis\n"
"#  - Assumed vertically aligned (roll and pitch must be 0)\n"
"#  - Z provides the lower border of the wall (normally 0)\n"
"\n"
"string  name\n"
"float32 length\n"
"float32 width\n"
"float32 height\n"
"geometry_msgs/PoseWithCovarianceStamped pose\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PoseWithCovarianceStamped\n"
"# This expresses an estimated pose with a reference coordinate frame and timestamp\n"
"\n"
"Header header\n"
"PoseWithCovariance pose\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in python3 the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in python3 the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/PoseWithCovariance\n"
"# This represents a pose in free space with uncertainty.\n"
"\n"
"Pose pose\n"
"\n"
"# Row-major representation of the 6x6 covariance matrix\n"
"# The orientation parameters use a fixed-axis representation.\n"
"# In order, the parameters are:\n"
"# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)\n"
"float64[36] covariance\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::yocs_msgs::Wall_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::yocs_msgs::Wall_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.name);
      stream.next(m.length);
      stream.next(m.width);
      stream.next(m.height);
      stream.next(m.pose);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Wall_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::yocs_msgs::Wall_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::yocs_msgs::Wall_<ContainerAllocator>& v)
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.name);
    s << indent << "length: ";
    Printer<float>::stream(s, indent + "  ", v.length);
    s << indent << "width: ";
    Printer<float>::stream(s, indent + "  ", v.width);
    s << indent << "height: ";
    Printer<float>::stream(s, indent + "  ", v.height);
    s << indent << "pose: ";
    s << std::endl;
    Printer< ::geometry_msgs::PoseWithCovarianceStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.pose);
  }
};

} // namespace message_operations
} // namespace ros

#endif // YOCS_MSGS_MESSAGE_WALL_H

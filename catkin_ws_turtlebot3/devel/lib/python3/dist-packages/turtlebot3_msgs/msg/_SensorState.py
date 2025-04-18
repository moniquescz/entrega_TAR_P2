# This python3 file uses the following encoding: utf-8
"""autogenerated by genpy from turtlebot3_msgs/SensorState.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SensorState(genpy.Message):
  _md5sum = "7250c1dc0b61c4190e78f528f599285f"
  _type = "turtlebot3_msgs/SensorState"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """########################################
# CONSTANTS
########################################
# Bumper states (states are combined, when multiple bumpers are pressed)
uint8 BUMPER_FORWARD  = 1
uint8 BUMPER_BACKWARD = 2

# Cliff sensor states (states are combined, when multiple cliff sensors are triggered)
uint8 CLIFF = 1

# Sonar sensor states (states are combined, when multiple sonar sensors are triggered)
uint8 SONAR = 1

# Illumination sensor (states are combined, when multiple illumination sensors are triggered) 
uint8 ILLUMINATION = 1

# Button states (states are combined, when multiple buttons are pressed)
uint8 BUTTON0 = 1
uint8 BUTTON1 = 2

# Motor errors
uint8 ERROR_LEFT_MOTOR  = 1
uint8 ERROR_RIGHT_MOTOR = 2

# Motor torque
uint8 TORQUE_ON  = 1
uint8 TORQUE_OFF = 2

########################################
# Messages
########################################
Header  header
uint8   bumper
float32 cliff
float32 sonar
float32 illumination
uint8   led
uint8  button
bool   torque
int32  left_encoder    # (-2,147,483,648 ~ 2,147,483,647)
int32  right_encoder   # (-2,147,483,648 ~ 2,147,483,647)
float32  battery

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in python3 the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in python3 the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  # Pseudo-constants
  BUMPER_FORWARD = 1
  BUMPER_BACKWARD = 2
  CLIFF = 1
  SONAR = 1
  ILLUMINATION = 1
  BUTTON0 = 1
  BUTTON1 = 2
  ERROR_LEFT_MOTOR = 1
  ERROR_RIGHT_MOTOR = 2
  TORQUE_ON = 1
  TORQUE_OFF = 2

  __slots__ = ['header','bumper','cliff','sonar','illumination','led','button','torque','left_encoder','right_encoder','battery']
  _slot_types = ['std_msgs/Header','uint8','float32','float32','float32','uint8','uint8','bool','int32','int32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,bumper,cliff,sonar,illumination,led,button,torque,left_encoder,right_encoder,battery

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SensorState, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.bumper is None:
        self.bumper = 0
      if self.cliff is None:
        self.cliff = 0.
      if self.sonar is None:
        self.sonar = 0.
      if self.illumination is None:
        self.illumination = 0.
      if self.led is None:
        self.led = 0
      if self.button is None:
        self.button = 0
      if self.torque is None:
        self.torque = False
      if self.left_encoder is None:
        self.left_encoder = 0
      if self.right_encoder is None:
        self.right_encoder = 0
      if self.battery is None:
        self.battery = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.bumper = 0
      self.cliff = 0.
      self.sonar = 0.
      self.illumination = 0.
      self.led = 0
      self.button = 0
      self.torque = False
      self.left_encoder = 0
      self.right_encoder = 0
      self.battery = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B3f3B2if().pack(_x.bumper, _x.cliff, _x.sonar, _x.illumination, _x.led, _x.button, _x.torque, _x.left_encoder, _x.right_encoder, _x.battery))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.bumper, _x.cliff, _x.sonar, _x.illumination, _x.led, _x.button, _x.torque, _x.left_encoder, _x.right_encoder, _x.battery,) = _get_struct_B3f3B2if().unpack(str[start:end])
      self.torque = bool(self.torque)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python3 module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B3f3B2if().pack(_x.bumper, _x.cliff, _x.sonar, _x.illumination, _x.led, _x.button, _x.torque, _x.left_encoder, _x.right_encoder, _x.battery))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python3 module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 28
      (_x.bumper, _x.cliff, _x.sonar, _x.illumination, _x.led, _x.button, _x.torque, _x.left_encoder, _x.right_encoder, _x.battery,) = _get_struct_B3f3B2if().unpack(str[start:end])
      self.torque = bool(self.torque)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_B3f3B2if = None
def _get_struct_B3f3B2if():
    global _struct_B3f3B2if
    if _struct_B3f3B2if is None:
        _struct_B3f3B2if = struct.Struct("<B3f3B2if")
    return _struct_B3f3B2if

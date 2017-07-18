# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorboard/src/graph.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorboard.src import node_def_pb2 as tensorboard_dot_src_dot_node__def__pb2
from tensorboard.src import versions_pb2 as tensorboard_dot_src_dot_versions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorboard/src/graph.proto',
  package='tensorboard',
  syntax='proto3',
  serialized_pb=_b('\n\x1btensorboard/src/graph.proto\x12\x0btensorboard\x1a\x1etensorboard/src/node_def.proto\x1a\x1etensorboard/src/versions.proto\"n\n\x08GraphDef\x12\"\n\x04node\x18\x01 \x03(\x0b\x32\x14.tensorboard.NodeDef\x12)\n\x08versions\x18\x04 \x01(\x0b\x32\x17.tensorboard.VersionDef\x12\x13\n\x07version\x18\x03 \x01(\x05\x42\x02\x18\x01\x42,\n\x18org.tensorflow.frameworkB\x0bGraphProtosP\x01\xf8\x01\x01\x62\x06proto3')
  ,
  dependencies=[tensorboard_dot_src_dot_node__def__pb2.DESCRIPTOR,tensorboard_dot_src_dot_versions__pb2.DESCRIPTOR,])




_GRAPHDEF = _descriptor.Descriptor(
  name='GraphDef',
  full_name='tensorboard.GraphDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='tensorboard.GraphDef.node', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versions', full_name='tensorboard.GraphDef.versions', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorboard.GraphDef.version', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=218,
)

_GRAPHDEF.fields_by_name['node'].message_type = tensorboard_dot_src_dot_node__def__pb2._NODEDEF
_GRAPHDEF.fields_by_name['versions'].message_type = tensorboard_dot_src_dot_versions__pb2._VERSIONDEF
DESCRIPTOR.message_types_by_name['GraphDef'] = _GRAPHDEF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GraphDef = _reflection.GeneratedProtocolMessageType('GraphDef', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHDEF,
  __module__ = 'tensorboard.src.graph_pb2'
  # @@protoc_insertion_point(class_scope:tensorboard.GraphDef)
  ))
_sym_db.RegisterMessage(GraphDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030org.tensorflow.frameworkB\013GraphProtosP\001\370\001\001'))
_GRAPHDEF.fields_by_name['version'].has_options = True
_GRAPHDEF.fields_by_name['version']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\030\001'))
# @@protoc_insertion_point(module_scope)

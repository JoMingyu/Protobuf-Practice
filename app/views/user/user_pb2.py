# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='user',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nuser.proto\x12\x04user\"5\n\rSignupRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\n\n\x02pw\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\tb\x06proto3')
)




_SIGNUPREQUEST = _descriptor.Descriptor(
  name='SignupRequest',
  full_name='user.SignupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='user.SignupRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pw', full_name='user.SignupRequest.pw', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='user.SignupRequest.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=73,
)

DESCRIPTOR.message_types_by_name['SignupRequest'] = _SIGNUPREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignupRequest = _reflection.GeneratedProtocolMessageType('SignupRequest', (_message.Message,), dict(
  DESCRIPTOR = _SIGNUPREQUEST,
  __module__ = 'user_pb2'
  # @@protoc_insertion_point(class_scope:user.SignupRequest)
  ))
_sym_db.RegisterMessage(SignupRequest)


# @@protoc_insertion_point(module_scope)
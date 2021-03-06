# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/experiment.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from rastervision.protos import dataset_pb2 as rastervision_dot_protos_dot_dataset__pb2
from rastervision.protos import task_pb2 as rastervision_dot_protos_dot_task__pb2
from rastervision.protos import backend_pb2 as rastervision_dot_protos_dot_backend__pb2
from rastervision.protos import analyzer_pb2 as rastervision_dot_protos_dot_analyzer__pb2
from rastervision.protos import evaluator_pb2 as rastervision_dot_protos_dot_evaluator__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/experiment.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n$rastervision/protos/experiment.proto\x12\trv.protos\x1a\x1cgoogle/protobuf/struct.proto\x1a!rastervision/protos/dataset.proto\x1a\x1erastervision/protos/task.proto\x1a!rastervision/protos/backend.proto\x1a\"rastervision/protos/analyzer.proto\x1a#rastervision/protos/evaluator.proto\"\xae\x03\n\x10\x45xperimentConfig\x12\n\n\x02id\x18\x01 \x02(\t\x12)\n\x07\x64\x61taset\x18\x02 \x02(\x0b\x32\x18.rv.protos.DatasetConfig\x12#\n\x04task\x18\x03 \x02(\x0b\x32\x15.rv.protos.TaskConfig\x12)\n\x07\x62\x61\x63kend\x18\x04 \x02(\x0b\x32\x18.rv.protos.BackendConfig\x12,\n\tanalyzers\x18\x05 \x03(\x0b\x32\x19.rv.protos.AnalyzerConfig\x12.\n\nevaluators\x18\x06 \x03(\x0b\x32\x1a.rv.protos.EvaluatorConfig\x12\x10\n\x08root_uri\x18\x07 \x02(\t\x12\x13\n\x0b\x61nalyze_uri\x18\x08 \x02(\t\x12\x10\n\x08\x63hip_uri\x18\t \x02(\t\x12\x11\n\ttrain_uri\x18\n \x02(\t\x12\x13\n\x0bpredict_uri\x18\x0b \x02(\t\x12\x10\n\x08\x65val_uri\x18\x0c \x02(\t\x12\x12\n\nbundle_uri\x18\r \x02(\t\x12.\n\rcustom_config\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,rastervision_dot_protos_dot_dataset__pb2.DESCRIPTOR,rastervision_dot_protos_dot_task__pb2.DESCRIPTOR,rastervision_dot_protos_dot_backend__pb2.DESCRIPTOR,rastervision_dot_protos_dot_analyzer__pb2.DESCRIPTOR,rastervision_dot_protos_dot_evaluator__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EXPERIMENTCONFIG = _descriptor.Descriptor(
  name='ExperimentConfig',
  full_name='rv.protos.ExperimentConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='rv.protos.ExperimentConfig.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='rv.protos.ExperimentConfig.dataset', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task', full_name='rv.protos.ExperimentConfig.task', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend', full_name='rv.protos.ExperimentConfig.backend', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analyzers', full_name='rv.protos.ExperimentConfig.analyzers', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluators', full_name='rv.protos.ExperimentConfig.evaluators', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root_uri', full_name='rv.protos.ExperimentConfig.root_uri', index=6,
      number=7, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analyze_uri', full_name='rv.protos.ExperimentConfig.analyze_uri', index=7,
      number=8, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_uri', full_name='rv.protos.ExperimentConfig.chip_uri', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_uri', full_name='rv.protos.ExperimentConfig.train_uri', index=9,
      number=10, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_uri', full_name='rv.protos.ExperimentConfig.predict_uri', index=10,
      number=11, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval_uri', full_name='rv.protos.ExperimentConfig.eval_uri', index=11,
      number=12, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_uri', full_name='rv.protos.ExperimentConfig.bundle_uri', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='custom_config', full_name='rv.protos.ExperimentConfig.custom_config', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=687,
)

_EXPERIMENTCONFIG.fields_by_name['dataset'].message_type = rastervision_dot_protos_dot_dataset__pb2._DATASETCONFIG
_EXPERIMENTCONFIG.fields_by_name['task'].message_type = rastervision_dot_protos_dot_task__pb2._TASKCONFIG
_EXPERIMENTCONFIG.fields_by_name['backend'].message_type = rastervision_dot_protos_dot_backend__pb2._BACKENDCONFIG
_EXPERIMENTCONFIG.fields_by_name['analyzers'].message_type = rastervision_dot_protos_dot_analyzer__pb2._ANALYZERCONFIG
_EXPERIMENTCONFIG.fields_by_name['evaluators'].message_type = rastervision_dot_protos_dot_evaluator__pb2._EVALUATORCONFIG
_EXPERIMENTCONFIG.fields_by_name['custom_config'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['ExperimentConfig'] = _EXPERIMENTCONFIG

ExperimentConfig = _reflection.GeneratedProtocolMessageType('ExperimentConfig', (_message.Message,), dict(
  DESCRIPTOR = _EXPERIMENTCONFIG,
  __module__ = 'rastervision.protos.experiment_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.ExperimentConfig)
  ))
_sym_db.RegisterMessage(ExperimentConfig)


# @@protoc_insertion_point(module_scope)

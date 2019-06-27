# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import Accessory
    from ._models_py3 import APIError, APIErrorException
    from ._models_py3 import ApplySnapshotRequest
    from ._models_py3 import Blur
    from ._models_py3 import Coordinate
    from ._models_py3 import DetectedFace
    from ._models_py3 import Emotion
    from ._models_py3 import Error
    from ._models_py3 import Exposure
    from ._models_py3 import FaceAttributes
    from ._models_py3 import FaceLandmarks
    from ._models_py3 import FaceList
    from ._models_py3 import FaceRectangle
    from ._models_py3 import FacialHair
    from ._models_py3 import FindSimilarRequest
    from ._models_py3 import GroupRequest
    from ._models_py3 import GroupResult
    from ._models_py3 import Hair
    from ._models_py3 import HairColor
    from ._models_py3 import HeadPose
    from ._models_py3 import IdentifyCandidate
    from ._models_py3 import IdentifyRequest
    from ._models_py3 import IdentifyResult
    from ._models_py3 import ImageUrl
    from ._models_py3 import LargeFaceList
    from ._models_py3 import LargePersonGroup
    from ._models_py3 import Makeup
    from ._models_py3 import MetaDataContract
    from ._models_py3 import NameAndUserDataContract
    from ._models_py3 import Noise
    from ._models_py3 import Occlusion
    from ._models_py3 import OperationStatus
    from ._models_py3 import PersistedFace
    from ._models_py3 import Person
    from ._models_py3 import PersonGroup
    from ._models_py3 import SimilarFace
    from ._models_py3 import Snapshot
    from ._models_py3 import TakeSnapshotRequest
    from ._models_py3 import TrainingStatus
    from ._models_py3 import UpdateFaceRequest
    from ._models_py3 import UpdateSnapshotRequest
    from ._models_py3 import VerifyFaceToFaceRequest
    from ._models_py3 import VerifyFaceToPersonRequest
    from ._models_py3 import VerifyResult
except (SyntaxError, ImportError):
    from ._models import Accessory
    from ._models import APIError, APIErrorException
    from ._models import ApplySnapshotRequest
    from ._models import Blur
    from ._models import Coordinate
    from ._models import DetectedFace
    from ._models import Emotion
    from ._models import Error
    from ._models import Exposure
    from ._models import FaceAttributes
    from ._models import FaceLandmarks
    from ._models import FaceList
    from ._models import FaceRectangle
    from ._models import FacialHair
    from ._models import FindSimilarRequest
    from ._models import GroupRequest
    from ._models import GroupResult
    from ._models import Hair
    from ._models import HairColor
    from ._models import HeadPose
    from ._models import IdentifyCandidate
    from ._models import IdentifyRequest
    from ._models import IdentifyResult
    from ._models import ImageUrl
    from ._models import LargeFaceList
    from ._models import LargePersonGroup
    from ._models import Makeup
    from ._models import MetaDataContract
    from ._models import NameAndUserDataContract
    from ._models import Noise
    from ._models import Occlusion
    from ._models import OperationStatus
    from ._models import PersistedFace
    from ._models import Person
    from ._models import PersonGroup
    from ._models import SimilarFace
    from ._models import Snapshot
    from ._models import TakeSnapshotRequest
    from ._models import TrainingStatus
    from ._models import UpdateFaceRequest
    from ._models import UpdateSnapshotRequest
    from ._models import VerifyFaceToFaceRequest
    from ._models import VerifyFaceToPersonRequest
    from ._models import VerifyResult
from ._face_client_enums import (
    AccessoryType,
    BlurLevel,
    DetectionModel,
    ExposureLevel,
    FaceAttributeType,
    FindSimilarMatchMode,
    Gender,
    GlassesType,
    HairColorType,
    NoiseLevel,
    OperationStatusType,
    RecognitionModel,
    SnapshotApplyMode,
    SnapshotObjectType,
    TrainingStatusType,
)

__all__ = [
    'Accessory',
    'APIError', 'APIErrorException',
    'ApplySnapshotRequest',
    'Blur',
    'Coordinate',
    'DetectedFace',
    'Emotion',
    'Error',
    'Exposure',
    'FaceAttributes',
    'FaceLandmarks',
    'FaceList',
    'FaceRectangle',
    'FacialHair',
    'FindSimilarRequest',
    'GroupRequest',
    'GroupResult',
    'Hair',
    'HairColor',
    'HeadPose',
    'IdentifyCandidate',
    'IdentifyRequest',
    'IdentifyResult',
    'ImageUrl',
    'LargeFaceList',
    'LargePersonGroup',
    'Makeup',
    'MetaDataContract',
    'NameAndUserDataContract',
    'Noise',
    'Occlusion',
    'OperationStatus',
    'PersistedFace',
    'Person',
    'PersonGroup',
    'SimilarFace',
    'Snapshot',
    'TakeSnapshotRequest',
    'TrainingStatus',
    'UpdateFaceRequest',
    'UpdateSnapshotRequest',
    'VerifyFaceToFaceRequest',
    'VerifyFaceToPersonRequest',
    'VerifyResult',
    'RecognitionModel',
    'Gender',
    'GlassesType',
    'HairColorType',
    'AccessoryType',
    'BlurLevel',
    'ExposureLevel',
    'NoiseLevel',
    'FindSimilarMatchMode',
    'TrainingStatusType',
    'SnapshotApplyMode',
    'SnapshotObjectType',
    'OperationStatusType',
    'FaceAttributeType',
    'DetectionModel',
]

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

from msrest.serialization import Model


class DetectedFace(Model):
    """Detected Face object.

    :param face_id:
    :type face_id: str
    :param face_rectangle:
    :type face_rectangle:
     ~azure.cognitiveservices.vision.face.models.FaceRectangle
    :param face_landmarks:
    :type face_landmarks:
     ~azure.cognitiveservices.vision.face.models.FaceLandmarks
    :param face_attributes:
    :type face_attributes:
     ~azure.cognitiveservices.vision.face.models.FaceAttributes
    """

    _validation = {
        'face_rectangle': {'required': True},
    }

    _attribute_map = {
        'face_id': {'key': 'faceId', 'type': 'str'},
        'face_rectangle': {'key': 'faceRectangle', 'type': 'FaceRectangle'},
        'face_landmarks': {'key': 'faceLandmarks', 'type': 'FaceLandmarks'},
        'face_attributes': {'key': 'faceAttributes', 'type': 'FaceAttributes'},
    }

    def __init__(self, face_rectangle, face_id=None, face_landmarks=None, face_attributes=None):
        super(DetectedFace, self).__init__()
        self.face_id = face_id
        self.face_rectangle = face_rectangle
        self.face_landmarks = face_landmarks
        self.face_attributes = face_attributes

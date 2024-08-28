# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AccessoryType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the accessory."""

    HEADWEAR = "headwear"
    """Head wear."""
    GLASSES = "glasses"
    """Glasses."""
    MASK = "mask"
    """Mask."""


class BlurLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates level of blurriness."""

    LOW = "low"
    """Low blur level."""
    MEDIUM = "medium"
    """Medium blur level."""
    HIGH = "high"
    """High blur level."""


class ExposureLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates level of exposure."""

    UNDER_EXPOSURE = "underExposure"
    """Low exposure level."""
    GOOD_EXPOSURE = "goodExposure"
    """Good exposure level."""
    OVER_EXPOSURE = "overExposure"
    """High exposure level."""


class FaceAttributeType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Available options for detect face with attribute."""

    HEAD_POSE = "headPose"
    """3-D roll/yaw/pitch angles for face direction."""
    GLASSES = "glasses"
    """Glasses type. Values include 'NoGlasses', 'ReadingGlasses', 'Sunglasses', 'SwimmingGoggles'."""
    OCCLUSION = "occlusion"
    """Whether each facial area is occluded, including forehead, eyes and mouth."""
    ACCESSORIES = "accessories"
    """Accessories around face, including 'headwear', 'glasses' and 'mask'. Empty array means no
    accessories detected. Note this is after a face is detected. Large mask could result in no face
    to be detected."""
    BLUR = "blur"
    """Face is blurry or not. Level returns 'Low', 'Medium' or 'High'. Value returns a number between
    [0,1], the larger the blurrier."""
    EXPOSURE = "exposure"
    """Face exposure level. Level returns 'GoodExposure', 'OverExposure' or 'UnderExposure'."""
    NOISE = "noise"
    """Noise level of face pixels. Level returns 'Low', 'Medium' and 'High'. Value returns a number
    between [0,1], the larger the noisier"""
    MASK = "mask"
    """Whether each face is wearing a mask. Mask type returns 'noMask', 'faceMask',
    'otherMaskOrOcclusion', or 'uncertain'. Value returns a boolean 'noseAndMouthCovered'
    indicating whether nose and mouth are covered."""
    QUALITY_FOR_RECOGNITION = "qualityForRecognition"
    """The overall image quality regarding whether the image being used in the detection is of
    sufficient quality to attempt face recognition on. The value is an informal rating of low,
    medium, or high. Only 'high' quality images are recommended for person enrollment and quality
    at or above 'medium' is recommended for identification scenarios. The attribute is only
    available when using recognition models recognition_03 or recognition_04."""
    AGE = "age"
    """Age in years."""
    SMILE = "smile"
    """Smile intensity, a number between [0,1]."""
    FACIAL_HAIR = "facialHair"
    """Properties describing facial hair attributes."""
    HAIR = "hair"
    """Properties describing hair attributes."""


class FaceDetectionModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The detection model for the face."""

    DETECTION_01 = "detection_01"
    """The default detection model. Recommend for near frontal face detection. For scenarios with
    exceptionally large angle (head-pose) faces, occluded faces or wrong image orientation, the
    faces in such cases may not be detected."""
    DETECTION_02 = "detection_02"
    """Detection model released in 2019 May with improved accuracy especially on small, side and
    blurry faces."""
    DETECTION_03 = "detection_03"
    """Detection model released in 2021 February with improved accuracy especially on small faces."""


class FaceImageType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The type of image."""

    COLOR = "Color"
    """Color image."""
    INFRARED = "Infrared"
    """Infrared image."""
    DEPTH = "Depth"
    """Depth image."""


class FaceLivenessDecision(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The outcome of the liveness classification."""

    UNCERTAIN = "uncertain"
    """The algorithm could not classify the target face as either real or spoof."""
    REAL_FACE = "realface"
    """The algorithm has classified the target face as real."""
    SPOOF_FACE = "spoofface"
    """The algorithm has classified the target face as a spoof."""


class FaceOperationStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The status of long running operation."""

    NOT_STARTED = "notStarted"
    """The operation is not started."""
    RUNNING = "running"
    """The operation is still running."""
    SUCCEEDED = "succeeded"
    """The operation is succeeded."""
    FAILED = "failed"
    """The operation is failed."""


class FaceRecognitionModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The recognition model for the face."""

    RECOGNITION_01 = "recognition_01"
    """The default recognition model for "Detect". All those faceIds created before 2019 March are
    bonded with this recognition model."""
    RECOGNITION_02 = "recognition_02"
    """Recognition model released in 2019 March."""
    RECOGNITION_03 = "recognition_03"
    """Recognition model released in 2020 May."""
    RECOGNITION_04 = "recognition_04"
    """Recognition model released in 2021 February. It's recommended to use this recognition model for
    better recognition accuracy."""


class FaceSessionStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current status of the session."""

    NOT_STARTED = "NotStarted"
    """Session has not started."""
    STARTED = "Started"
    """Session has started."""
    RESULT_AVAILABLE = "ResultAvailable"
    """Session has available result."""


class FindSimilarMatchMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Similar face searching mode."""

    MATCH_PERSON = "matchPerson"
    """Match person."""
    MATCH_FACE = "matchFace"
    """Match face."""


class GlassesType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Glasses type of the face."""

    NO_GLASSES = "noGlasses"
    """No glasses on the face."""
    READING_GLASSES = "readingGlasses"
    """Normal glasses on the face."""
    SUNGLASSES = "sunglasses"
    """Sunglasses on the face."""
    SWIMMING_GOGGLES = "swimmingGoggles"
    """Swimming goggles on the face."""


class HairColorType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Name of the hair color."""

    UNKNOWN_HAIR_COLOR = "unknown"
    """Unknown."""
    WHITE = "white"
    """White."""
    GRAY = "gray"
    """Gray."""
    BLOND = "blond"
    """Blond."""
    BROWN = "brown"
    """Brown."""
    RED = "red"
    """Red."""
    BLACK = "black"
    """Black."""
    OTHER = "other"
    """Other."""


class LivenessModel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The model version used for liveness classification."""

    V2022_10_15_PREVIEW_04 = "2022-10-15-preview.04"
    V2023_12_20_PREVIEW_06 = "2023-12-20-preview.06"


class LivenessOperationMode(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The liveness operation mode to drive the client's end-user experience."""

    PASSIVE = "Passive"
    """Utilizes a passive liveness technique that requires no additional actions from the user.
    Requires normal indoor lighting and high screen brightness for optimal performance. And thus,
    this mode has a narrow operational envelope and will not be suitable for scenarios that
    requires the end-user's to be in bright lighting conditions. Note: this is the only supported
    mode for the Mobile (iOS and Android) solution."""
    PASSIVE_ACTIVE = "PassiveActive"
    """This mode utilizes a hybrid passive or active liveness technique that necessitates user
    cooperation. It is optimized to require active motion only under suboptimal lighting
    conditions. Unlike the passive mode, this mode has no lighting restrictions, and thus offering
    a broader operational envelope. This mode is preferable on Web based solutions due to the lack
    of automatic screen brightness control available on browsers which hinders the Passive mode's
    operational envelope on Web based solutions."""


class MaskType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Type of the mask."""

    FACE_MASK = "faceMask"
    """Face mask."""
    NO_MASK = "noMask"
    """No mask."""
    OTHER_MASK_OR_OCCLUSION = "otherMaskOrOcclusion"
    """Other types of mask or occlusion."""
    UNCERTAIN = "uncertain"
    """Uncertain."""


class NoiseLevel(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates level of noise."""

    LOW = "low"
    """Low noise level."""
    MEDIUM = "medium"
    """Medium noise level."""
    HIGH = "high"
    """High noise level."""


class QualityForRecognition(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates quality of image for recognition."""

    LOW = "low"
    """Low quality."""
    MEDIUM = "medium"
    """Medium quality."""
    HIGH = "high"
    """High quality."""


class Versions(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """API versions for Azure AI Face API."""

    V1_1_PREVIEW_1 = "v1.1-preview.1"
    """v1.1-preview.1"""
    V1_2_PREVIEW_1 = "v1.2-preview.1"
    """v1.2-preview.1"""

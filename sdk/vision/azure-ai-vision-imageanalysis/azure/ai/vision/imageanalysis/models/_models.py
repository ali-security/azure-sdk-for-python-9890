# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, List, Mapping, Optional, TYPE_CHECKING, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class CaptionResult(_model_base.Model):
    """Represents a generated phrase that describes the content of the whole image.


    :ivar confidence: A score, in the range of 0 to 1 (inclusive), representing the confidence that
     this description is accurate.
     Higher values indicating higher confidence. Required.
    :vartype confidence: float
    :ivar text: The text of the caption. Required.
    :vartype text: str
    """

    confidence: float = rest_field()
    """A score, in the range of 0 to 1 (inclusive), representing the confidence that this description
     is accurate.
     Higher values indicating higher confidence. Required."""
    text: str = rest_field()
    """The text of the caption. Required."""

    @overload
    def __init__(
        self,
        *,
        confidence: float,
        text: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class CropRegion(_model_base.Model):
    """A region at the desired aspect ratio that can be used as image thumbnail.
    The region preserves as much content as possible from the analyzed image, with priority given
    to detected faces.


    :ivar aspect_ratio: The aspect ratio of the crop region.
     Aspect ratio is calculated by dividing the width of the region in pixels by its height in
     pixels.
     The aspect ratio will be in the range 0.75 to 1.8 (inclusive) if provided by the developer
     during the analyze call.
     Otherwise, it will be in the range 0.5 to 2.0 (inclusive). Required.
    :vartype aspect_ratio: float
    :ivar bounding_box: The bounding box of the region. Required.
    :vartype bounding_box: ~azure.ai.vision.imageanalysis.models.ImageBoundingBox
    """

    aspect_ratio: float = rest_field(name="aspectRatio")
    """The aspect ratio of the crop region.
     Aspect ratio is calculated by dividing the width of the region in pixels by its height in
     pixels.
     The aspect ratio will be in the range 0.75 to 1.8 (inclusive) if provided by the developer
     during the analyze call.
     Otherwise, it will be in the range 0.5 to 2.0 (inclusive). Required."""
    bounding_box: "_models.ImageBoundingBox" = rest_field(name="boundingBox")
    """The bounding box of the region. Required."""

    @overload
    def __init__(
        self,
        *,
        aspect_ratio: float,
        bounding_box: "_models.ImageBoundingBox",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DenseCaption(_model_base.Model):
    """Represents a generated phrase that describes the content of the whole image or a region in the
    image.


    :ivar confidence: A score, in the range of 0 to 1 (inclusive), representing the confidence that
     this description is accurate.
     Higher values indicating higher confidence. Required.
    :vartype confidence: float
    :ivar text: The text of the caption. Required.
    :vartype text: str
    :ivar bounding_box: The image region of which this caption applies. Required.
    :vartype bounding_box: ~azure.ai.vision.imageanalysis.models.ImageBoundingBox
    """

    confidence: float = rest_field()
    """A score, in the range of 0 to 1 (inclusive), representing the confidence that this description
     is accurate.
     Higher values indicating higher confidence. Required."""
    text: str = rest_field()
    """The text of the caption. Required."""
    bounding_box: "_models.ImageBoundingBox" = rest_field(name="boundingBox")
    """The image region of which this caption applies. Required."""

    @overload
    def __init__(
        self,
        *,
        confidence: float,
        text: str,
        bounding_box: "_models.ImageBoundingBox",
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DenseCaptionsResult(_model_base.Model):
    """Represents a list of up to 10 image captions for different regions of the image.
    The first caption always applies to the whole image.


    :ivar list: The list of image captions. Required.
    :vartype list: list[~azure.ai.vision.imageanalysis.models.DenseCaption]
    """

    list: List["_models.DenseCaption"] = rest_field(name="values")
    """The list of image captions. Required."""

    @overload
    def __init__(
        self,
        *,
        list: List["_models.DenseCaption"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DetectedObject(_model_base.Model):
    """Represents a physical object detected in an image.


    :ivar bounding_box: A rectangular boundary where the object was detected. Required.
    :vartype bounding_box: ~azure.ai.vision.imageanalysis.models.ImageBoundingBox
    :ivar tags: A single-item list containing the object information. Required.
    :vartype tags: list[~azure.ai.vision.imageanalysis.models.DetectedTag]
    """

    bounding_box: "_models.ImageBoundingBox" = rest_field(name="boundingBox")
    """A rectangular boundary where the object was detected. Required."""
    tags: List["_models.DetectedTag"] = rest_field()
    """A single-item list containing the object information. Required."""

    @overload
    def __init__(
        self,
        *,
        bounding_box: "_models.ImageBoundingBox",
        tags: List["_models.DetectedTag"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DetectedPerson(_model_base.Model):
    """Represents a person detected in an image.

    Readonly variables are only populated by the server, and will be ignored when sending a request.


    :ivar bounding_box: A rectangular boundary where the person was detected. Required.
    :vartype bounding_box: ~azure.ai.vision.imageanalysis.models.ImageBoundingBox
    :ivar confidence: A score, in the range of 0 to 1 (inclusive), representing the confidence that
     this detection was accurate.
     Higher values indicating higher confidence. Required.
    :vartype confidence: float
    """

    bounding_box: "_models.ImageBoundingBox" = rest_field(name="boundingBox", visibility=["read"])
    """A rectangular boundary where the person was detected. Required."""
    confidence: float = rest_field(visibility=["read"])
    """A score, in the range of 0 to 1 (inclusive), representing the confidence that this detection
     was accurate.
     Higher values indicating higher confidence. Required."""


class DetectedTag(_model_base.Model):
    """A content entity observation in the image. A tag can be a physical object, living being,
    scenery, or action
    that appear in the image.


    :ivar confidence: A score, in the range of 0 to 1 (inclusive), representing the confidence that
     this entity was observed.
     Higher values indicating higher confidence. Required.
    :vartype confidence: float
    :ivar name: Name of the entity. Required.
    :vartype name: str
    """

    confidence: float = rest_field()
    """A score, in the range of 0 to 1 (inclusive), representing the confidence that this entity was
     observed.
     Higher values indicating higher confidence. Required."""
    name: str = rest_field()
    """Name of the entity. Required."""

    @overload
    def __init__(
        self,
        *,
        confidence: float,
        name: str,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DetectedTextBlock(_model_base.Model):
    """Represents a single block of detected text in the image.


    :ivar lines: A list of text lines in this block. Required.
    :vartype lines: list[~azure.ai.vision.imageanalysis.models.DetectedTextLine]
    """

    lines: List["_models.DetectedTextLine"] = rest_field()
    """A list of text lines in this block. Required."""

    @overload
    def __init__(
        self,
        *,
        lines: List["_models.DetectedTextLine"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DetectedTextLine(_model_base.Model):
    """Represents a single line of text in the image.


    :ivar text: Text content of the detected text line. Required.
    :vartype text: str
    :ivar bounding_polygon: A bounding polygon around the text line. At the moment only
     quadrilaterals are supported (represented by 4 image points). Required.
    :vartype bounding_polygon: list[~azure.ai.vision.imageanalysis.models.ImagePoint]
    :ivar words: A list of words in this line. Required.
    :vartype words: list[~azure.ai.vision.imageanalysis.models.DetectedTextWord]
    """

    text: str = rest_field()
    """Text content of the detected text line. Required."""
    bounding_polygon: List["_models.ImagePoint"] = rest_field(name="boundingPolygon")
    """A bounding polygon around the text line. At the moment only quadrilaterals are supported
     (represented by 4 image points). Required."""
    words: List["_models.DetectedTextWord"] = rest_field()
    """A list of words in this line. Required."""

    @overload
    def __init__(
        self,
        *,
        text: str,
        bounding_polygon: List["_models.ImagePoint"],
        words: List["_models.DetectedTextWord"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DetectedTextWord(_model_base.Model):
    """A word object consisting of a contiguous sequence of characters. For non-space delimited
    languages,
    such as Chinese, Japanese, and Korean, each character is represented as its own word.


    :ivar text: Text content of the word. Required.
    :vartype text: str
    :ivar bounding_polygon: A bounding polygon around the word. At the moment only quadrilaterals
     are supported (represented by 4 image points). Required.
    :vartype bounding_polygon: list[~azure.ai.vision.imageanalysis.models.ImagePoint]
    :ivar confidence: The level of confidence that the word was detected. Confidence scores span
     the range of 0.0 to 1.0 (inclusive), with higher values indicating a higher confidence of
     detection. Required.
    :vartype confidence: float
    """

    text: str = rest_field()
    """Text content of the word. Required."""
    bounding_polygon: List["_models.ImagePoint"] = rest_field(name="boundingPolygon")
    """A bounding polygon around the word. At the moment only quadrilaterals are supported
     (represented by 4 image points). Required."""
    confidence: float = rest_field()
    """The level of confidence that the word was detected. Confidence scores span the range of 0.0 to
     1.0 (inclusive), with higher values indicating a higher confidence of detection. Required."""

    @overload
    def __init__(
        self,
        *,
        text: str,
        bounding_polygon: List["_models.ImagePoint"],
        confidence: float,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ImageAnalysisResult(_model_base.Model):
    """Represents the outcome of an Image Analysis operation.


    :ivar caption: The generated phrase that describes the content of the analyzed image.
    :vartype caption: ~azure.ai.vision.imageanalysis.models.CaptionResult
    :ivar dense_captions: The up to 10 generated phrases, the first describing the content of the
     whole image,
     and the others describing the content of different regions of the image.
    :vartype dense_captions: ~azure.ai.vision.imageanalysis.models.DenseCaptionsResult
    :ivar metadata: Metadata associated with the analyzed image. Required.
    :vartype metadata: ~azure.ai.vision.imageanalysis.models.ImageMetadata
    :ivar model_version: The cloud AI model used for the analysis. Required.
    :vartype model_version: str
    :ivar objects: A list of detected physical objects in the analyzed image, and their location.
    :vartype objects: ~azure.ai.vision.imageanalysis.models.ObjectsResult
    :ivar people: A list of detected people in the analyzed image, and their location.
    :vartype people: ~azure.ai.vision.imageanalysis.models.PeopleResult
    :ivar read: The extracted printed and hand-written text in the analyze image. Also knows as
     OCR.
    :vartype read: ~azure.ai.vision.imageanalysis.models.ReadResult
    :ivar smart_crops: A list of crop regions at the desired as aspect ratios (if provided) that
     can be used as image thumbnails.
     These regions preserve as much content as possible from the analyzed image, with priority
     given to detected faces.
    :vartype smart_crops: ~azure.ai.vision.imageanalysis.models.SmartCropsResult
    :ivar tags: A list of content tags in the analyzed image.
    :vartype tags: ~azure.ai.vision.imageanalysis.models.TagsResult
    """

    caption: Optional["_models.CaptionResult"] = rest_field(name="captionResult")
    """The generated phrase that describes the content of the analyzed image."""
    dense_captions: Optional["_models.DenseCaptionsResult"] = rest_field(name="denseCaptionsResult")
    """The up to 10 generated phrases, the first describing the content of the whole image,
     and the others describing the content of different regions of the image."""
    metadata: "_models.ImageMetadata" = rest_field()
    """Metadata associated with the analyzed image. Required."""
    model_version: str = rest_field(name="modelVersion")
    """The cloud AI model used for the analysis. Required."""
    objects: Optional["_models.ObjectsResult"] = rest_field(name="objectsResult")
    """A list of detected physical objects in the analyzed image, and their location."""
    people: Optional["_models.PeopleResult"] = rest_field(name="peopleResult")
    """A list of detected people in the analyzed image, and their location."""
    read: Optional["_models.ReadResult"] = rest_field(name="readResult")
    """The extracted printed and hand-written text in the analyze image. Also knows as OCR."""
    smart_crops: Optional["_models.SmartCropsResult"] = rest_field(name="smartCropsResult")
    """A list of crop regions at the desired as aspect ratios (if provided) that can be used as image
     thumbnails.
     These regions preserve as much content as possible from the analyzed image, with priority given
     to detected faces."""
    tags: Optional["_models.TagsResult"] = rest_field(name="tagsResult")
    """A list of content tags in the analyzed image."""

    @overload
    def __init__(
        self,
        *,
        metadata: "_models.ImageMetadata",
        model_version: str,
        caption: Optional["_models.CaptionResult"] = None,
        dense_captions: Optional["_models.DenseCaptionsResult"] = None,
        objects: Optional["_models.ObjectsResult"] = None,
        people: Optional["_models.PeopleResult"] = None,
        read: Optional["_models.ReadResult"] = None,
        smart_crops: Optional["_models.SmartCropsResult"] = None,
        tags: Optional["_models.TagsResult"] = None,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ImageBoundingBox(_model_base.Model):
    """A basic rectangle specifying a sub-region of the image.


    :ivar x: X-coordinate of the top left point of the area, in pixels. Required.
    :vartype x: int
    :ivar y: Y-coordinate of the top left point of the area, in pixels. Required.
    :vartype y: int
    :ivar width: Width of the area, in pixels. Required.
    :vartype width: int
    :ivar height: Height of the area, in pixels. Required.
    :vartype height: int
    """

    x: int = rest_field()
    """X-coordinate of the top left point of the area, in pixels. Required."""
    y: int = rest_field()
    """Y-coordinate of the top left point of the area, in pixels. Required."""
    width: int = rest_field(name="w")
    """Width of the area, in pixels. Required."""
    height: int = rest_field(name="h")
    """Height of the area, in pixels. Required."""

    @overload
    def __init__(
        self,
        *,
        x: int,
        y: int,
        width: int,
        height: int,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ImageMetadata(_model_base.Model):
    """Metadata associated with the analyzed image.


    :ivar height: The height of the image in pixels. Required.
    :vartype height: int
    :ivar width: The width of the image in pixels. Required.
    :vartype width: int
    """

    height: int = rest_field()
    """The height of the image in pixels. Required."""
    width: int = rest_field()
    """The width of the image in pixels. Required."""

    @overload
    def __init__(
        self,
        *,
        height: int,
        width: int,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ImagePoint(_model_base.Model):
    """Represents the coordinates of a single pixel in the image.


    :ivar x: The horizontal x-coordinate of this point, in pixels. Zero values corresponds to the
     left-most pixels in the image. Required.
    :vartype x: int
    :ivar y: The vertical y-coordinate of this point, in pixels. Zero values corresponds to the
     top-most pixels in the image. Required.
    :vartype y: int
    """

    x: int = rest_field()
    """The horizontal x-coordinate of this point, in pixels. Zero values corresponds to the left-most
     pixels in the image. Required."""
    y: int = rest_field()
    """The vertical y-coordinate of this point, in pixels. Zero values corresponds to the top-most
     pixels in the image. Required."""

    @overload
    def __init__(
        self,
        *,
        x: int,
        y: int,
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ImageUrl(_model_base.Model):
    """An object holding the publicly reachable URL of an image to analyze.

    All required parameters must be populated in order to send to server.

    :ivar url: Publicly reachable URL of an image to analyze. Required.
    :vartype url: str
    """

    url: str = rest_field()
    """Publicly reachable URL of an image to analyze. Required."""


class ObjectsResult(_model_base.Model):
    """Represents a list of physical object detected in an image and their location.


    :ivar list: A list of physical object detected in an image and their location. Required.
    :vartype list: list[~azure.ai.vision.imageanalysis.models.DetectedObject]
    """

    list: List["_models.DetectedObject"] = rest_field(name="values")
    """A list of physical object detected in an image and their location. Required."""

    @overload
    def __init__(
        self,
        *,
        list: List["_models.DetectedObject"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PeopleResult(_model_base.Model):
    """Represents a list of people detected in an image and their location.


    :ivar list: A list of people detected in an image and their location. Required.
    :vartype list: list[~azure.ai.vision.imageanalysis.models.DetectedPerson]
    """

    list: List["_models.DetectedPerson"] = rest_field(name="values")
    """A list of people detected in an image and their location. Required."""

    @overload
    def __init__(
        self,
        *,
        list: List["_models.DetectedPerson"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ReadResult(_model_base.Model):
    """The results of a Read (OCR) operation.


    :ivar blocks: A list of text blocks in the image. At the moment only one block is returned,
     containing all the text detected in the image. Required.
    :vartype blocks: list[~azure.ai.vision.imageanalysis.models.DetectedTextBlock]
    """

    blocks: List["_models.DetectedTextBlock"] = rest_field()
    """A list of text blocks in the image. At the moment only one block is returned, containing all
     the text detected in the image. Required."""

    @overload
    def __init__(
        self,
        *,
        blocks: List["_models.DetectedTextBlock"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class SmartCropsResult(_model_base.Model):
    """Smart cropping result. A list of crop regions at the desired as aspect ratios (if provided)
    that can be used as image thumbnails.
    These regions preserve as much content as possible from the analyzed image, with priority given
    to detected faces.


    :ivar list: A list of crop regions. Required.
    :vartype list: list[~azure.ai.vision.imageanalysis.models.CropRegion]
    """

    list: List["_models.CropRegion"] = rest_field(name="values")
    """A list of crop regions. Required."""

    @overload
    def __init__(
        self,
        *,
        list: List["_models.CropRegion"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class TagsResult(_model_base.Model):
    """A list of entities observed in the image. Tags can be physical objects, living being, scenery,
    or actions
    that appear in the image.


    :ivar list: A list of tags. Required.
    :vartype list: list[~azure.ai.vision.imageanalysis.models.DetectedTag]
    """

    list: List["_models.DetectedTag"] = rest_field(name="values")
    """A list of tags. Required."""

    @overload
    def __init__(
        self,
        *,
        list: List["_models.DetectedTag"],
    ): ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)

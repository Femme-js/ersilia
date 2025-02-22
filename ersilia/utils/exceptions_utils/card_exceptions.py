from .exceptions import ErsiliaError
from ...default import AIRTABLE_MODEL_HUB_VIEW_URL

import os


def _read_default_fields(field):
    root = os.path.dirname(os.path.abspath(__file__))
    filename = field.lower().replace(" ", "_")
    file_path = os.path.join(
        root, "..", "..", "hub", "content", "metadata", filename + ".txt"
    )
    with open(file_path, "r") as f:
        valid_field = f.read().split("\n")
    return valid_field


class CardErsiliaError(ErsiliaError):
    def __init__(self):
        self.message = "Error occured while running card command"
        self.hints = ""
        super().__init__(self.message, self.hints)


class BaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia model information\n"
        self.hints = "Please check Ersilia AirTable to make sure you are providing the right information. This is the AirTable link: {0}".format(
            AIRTABLE_MODEL_HUB_VIEW_URL
        )
        super().__init__(self.message, self.hints)


class IdentifierBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia model identifier"
        self.hints = "Ersilia model identifiers are 7 alphanumeric characters. They always start with eos, followed by a digit. The eos identifier coincides with the name of the repository. Check our current AirTable to see correct identifiers: {0}".format(
            AIRTABLE_MODEL_HUB_VIEW_URL
        )
        super().__init__(self.message, self.hints)


class SlugBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia slug"
        self.hints = "Slug must be a 5-60 chars lowercase single-word unique identifier. Use '-' for linking words if necessary"
        super().__init__(self.message, self.hints)


class StatusBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia status"
        self.hints = "Only one of the following status is allowed: {}".format(
            ", ".join(_read_default_fields("Status"))
        )
        super().__init__(self.message, self.hints)


class TitleBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia title"
        self.hints = "Title must be a 1 sentence (10 to 300 chars)"
        super().__init__(self.message, self.hints)


class DescriptionBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia description"
        self.hints = "Description must be longer than 200 characters and different from the title"
        super().__init__(self.message, self.hints)


class ModeBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia mode"
        self.hints = "Only one of the following modes is allowed: {}".format(
            ", ".join(_read_default_fields("Mode"))
        )
        super().__init__(self.message, self.hints)


class TaskBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia model task"
        self.hints = "Only tasks allowed: {}. Tasks must be in list format".format(
            ", ".join(_read_default_fields("Task"))
        )
        super().__init__(self.message, self.hints)


class InputBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia input"
        self.hints = "Only inputs allowed: {}. Input must be in list format".format(
            ", ".join(_read_default_fields("Input"))
        )
        super().__init__(self.message, self.hints)


class InputShapeBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia input shape"
        self.hints = "Only one of the following shapes is allowed: {}".format(
            ", ".join(_read_default_fields("Input Shape"))
        )
        super().__init__(self.message, self.hints)


class OutputBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia output"
        self.hints = "Only one of the following outputs is allowed: {}".format(
            ", ".join(_read_default_fields("Output"))
        )
        super().__init__(self.message, self.hints)


class OutputTypeBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia output type"
        self.hints = "Only output types allowed: {}. More than one output type can be added in list format".format(
            ", ".join(_read_default_fields("Output Type"))
        )
        super().__init__(self.message, self.hints)


class OutputShapeBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia output shape"
        self.hints = "Only one of the following output shapes is allowed: {}".format(
            ", ".join(_read_default_fields("Output Shape"))
        )
        super().__init__(self.message, self.hints)


class TagBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia model tag"
        self.hints = "Tags must be in list format and they must be accepted our team. This means that only tags that are already available in Ersilia are allowed. If you want to include a new tag, please open a pull request (PR) on the 'tag.txt' file from the Ersilia repository."
        super().__init__(self.message, self.hints)


class LicenseBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong license"
        self.hints = "Listed licenses are: {}. If the model has a license not in this list, please open a PR on the 'license.txt' file in the Ersilia repository".format(
            ", ".join(_read_default_fields("License"))
        )
        super().__init__(self.message, self.hints)


class GithubBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Wrong Ersilia GitHub URL"
        self.hints = "The model does not seem to be publicly available in Ersilia's GitHub organization profile (ersilia-os). Make sure that a model identifier has been set."
        super().__init__(self.message, self.hints)


class BothIdentifiersBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Both identifiers field error"
        self.hints = "Ersilia model identifier and/or slug have not been set yet"
        super().__init__(self.message, self.hints)


class PublicationBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Publication field error"
        self.hints = "Publication must be a valid URL"
        super().__init__(self.message, self.hints)


class SourceCodeBaseInformationError(ErsiliaError):
    def __init__(self):
        self.message = "Source Code field error"
        self.hints = "Source Code must be a valid URL"
        super().__init__(self.message, self.hints)

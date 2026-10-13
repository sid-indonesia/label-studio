import re

from django.http import JsonResponse

_IMPORT_PATH = re.compile(r"^/api/projects/\d+/(re)?import/?$")


class DisableFileUploadMiddleware:
    """Blocks local file uploads from the Label Studio UI.

    Cloud storage sync (/api/storages/*) is unaffected, so projects can still
    pull images from S3-compatible buckets.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        content_type = request.META.get("CONTENT_TYPE", "")
        if (
            request.method == "POST"
            and _IMPORT_PATH.match(request.path)
            and content_type.startswith("multipart/form-data")
        ):
            return JsonResponse(
                {
                    "detail": (
                        "Direct file upload is disabled on this instance. "
                        "Import data through a configured cloud storage source."
                    )
                },
                status=403,
            )
        return self.get_response(request)

FROM heartexlabs/label-studio:latest

USER root

# Middleware that rejects file uploads via the UI (/api/projects/<id>/import
# and /reimport). Cloud-storage sync uses /api/storages/* and keeps working.
COPY disable_uploads.py /label-studio/label_studio/core/disable_uploads.py

# Register the middleware by appending it to the active settings module.
RUN echo "" >> /label-studio/label_studio/core/settings/label_studio.py \
 && echo "MIDDLEWARE = list(MIDDLEWARE) + ['core.disable_uploads.DisableFileUploadMiddleware']" \
      >> /label-studio/label_studio/core/settings/label_studio.py

USER 1001

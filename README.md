# Label Studio local stack

This Compose stack runs Label Studio with PostgreSQL 18 Alpine and a local S3-compatible RustFS server. Local file serving is disabled; use a Label Studio S3 import storage pointing at RustFS for test data.

```sh
cp .env.example .env
# Edit .env and replace every placeholder.
docker compose up -d
```

Open Label Studio at <http://localhost:8080> and the RustFS console at <http://localhost:9001>. The S3 endpoint is <http://localhost:9000>. The `rustfs-init` one-shot service creates the `label-studio` bucket before Label Studio starts.

For an S3 import storage inside Label Studio, use:

- Endpoint: `http://rustfs:9000` (from the Label Studio container)
- Bucket: `label-studio`
- Region: `us-east-1`
- Access key and secret: the values from `.env`

The defaults in `compose.yaml` are intentionally development-only. Keep `.env` out of version control and use Secret Manager or platform secrets for production.

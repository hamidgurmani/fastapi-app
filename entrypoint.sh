#!/bin/sh
set -e

echo "Starting FastAPI application..."

# Optional: DB check (extra safety)
python - <<EOF
from app.database import check_db
check_db()
EOF

exec "$@"


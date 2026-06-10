"""Dev-only Django settings for running inside an Ona environment.

The project's ALLOWED_HOSTS is empty, so Django rejects requests that arrive
through Ona's exposed-port domain (<port>--<environment-id>.<runner-domain>).
This shim reuses the project settings and relaxes the host allowlist for local
development only. It is activated solely by the dev-server automation via
DJANGO_SETTINGS_MODULE and is never imported by the application itself.
"""

from config.settings import *  # noqa: F401,F403

ALLOWED_HOSTS = ["*"]

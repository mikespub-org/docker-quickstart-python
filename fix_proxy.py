import os

from werkzeug.middleware.proxy_fix import ProxyFix

# See https://werkzeug.palletsprojects.com/en/2.0.x/middleware/proxy_fix/
# Adjust the WSGI environ based on X-Forwarded- that proxies in front of the application may set.
#     X-Forwarded-For sets REMOTE_ADDR.
#     X-Forwarded-Proto sets wsgi.url_scheme.
#     X-Forwarded-Host sets HTTP_HOST, SERVER_NAME, and SERVER_PORT.
#     X-Forwarded-Port sets HTTP_HOST and SERVER_PORT.
#     X-Forwarded-Prefix sets SCRIPT_NAME.
# You must tell the middleware how many proxies set each header so it knows what values to trust.
# app = ProxyFix(app, x_for=1, x_proto=1, x_host=0, x_port=0, x_prefix=0)


# Wrapping app.wsgi_app instead of app means that app still points at your Flask application, not at the middleware.
def add_wsgi_proxy(wsgi_app):
    if not os.getenv("PROXY_FIX", 0):
        return wsgi_app
    # Use same defaults as ProxyFix here
    return ProxyFix(
        wsgi_app,
        x_for=int(os.getenv("PROXY_FIX_FOR", 1)),
        x_proto=int(os.getenv("PROXY_FIX_PROTO", 1)),
        x_host=int(os.getenv("PROXY_FIX_HOST", 0)),
        x_port=int(os.getenv("PROXY_FIX_PORT", 0)),
        x_prefix=int(os.getenv("PROXY_FIX_PREFIX", 0)),
    )

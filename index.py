# -*- coding: utf8 -*-
import requests
from urllib import parse


def handler(environ, start_response):
    # print(environ)
    headers = {}
    for k, v in environ.items():
        if k in ["HTTP_HOST", "HTTP_X_FORWARDED_PROTO", "HTTP_X_FC_FUNCTION_HANDLER", "HTTP_X_FC_URL"]:
            continue
        if k.startswith("HTTP_"):
            headers[k.lstrip("HTTP_")] = v

    url = environ.get("HTTP_X_FC_URL", "") or parse.parse_qs(environ['QUERY_STRING']).get("url", [""])[0]
    if not url:
        start_response('200 OK', [('Content-type', 'text/plain')])
        return [b"no target"]

    length = int(environ.get("CONTENT_LENGTH", 0))
    data = b''
    if length:
        data = environ["wsgi.input"].read(length)

    try:
        r = requests.request(environ["REQUEST_METHOD"], url, headers=headers, data=data, verify=False)
        status = f"{r.status_code} {r.reason}"
        response_headers = [(k, v) for k, v in r.headers.items()]
        start_response(status, response_headers)
        return [r.content]
    except Exception as e:
        start_response('200 OK', [('Content-type', 'text/plain')])
        return [str(e).encode()]


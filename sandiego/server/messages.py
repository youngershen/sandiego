# -*- coding:utf-8 -*-
# PROJECT_NAME : sandiego
# AUTHOR       : younger shen
# EMAIL        : younger.x.shen@gmail.com

from sandiego.i18n import ugettext as _

HTTPMESSAGE_100 = _("Continue")
HTTPMESSAGE_101 = _("Switching Protocols")

HTTPMESSAGE_200 = _("OK")
HTTPMESSAGE_201 = _("Created")
HTTPMESSAGE_202 = _("Accepted")
HTTPMESSAGE_203 = _("Non-Authoritative Information")
HTTPMESSAGE_204 = _("No Content")
HTTPMESSAGE_205 = _("Reset Content")
HTTPMESSAGE_206 = _("Partial Content")

HTTPMESSAGE_300 = _("Multiple Choices")
HTTPMESSAGE_301 = _("Moved Permanently")
HTTPMESSAGE_302 = _("Found")
HTTPMESSAGE_303 = _("See Other")
HTTPMESSAGE_304 = _("Not Modified")
HTTPMESSAGE_305 = _("Use Proxy")
HTTPMESSAGE_306 = _("Unused")
HTTPMESSAGE_307 = _("Temporary Redirect")

HTTPMESSAGE_400 = _("Bad Request")
HTTPMESSAGE_401 = _("Unauthorized")
HTTPMESSAGE_402 = _("Payment Required")
HTTPMESSAGE_403 = _("Forbidden")
HTTPMESSAGE_404 = _("Not Found")
HTTPMESSAGE_405 = _("Method Not Allowed")
HTTPMESSAGE_406 = _("Not Acceptable")
HTTPMESSAGE_407 = _("Proxy Authentication Required")
HTTPMESSAGE_408 = _("Request Timeout")
HTTPMESSAGE_409 = _("Conflict")
HTTPMESSAGE_410 = _("Gone")
HTTPMESSAGE_411 = _("Length Required")
HTTPMESSAGE_412 = _("Precondition Failed")
HTTPMESSAGE_413 = _("Request Entity Too Large")
HTTPMESSAGE_414 = _("Request-URI Too Long")
HTTPMESSAGE_415 = _("Unsupported Media Type")
HTTPMESSAGE_416 = _("Requested Range Not Satisfiable")
HTTPMESSAGE_417 = _("Expectation Failed")

HTTPMESSAGE_500 = _("Internal Server Error")
HTTPMESSAGE_501 = _("Not Implemented")
HTTPMESSAGE_502 = _("Bad Gateway")
HTTPMESSAGE_503 = _("Service Unavailable")
HTTPMESSAGE_504 = _("Gateway Timeout")
HTTPMESSAGE_505 = _("HTTP Version Not Supported")

HTTPMESSAGES = {
    100: HTTPMESSAGE_100,
    101: HTTPMESSAGE_101,

    200: HTTPMESSAGE_200,
    201: HTTPMESSAGE_201,
    202: HTTPMESSAGE_202,
    203: HTTPMESSAGE_203,
    204: HTTPMESSAGE_204,
    205: HTTPMESSAGE_205,
    206: HTTPMESSAGE_206,

    300: HTTPMESSAGE_300,
    301: HTTPMESSAGE_301,
    302: HTTPMESSAGE_302,
    303: HTTPMESSAGE_303,
    304: HTTPMESSAGE_304,
    305: HTTPMESSAGE_305,
    306: HTTPMESSAGE_306,
    307: HTTPMESSAGE_307,

    400: HTTPMESSAGE_400,
    401: HTTPMESSAGE_401,
    402: HTTPMESSAGE_402,
    403: HTTPMESSAGE_403,
    404: HTTPMESSAGE_404,
    405: HTTPMESSAGE_405,
    406: HTTPMESSAGE_406,
    407: HTTPMESSAGE_407,
    408: HTTPMESSAGE_408,
    409: HTTPMESSAGE_409,
    410: HTTPMESSAGE_410,
    411: HTTPMESSAGE_411,
    412: HTTPMESSAGE_412,
    413: HTTPMESSAGE_413,
    414: HTTPMESSAGE_414,
    415: HTTPMESSAGE_415,
    416: HTTPMESSAGE_416,
    417: HTTPMESSAGE_417,

    500: HTTPMESSAGE_500,
    501: HTTPMESSAGE_501,
    502: HTTPMESSAGE_502,
    503: HTTPMESSAGE_503,
    504: HTTPMESSAGE_504,
    505: HTTPMESSAGE_505
}

HTTPHEADER_100 = b"HTTP/1.1 200 Ok\r\n"
HTTPHEADER_101 = b"HTTP/1.1 200 Switching Protocols\r\n"


def get_http_status_message(code):
    return HTTPMESSAGES.get(code, None)


# exceptions

CONNECTION_CLOSED_EXCEPTION = _("remote connection closed")
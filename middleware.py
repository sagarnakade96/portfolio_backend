# Fast API imports
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse as FastAPIJSONResponse

# Python imports
from http import HTTPStatus
import json

# App imports

app = FastAPI()


class AsyncIteratorWrapper:
    """The following is a utility class that transforms a
    regular iterable to an asynchronous one.

    link: https://www.python.org/dev/peps/pep-0492/#example-2
    """

    def __init__(self, obj):
        self._it = iter(obj)

    def __aiter__(self):
        return self

    async def __anext__(self):
        try:
            value = next(self._it)
        except StopIteration:
            raise StopAsyncIteration
        return value


class CustomJSONResponse(FastAPIJSONResponse):
    def render(self, content) -> bytes:
        content_type = self.media_type
        if content_type == "application/json":
            http_code_to_message = {v.value: v.description for v in HTTPStatus}

            if self.status_code < 400:
                response_data = {
                    "code": self.status_code,
                    "message": http_code_to_message[self.status_code],
                    "data": content,
                    "error": None,
                }
            elif self.status_code >= 400:
                response_data = {
                    "code": self.status_code,
                    "message": http_code_to_message[self.status_code],
                    "error": content,
                    "data": None,
                }

            content = response_data
        return super().render(content)


def middleware_config(response: Response, resp_body: list):
    response.__setattr__("body_iterator", AsyncIteratorWrapper(resp_body))
    try:
        resp_body = json.loads(resp_body[0].decode())
    except:
        resp_body = str(resp_body)
    return CustomJSONResponse(content=resp_body, status_code=response.status_code)

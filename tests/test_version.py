import responses
from responses import matchers

from .factories import create_version


@responses.activate
def test_predict():
    version = create_version()

    responses.post(
        "https://api.replicate.com/v1/predictions",
        match=[
            matchers.json_params_matcher({"version": "v1", "input": {"text": "world"}})
        ],
        json={
            "id": "p1",
            "version": "v1",
            "urls": {
                "get": "https://api.replicate.com/v1/predictions/p1",
                "cancel": "https://api.replicate.com/v1/predictions/p1/cancel",
            },
            "created_at": "2022-04-26T20:00:40.658234Z",
            "completed_at": "2022-04-26T20:02:27.648305Z",
            "source": "api",
            "status": "processing",
            "input": {"text": "world"},
            "output": None,
            "error": None,
            "logs": "",
        },
    )
    responses.get(
        "https://api.replicate.com/v1/predictions/p1",
        json={
            "id": "p1",
            "version": "v1",
            "urls": {
                "get": "https://api.replicate.com/v1/predictions/p1",
                "cancel": "https://api.replicate.com/v1/predictions/p1/cancel",
            },
            "created_at": "2022-04-26T20:00:40.658234Z",
            "completed_at": "2022-04-26T20:02:27.648305Z",
            "source": "api",
            "status": "succeeded",
            "input": {"text": "world"},
            "output": "hello world",
            "error": None,
            "logs": "",
        },
    )

    assert version.predict(text="world") == "hello world"

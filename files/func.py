import io
import json
import requests
import ads

def handler(ctx, data: io.BytesIO=None):
    ads.set_auth('resource_principal')
    body = json.loads(data.getvalue())
    endpoint = ctx.Headers()["model_deployment"]
    return requests.post(endpoint, json=body, auth=ads.common.auth.default_signer()['signer']).json()

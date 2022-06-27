from fastapi import FastAPI, Response

import uvicorn

from logger_config.logger import logger

app = FastAPI()


@app.get('/')
def run():
    print('hello')


@app.middleware('http')
async def log_request(request, call_next):
    logger.info(f'{request.method} {request.url}')
    response = await call_next(request)
    logger.info(f'Status code: {response.status_code}')
    body = b""
    async for chunk in response.body_iterator:
        body += chunk
    return Response(
        content=body,
        status_code=response.status_code,
        headers=dict(response.headers),
        media_type=response.media_type
    )


if __name__ == "__main__":
    uvicorn.run('main:app', host='127.0.0.1', port=8008, reload=True, debug=True)

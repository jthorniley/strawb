Strawberry websocket/subscription test

1. Install uv package manager from https://docs.astral.sh/uv/
2. `uv sync`
3. `uv run --env-file=.env granian --interface=asginl --workers-kill-timeout=1 project.asgi:application`
4. Go to the test GraphiQL page at http://localhost:8000/graphql
5. Run

```
subscription {
  count(target: 10)
}
```

6. When the subscription completes, either the worker hangs and no more graphql requests 
   can be processed, or you get this stack trace.

```
[ERROR] Application callable raised an exception
Traceback (most recent call last):
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/granian/_futures.py", line 15, in future_watcher
    await inner(watcher.scope, watcher.proto)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/routing.py", line 48, in __call__
    return await application(scope, receive, send)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/sessions.py", line 44, in __call__
    return await self.inner(dict(scope, cookies=cookies), receive, send)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/sessions.py", line 261, in __call__
    return await self.inner(wrapper.scope, receive, wrapper.send)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/auth.py", line 185, in __call__
    return await super().__call__(scope, receive, send)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/middleware.py", line 24, in __call__
    return await self.inner(scope, receive, send)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/routing.py", line 118, in __call__
    return await application(
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/consumer.py", line 95, in app
    return await consumer(scope, receive, send)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/consumer.py", line 62, in __call__
    await await_many_dispatch([receive], self.dispatch)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/utils.py", line 50, in await_many_dispatch
    await dispatch(result)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/strawberry/channels/handlers/base.py", line 77, in dispatch
    await super().dispatch(message)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/consumer.py", line 74, in dispatch
    await handler(message)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/generic/websocket.py", line 250, in websocket_disconnect
    await self.disconnect(message["code"])
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/strawberry/channels/handlers/ws_handler.py", line 146, in disconnect
    await self.run_task
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/strawberry/http/async_base_view.py", line 275, in run
    websocket_response = await self.create_websocket_response(
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/strawberry/channels/handlers/ws_handler.py", line 190, in create_websocket_response
    await request.accept(subprotocol=subprotocol)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/generic/websocket.py", line 196, in accept
    await super().send(message)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/consumer.py", line 82, in send
    await self.base_send(message)
  File "/Users/james/strawb/.venv/lib/python3.13/site-packages/channels/sessions.py", line 221, in send
    return await self.real_send(message)
RuntimeError: ASGI flow error
```
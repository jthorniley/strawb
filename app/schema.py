from typing import AsyncGenerator
import strawberry
import asyncio

@strawberry.type
class Result:
    value: int

@strawberry.type
class Query:
    one: Result = strawberry.field(resolver=lambda: Result(value=1))

@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 10) -> AsyncGenerator[int, None]:
        try:
            for i in range(target):
                yield i
                print(f"yield {i}")
                await asyncio.sleep(0.1)
        finally:
            print("done")

schema = strawberry.Schema(query=Query, subscription=Subscription)

from fastapi import FastAPI
from models import ItemModel, QueueModel
from implementations.alchemy_queue import AlchemyQueue, QueueRepository, ItemRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from implementations.alchemy_queue.base import Base

app = FastAPI()


def instantiate_queue():
    engine = create_engine('sqlite:///test/alchemy_queue/local.db')

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    queue_repository = QueueRepository(session)
    item_repository = ItemRepository(session)

    queue = AlchemyQueue(queue_repository, item_repository, 'queue1')

    return queue


engine = create_engine('sqlite:///test/alchemy_queue/local.db')

# Create a queue object
app.queue = instantiate_queue()


@app.get("/mayonoise")
async def root():
    return {"message": "QPY Says Hello! QPY says MayonNoise!"}


@app.get("/queue/items/", response_model=list[ItemModel])
async def read_items():
    items = app.queue.get_items()

    return items


@app.post("/queue/item/", response_model=ItemModel)
async def add_item(data: dict):
    return app.queue.add(data)


@app.get("/queue/items/{item_id}", response_model=ItemModel)
async def get_item_by_id(item_id):
    item = app.queue.get_item_by_id(item_id)

    return item


@app.get("/queue/next_item", response_model=ItemModel)
async def get_next_item():
    item = app.queue.get_next()

    return item


@app.get('/queue', response_model=QueueModel)
async def get_queue():
    return {
        'name': app.queue.name,
        'max_retry_count': app.queue.queue.max_retry_count,
        'has_pending_items': app.queue.has_pending_items(),
        'is_empty': app.queue.is_empty()
    }


@app.put("/queue/items/{item_id}", response_model=bool)
async def update_item(item_id: int, status: str, output_data: dict = None):
    return app.queue.update_item(item_id, status, output_data)

# @app.delete("/items/remove")
# async def remove_item(item: ItemModel):
#     app.queue.remove_item(item)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

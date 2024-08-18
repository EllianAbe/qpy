from .models import ItemModel, QueueModel
from fastapi import FastAPI, Request
from .queue_manager import instantiate_queue

app = FastAPI()


# Create a queue object
app.queue = instantiate_queue()


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc: Exception):
    content = {"detail": "An unexpected error occurred.", "error": str(exc)},


@app.get("/mayonoise")
async def root():
    return {"message": "QPY Says Hello! QPY says MayonNoise!"}


@app.get("/queue/items/", response_model=list[ItemModel])
async def read_items(request: Request):
    filters = request.query_params

    filters = {key: value for key, value in filters.items()}

    items = app.queue.get_items(**filters)

    items = [ItemModel(id=item.id, data=item.data,
                       status=item.status, creation_datetime=item.creation_datetime,
                       retry_count=item.retry_count, output_data=item.output_data,
                       queue_id=item.queue_id) for item in items]

    # items = [ItemModel(**item) for item in items]

    return items


@app.post("/queue/items/", response_model=ItemModel)
async def add_item(data: dict):
    item = app.queue.add(data)

    return item


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

    app.queue.update_item(item_id, status, output_data)

    return True


@app.delete("/queue/items/{item_id}", response_model=dict)
async def remove_item(item_id):
    app.queue.remove_item(item_id)

    return {}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

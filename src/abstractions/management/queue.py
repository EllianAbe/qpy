from abc import abstractmethod, ABCMeta
from datetime import datetime


class Queue(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, definition: dict | None):
        # define a connection to the data source
        pass

    @abstractmethod
    def add(self, item: dict, eligible_date: datetime):
        # add an item to the queues
        pass

    @abstractmethod
    def enqueue_item(self, item):
        item.enqueue(self)

    @abstractmethod
    def get_next(self):
        # get the next item in the queue
        # return None if the queue is empty
        # do not forget to change the status of the item
        pass

    @abstractmethod
    def get_items(self):
        # get items from the queue, specify filter rules
        pass

    def has_pending_items(self, ignore_eligibility: bool = False) -> bool:
        # check if there are pending items in the queue
        pass

    @abstractmethod
    def get_item_by_id(self, item_id):
        # get an item from the queue by id
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        # check if the queue is empty
        pass

    @abstractmethod
    def update_item(self, item_id, status, output_data):
        item = self.get_item_by_id(item_id)

        if ItemStatus.is_final(item.status):
            raise ChangeStatusError(
                f'Cannot change status when status is {item._status}')

        item.status = status

        if output_data:
            item.output_data = output_data

        if item.status == ItemStatus.ERROR:
            item.retry_count += 1
            item.status = \
                ItemStatus.PENDING \
                if item.retry_count < self.max_retry_count \
                else ItemStatus.ERROR

            if self.max_retry_count == 0 or item.retry_count > self.max_retry_count:
                item.status = ItemStatus.ERROR

        return item

        # update an item in the queue

    @abstractmethod
    def postpone_item(self, item_id, eligible_date: datetime):
        # postpone an item
        pass

    @abstractmethod
    def remove_item(self, item_id):
        # remove an item from the queue
        pass

    def validate_item(self, item) -> bool:
        # validate an item
        pass

    def dispatcher(self, func):
        def wrapper(*args, **kwargs):
            item = func(*args, **kwargs)

            item = self.add(item)

            return item

        return wrapper

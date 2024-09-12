from abc import abstractmethod, ABCMeta


class Consumer(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, queue, identity: str = None):
        self.queue = queue
        self.identity = identity
        # define a connection to the data source
        pass

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
        pass
        # update an item in the queue

    @abstractmethod
    def postpone_item(self, item_id, eligible_date):
        # postpone an item
        pass

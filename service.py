import logging
import random
from datetime import datetime
from currency_service_pb2 import Value, TimeSlice
from currency_service_pb2_grpc import CurrencyProviderServicer


class DummyProvider(CurrencyProviderServicer):
    def __init__(self):
        pass

    def GetCurrency(self, request: TimeSlice, context):
        start = datetime.fromisoformat(request.start)
        end = datetime.fromisoformat(request.end)
        typ = request.currencyCode

        delta = (end - start).days

        logging.info(f'Received request for {typ}')

        for i in range(delta):
            item = random.uniform(0., 100.)
            yield Value(value=item)

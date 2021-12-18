import grpc
import os
import currency_service_pb2_grpc
from concurrent import futures
from service import DummyProvider

if __name__ == '__main__':
    host = os.getenv('HOST', '[::1]')
    port = os.getenv('PORT', '50000')

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=6))
    currency_service_pb2_grpc.add_CurrencyProviderServicer_to_server(
        DummyProvider(), server)

    server.add_insecure_port(f'{host}:{port}')
    server.start()
    server.wait_for_termination()

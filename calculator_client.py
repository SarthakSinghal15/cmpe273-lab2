from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def start():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.AdditionStub(channel)
    integer1=12
    integer2=122
    response = stub.add(calculator_pb2.AddRequest(number1=integer1,number2=integer2))
    print("The addition of "+str(integer1)+" and "+str(integer2)+" is " + str(response.message))


if __name__ == '__main__':

    start()

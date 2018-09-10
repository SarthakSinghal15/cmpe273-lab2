from __future__ import print_function

import grpc

import calculator_pb2
import calculator_pb2_grpc


def add(a,b):
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.AdditionStub(channel)
    response = stub.Addthem(calculator_pb2.AddRequest(number1=a,number2=b))
    print("The addition of "+str(a)+" and "+str(b)+" is " + str(response.message))


if __name__ == '__main__':

    add(34,45)

from argparse import Action
from final_project_code.wrappers.GatewayWrapper import GatewayWrapper
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters
from final_project_code.action import Action
import pytest


def test():
   gateway = JavaGateway(gateway_parameters=GatewayParameters(port=4242), callback_server_parameters=CallbackServerParameters());
   gameData = gateway.jvm.struct.GameData()
   md = gameData.getMotionData(False)
   a=0



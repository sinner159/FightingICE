from argparse import Action
from final_project_code.wrappers.GatewayWrapper import GatewayWrapper
from py4j.java_gateway import JavaGateway, GatewayParameters, CallbackServerParameters, get_field
from final_project_code.action import Action

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=4242), callback_server_parameters=CallbackServerParameters());



def test_getDeque(gateway):
    
    g = GatewayWrapper(gateway=gateway)
    a = [Action.AIR_A,Action.AIR_B]
    d = g.getDeque(a)
    b = 0


test_getDeque(gateway)
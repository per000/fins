from abc import ABCMeta, abstractmethod

class FinsPLCMemoryAreas:
    def __init__(self):
        """Hex code for memory areas

        Each memory area has a corresponding hex code for word access, bit access
        forced word access and forced bit access. This class provides name-based
        access to them.
        """

        self.EM0_WORD=b'\xA0'

class FinsCommandCode:
    def __init__(self):
        """Hex code for fins command code

        Each fins command has a corresponding hex code. This class provides name-based
        access to them.
        """
        self.MEMORY_AREA_READ=b'\x01\x01'


class FinsResponseEndCode:
    def __init__(self):
        self.NORMAL_COMPLETION=b'\x00\x00'
        self.SERVICE_CANCELLED=b'\x00\x01'

class FinsConnection(metaclass=ABCMeta):
    def __init__(self):
        self.dest_node_add=0
        self.srce_node_add=0
        self.dest_net_add=1
        self.srce_net_add=1
        self.dest_unit_add=0
        self.srce_unit_add=0
    @abstractmethod
    def execute_fins_command_frame(self,fins_command_frame):
        pass
    def fins_command_frame(self,command_code,text=b'', service_id=b'\x60',
                 icf=b'\x80',gct=b'\x07',rsv=b'\x00'):
        command_bytes=icf+rsv+gct+\
                      self.dest_net_add.to_bytes(1,'big')+self.dest_node_add.to_bytes(1,'big')+\
                      self.dest_unit_add.to_bytes(1,'big')+self.srce_net_add.to_bytes(1,'big')+\
                      self.srce_node_add.to_bytes(1,'big')+self.srce_unit_add.to_bytes(1,'big')+\
                      service_id+command_code+text
        return command_bytes

    def memory_area_read(self,memory_area_code,beginning_address=b'\x00\x00\x00\x00',number_of_items=1):
        """Function to read PLC memory areas

        :param memory_area_code: Memory area to read
        :param beginning_address: Beginning address
        :param number_of_items: Number of items to read
        :return: response
        """
        assert len(beginning_address)==3 or len(beginning_address)==4 or len(beginning_address)==5
        data = memory_area_code+beginning_address+number_of_items.to_bytes(2,'big')
        response=self.execute_fins_command_frame(
            self.fins_command_frame(FinsCommandCode().MEMORY_AREA_READ,data))
        return response

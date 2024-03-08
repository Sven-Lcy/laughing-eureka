from connection import Net  

class IOS_XE_17(Net):
    def __init__(self):
        super().__init__('cisco_ios', '10.2.212.46', 'ciscouser', 'cisco@123')
    
    def get_config(self):
        cmd = 'show run'
        info = self.device.send_command(cmd)
        data_str = info.split('platform console serial\n')[1]
        return data_str
    
    def interfaces(self):
        cmd = 'show ip int brie'
        info = self.device.send_command(cmd)
        data_list = []
        for line in info.split('\n')[1:]:
            line_list = line.split()
            if_name =line_list[0]
            if_ip = line_list[1]
            status = line_list[-1]
            data_list.append({'name': if_name,
                              'ip': if_ip,
                              'status': status})
        return data_list
    
    def recover_interface(self):
        pass

    def get_route(self):
        pass

    def post_route(self):
        pass

    def monitor(self):
        pass
    

from p0f import P0f, P0fException
class OSscan:
    def __init__(self, ip_adr):
        self.ip_adr = ip_adr
    def OSscan(self):
        # create a folder before run bv. /var/log/p0f
        p0f = P0f("/var/run/p0f/")
        try:
            data = p0f.get_info(self.ip_adr)
        except P0fException as e:
            print(e)
        return data

    def OSscan_result(self):
        data = self.OSscan()
        return data

if __name__ == "__main__":
    osscan = OSscan("ip")
    result = osscan.OSscan_result()

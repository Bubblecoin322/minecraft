from packet import malformed_packet
from argparse import ArgumentParser, ArgumentTypeError


def check_module(module):
    modules = ["malformed_packet"]
    if module in modules:
        return module
    raise ArgumentTypeError("Module not in list:", modules)


if __name__ == '__main__':
    parser = ArgumentParser()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-t", dest="time",
                          help="Time of attack", required=True)
    required.add_argument("-th", dest="threads",
                          help="Number of threads used to attack", required=True)
    required.add_argument("-a", dest="address",
                          help="Address of attacked server", required=True)
    required.add_argument("-p", dest="port",
                          help="Port of attacked server", required=True)
    required.add_argument("-m", dest="module",
                          help="Attack module", required=True, type=check_module)
    args = parser.parse_args()
    if args.module == "malformed_packet":
        malformed_packet.MalformedPacket(int(args.time), int(args.threads), args.address, int(args.port))

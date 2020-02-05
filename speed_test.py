import sys

def test():
    try:
        import speedtest
    except ModuleNotFoundError:
        print("Run 'sudo pip3 install speedtest' before continuing.")
        sys.exit()

    s = speedtest.Speedtest()
    s.get_best_server()
    s.upload()
    s.download()

    print("RESULTS:")
    print("\nDOWNLOAD SPEED: {0:.2f}".format(s.results.download / 1000000) + " Mbps")
    print("UPLOAD SPEED  : {0:.2f}".format(s.results.upload / 1000000) + " Mbps")
    print("PING LATENCY  : {0:.2f}".format(s.results.ping) + " ms")

    print("\nCLIENT INFO:")
    for key in s.results.client:
        print("\t{0:10} : {1}".format(key.upper(), s.results.client[key]))

    print("\nSERVER INFO:")
    for key in s.results.server:
        print("\t{0:10} : {1}".format(key.upper(), s.results.server[key]))
    print()


def main():
    print("\n################################")
    print("#     BANDWIDTH SPEED TEST     #")
    print("################################")

    print("\nPlease be patient while the test completes...\n")

    test()


if __name__ == '__main__':
    main()

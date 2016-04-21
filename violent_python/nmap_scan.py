import nmap
import optparse

def nmapScan(tgHost, tgPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgHost, tgPort)
    state = nmScan[tgHost]['tcp'][int(tgPort)]['state']
    print '[*]' + tgHost + 'tcp/' + tgPort + " " + state

def main():
    parser = optparse.OptionParser('usage%prog ' + \
    '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgHost', type='string', \
    help='Specify target host')
    parser.add_option('-p', dest='tgPort', type='string', \
    help='Specify target port')
    (options, args) = parser.parse_args()
    tgHost = options.tgHost
    tgPorts = str(options.tgPort).split(', ')
    if (tgHost == None) | (tgPorts[0] == None):
        print parser.usage
        exit(0)
    for port in tgPorts:
        nmapScan(tgHost, port)

if __name__ == '__main__':
    main()

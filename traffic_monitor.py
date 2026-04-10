from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ipv4

log = core.getLogger()

mac_to_port = {}

tcp_count = 0
udp_count = 0
icmp_count = 0


def _handle_PacketIn(event):
    global tcp_count, udp_count, icmp_count

    packet = event.parsed
    dpid = event.connection.dpid

    if not packet.parsed:
        return

    if dpid not in mac_to_port:
        mac_to_port[dpid] = {}

    mac_to_port[dpid][packet.src] = event.port

    ip_packet = packet.find('ipv4')

    if ip_packet:
        if ip_packet.protocol == 6:
            tcp_count += 1
            log.info("TCP Packet detected")

        elif ip_packet.protocol == 17:
            udp_count += 1
            log.info("UDP Packet detected")

        elif ip_packet.protocol == 1:
            icmp_count += 1
            log.info("ICMP Packet detected")

        total = tcp_count + udp_count + icmp_count

        log.info("Stats -> TCP:%s UDP:%s ICMP:%s",
                 tcp_count, udp_count, icmp_count)

        if total > 0:
            log.info("Distribution -> TCP: %.2f%% UDP: %.2f%% ICMP: %.2f%%",
                     (tcp_count / total) * 100,
                     (udp_count / total) * 100,
                     (icmp_count / total) * 100)

    # Forwarding + Flow rule
    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    if out_port != of.OFPP_FLOOD:
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet, event.port)
        msg.actions.append(of.ofp_action_output(port=out_port))
        msg.idle_timeout = 10
        msg.hard_timeout = 30
        event.connection.send(msg)

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    msg.in_port = event.port
    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Traffic Monitor Started")

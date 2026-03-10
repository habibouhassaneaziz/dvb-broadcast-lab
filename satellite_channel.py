import random
import time

def satellite_channel(packets, loss_rate=0.05, delay_ms=250, bit_error_rate=0.0001):
    """
    Simule un canal satellite avec :
    - perte de paquets
    - latence
    - erreurs de bits
    """

    received = []
    total_packets = len(packets)
    lost_packets = 0
    total_bit_errors = 0

    for p in packets:

        # perte de paquet
        if random.random() < loss_rate:
            lost_packets += 1
            continue

        packet = bytearray(p)

        # erreurs de bits
        for i in range(len(packet)):
            if random.random() < bit_error_rate:
                packet[i] ^= 0x01
                total_bit_errors += 1

        # latence satellite
        time.sleep(delay_ms / 1000.0)

        received.append(bytes(packet))

    print("\n📊 Satellite channel statistics")
    print("------------------------------")
    print(f"Packets sent: {total_packets}")
    print(f"Packets received: {len(received)}")
    print(f"Packets lost: {lost_packets}")
    print(f"Bit errors simulated: {total_bit_errors}")
    print(f"Effective loss rate: {(lost_packets/total_packets)*100:.2f}%\n")

    return received, total_bit_errors
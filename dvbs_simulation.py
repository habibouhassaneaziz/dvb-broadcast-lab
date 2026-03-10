import hashlib
from satellite_channel import satellite_channel
from metrics import compute_metrics

TS_PACKET_SIZE = 188
SYNC_BYTE = 0x47
PID_DATA = 256


# Création d’un flux IP à transmettre
def create_ip_payload(filename):

    data = (
        "Hello DVB-S!\n"
        "This file simulates IP data sent over satellite.\n"
        "Broadcast, MPEG-TS, no return channel.\n"
    ) * 20

    data = data.encode("utf-8")

    with open(filename, "wb") as f:
        f.write(data)

    return data


# Encapsulation IP → MPEG-TS
def encapsulate_to_ts(ip_data):

    packets = []
    continuity_counter = 0

    payload_size = TS_PACKET_SIZE - 4

    for i in range(0, len(ip_data), payload_size):

        payload = ip_data[i:i + payload_size]

        header = bytearray(4)
        header[0] = SYNC_BYTE
        header[1] = (PID_DATA >> 8) & 0x1F
        header[2] = PID_DATA & 0xFF
        header[3] = continuity_counter & 0x0F

        continuity_counter = (continuity_counter + 1) % 16

        packet = header + payload

        if len(packet) < TS_PACKET_SIZE:
            packet += bytes(TS_PACKET_SIZE - len(packet))

        packets.append(packet)

    return packets


# Décapsulation MPEG-TS → IP
def decapsulate_from_ts(packets):

    ip_data = bytearray()

    for p in packets:

        if p[0] != SYNC_BYTE:
            continue

        pid = ((p[1] & 0x1F) << 8) | p[2]

        if pid != PID_DATA:
            continue

        payload = p[4:]

        ip_data.extend(payload)

    return bytes(ip_data).rstrip(b"\x00")


# Vérification d’intégrité
def checksum(data):

    return hashlib.sha256(data).hexdigest()


# Programme principal
if __name__ == "__main__":

    print("📡 DVB-S Simulation Started")

    original = create_ip_payload("ip_input.bin")

    print("Original checksum:", checksum(original))

    ts_packets = encapsulate_to_ts(original)

    print(f"Encapsulated into {len(ts_packets)} TS packets")

    # transmission via le canal satellite
    received_packets, bit_errors = satellite_channel(
        ts_packets,
        loss_rate=0.05,
        delay_ms=250,
        bit_error_rate=0.0001
    )

    print(f"Received {len(received_packets)} TS packets")

    # calcul des métriques
    stats = compute_metrics(len(ts_packets), len(received_packets), bit_errors)

    print("\n📈 Link Metrics")
    print("----------------")
    print(f"Packets sent: {stats['sent_packets']}")
    print(f"Packets received: {stats['received_packets']}")
    print(f"Packets lost: {stats['lost_packets']}")
    print(f"Loss rate: {stats['loss_rate']:.2f}%")
    print(f"Success rate: {stats['success_rate']:.2f}%")
    print(f"Bit errors: {stats['bit_errors']}")

    reconstructed = decapsulate_from_ts(received_packets)

    print("\nReconstructed checksum:", checksum(reconstructed))

    with open("ip_output.bin", "wb") as f:
        f.write(reconstructed)

    if checksum(original) == checksum(reconstructed):
        print("✅ Transmission OK (no loss impact)")
    else:
        print("⚠️ Data corrupted (typical DVB-S behavior)")
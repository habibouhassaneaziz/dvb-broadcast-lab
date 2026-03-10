def compute_metrics(sent_packets, received_packets, bit_errors):

    lost_packets = sent_packets - received_packets

    if sent_packets > 0:
        loss_rate = (lost_packets / sent_packets) * 100
        success_rate = (received_packets / sent_packets) * 100
    else:
        loss_rate = 0
        success_rate = 0

    metrics = {
        "sent_packets": sent_packets,
        "received_packets": received_packets,
        "lost_packets": lost_packets,
        "loss_rate": loss_rate,
        "success_rate": success_rate,
        "bit_errors": bit_errors
    }

    return metrics
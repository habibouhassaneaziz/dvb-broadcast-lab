import sys
import os

# Ajouter le dossier racine du projet au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from dvbs_simulation import encapsulate_to_ts, decapsulate_from_ts


def test_encapsulation_decapsulation():
    """
    Test basique : vérifier que l'encapsulation et la décapsulation
    ne corrompent pas les données IP.
    """
    data = b"Test DVB transmission"

    ts_packets = encapsulate_to_ts(data)

    reconstructed = decapsulate_from_ts(ts_packets)

    assert reconstructed == data


def test_large_payload():
    """
    Test avec un flux plus grand pour générer plusieurs paquets TS.
    """
    data = (b"Hello DVB-S! " * 100)

    ts_packets = encapsulate_to_ts(data)

    reconstructed = decapsulate_from_ts(ts_packets)

    assert reconstructed == data
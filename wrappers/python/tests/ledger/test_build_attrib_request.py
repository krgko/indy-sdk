import json
import pytest

from indy import ledger, error


@pytest.mark.asyncio
async def test_build_attrib_request_works_for_raw_value():
    identifier = "Th7MpTaRZVRYnPiabds81Y"
    destination = "Th7MpTaRZVRYnPiabds81Y"
    raw = '{"endpoint":{"ha":"127.0.0.1:5555"}}'

    expected_response = {
        "identifier": identifier,
        "operation": {
            "type": "100",
            "dest": destination,
            "raw": raw
        }
    }

    response = json.loads(await ledger.build_attrib_request(identifier, destination, None, raw, None))
    assert expected_response.items() <= response.items()


@pytest.mark.asyncio
async def test_build_attrib_request_works_for_hash_value():
    identifier = "Th7MpTaRZVRYnPiabds81Y"
    destination = "Th7MpTaRZVRYnPiabds81Y"
    xhash = "83d907821df1c87db829e96569a11f6fc2e7880acba5e43d07ab786959e13bd3"

    expected_response = {
        "identifier": identifier,
        "operation": {
            "type": "100",
            "dest": destination,
            "hash": xhash
        }
    }

    response = json.loads(await ledger.build_attrib_request(identifier, destination, xhash, None, None))
    assert expected_response.items() <= response.items()


@pytest.mark.asyncio
async def test_build_attrib_request_works_for_enc_value():
    identifier = "Th7MpTaRZVRYnPiabds81Y"
    destination = "Th7MpTaRZVRYnPiabds81Y"
    enc = "aa3f41f619aa7e5e6b6d0de555e05331787f9bf9aa672b94b57ab65b9b66c3ea960b18a98e3834b1fc6cebf49f463b81fd6e3181"

    expected_response = {
        "identifier": identifier,
        "operation": {
            "type": "100",
            "dest": destination,
            "enc": enc
        }
    }

    response = json.loads(await ledger.build_attrib_request(identifier, destination, None, None, enc))
    assert expected_response.items() <= response.items()


@pytest.mark.asyncio
async def test_build_attrib_request_works_for_missed_attribute():
    identifier = "Th7MpTaRZVRYnPiabds81Y"
    destination = "Th7MpTaRZVRYnPiabds81Y"

    with pytest.raises(error.CommonInvalidStructure):
        await ledger.build_attrib_request(identifier, destination, None, None, None)

import pytest
import psutil
import socket
import platform
import GPUtil

@pytest.mark.integration
def test_cpu_info():
    """CPU must report valid core count and frequency."""
    cores = psutil.cpu_count(logical=True)
    freq = psutil.cpu_freq()
    assert cores > 0, "No CPU cores detected!"
    assert freq and freq.current > 0, "CPU frequency not reported correctly."


@pytest.mark.integration
def test_memory_capacity():
    """RAM should be above amount (e.g., 5 GB)."""
    RAM_MIN_GB = 5
    mem = psutil.virtual_memory()
    assert mem.total > RAM_MIN_GB * 1024 ** 3, (
        f"Total memory is {mem.total / 1024**3:.1f}GB, "
        f"expected > {RAM_MIN_GB}GB"
    )
    assert mem.available > 0, (
        f"Available memory is {mem.available / 1024**3:.1f}GB, "
        f"expected > 0GB"
    )


@pytest.mark.integration
def test_disk_space():
    """Ensure root partition has some free space."""
    MAX_FREE_SPACE_GB = 1000
    MIN_SPACE_GB = 200
    usage = psutil.disk_usage("/")

    assert usage.total > 1 * 1024 ** 3, (
        f"Disk total size is {usage.total / 1024**3:.1f}GB, "
        f"expected > 1GB"
    )
    assert usage.free > MIN_SPACE_GB * 1024**2, (
        f"Disk free space is {usage.free / 1024**2:.1f}MB, "
        f"expected > {MIN_SPACE_GB}MB"
    )
    assert usage.free <= MAX_FREE_SPACE_GB * 1024**3, (
        f"Disk free space is {usage.free / 1024**3:.1f}GB, "
        f"expected ≤ {MAX_FREE_SPACE_GB}GB (low-space condition)."
    )


@pytest.mark.integration
def test_network_connectivity():
    """Check if hostname resolves and internet is reachable."""
    assert usage.free <= MAX_FREE_SPACE_MB * 1024**2, (
        f"Disk free space is {usage.free / 1024**2:.1f}MB, "
        f"expected ≤ {MAX_FREE_SPACE_MB}MB (low-space condition)."
    )


@pytest.mark.integration
def test_network_connectivity():
    """Check if hostname resolves and internet is reachable."""
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    assert ip, "No IP address detected!"

    # Try connecting to a reliable site (Google DNS)
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        pytest.fail("No network connectivity!")


@pytest.mark.integration
def test_system_identity():
    """Ensure system reports OS and machine architecture."""
    assert platform.system() in ["Linux"]
    assert platform.machine(), "Machine architecture not detected."


@pytest.mark.integration
def test_battery_status():
    """If battery is present, check plugged-in status."""
    battery = psutil.sensors_battery()
    if battery is None:
        pytest.skip("No battery detected on this system.")
    else:
        assert 0 <= battery.percent <= 100, f"Unexpected battery percentage: {battery.percent}"

        valid_states = [True, False, None]
        assert battery.power_plugged in valid_states, (
            f"Unexpected power_plugged state value: {battery.power_plugged}."
            "Expected True (plugged in), False (not plugged), or None (unknown)."
        )
        if battery.power_plugged is None:
            pytest.skip("Power status not reported by OS")

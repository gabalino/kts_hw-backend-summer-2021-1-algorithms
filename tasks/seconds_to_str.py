__all__ = ("seconds_to_str",)


def seconds_to_str(seconds: int) -> str:
    """Реализует текстовое представление времени.

    Example:
        >> seconds_to_str(20)
        20s
        >> seconds_to_str(60)
        01m00s
        >> seconds_to_str(65)
        01m05s
        >> seconds_to_str(3700)
        01h01m40s
        >> seconds_to_str(93600)
        01d02h00m00s
    """
    time = seconds
    time_str = f"{(time % 60):02}s"
    time = time // 60
    if time > 0:
        time_str = f"{(time % 60):02}m{time_str}"
        time = time // 60
        if time > 0:
            time_str = f"{(time % 24):02}h{time_str}"
            time = time // 24
            if time > 0:
                time_str = f"{(time % 30):02}d{time_str}"
                time = time // 30
                if time > 0:
                    time_str = f"{(time % 12):02}m{time_str}"
                    time = time // 12
                    if time > 0:
                        time_str = f"{(time):02}y{time_str}"
    return time_str

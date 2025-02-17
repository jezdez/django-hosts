def normalize_scheme(scheme=None, default="//"):
    if scheme is None:
        scheme = default
    elif scheme.endswith(":"):
        scheme = f"{scheme}//"
    elif "//" not in scheme:
        scheme = f"{scheme}://"
    return scheme


def normalize_port(port=None):
    if port is None:
        port = ""
    elif ":" in port:
        port = ":{}".format(port.strip(":"))
    elif port:
        port = f":{port}"
    return port

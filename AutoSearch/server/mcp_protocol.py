def parse_request(request: str) -> dict:
    if not request.startswith("MCP/1.0"):
        return {}
    body = request.split("FILTER", 1)[-1].strip()
    filters = {}
    for part in body.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            filters[k.strip()] = v.strip()
    return filters

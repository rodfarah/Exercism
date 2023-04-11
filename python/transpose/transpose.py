import itertools


def transpose(lines: str) -> str:
    """Transpose a string input."""
    if not transpose:
        return ""
    if "\n" in lines:
        lines = lines.split("\n")
    else:
        return "\n".join([char for char in lines])

    combined = []
    for tup in itertools.zip_longest(*lines, fillvalue=" "):
        combined.append("".join(tup))

    result = []
    for item in combined:
        while True:
            if item.endswith(" "):
                item = item.removesuffix(" ")
                continue
            else:
                result.append(item)
                break

    return "\n".join(result)


print(transpose("The first line.\nThe second line."))

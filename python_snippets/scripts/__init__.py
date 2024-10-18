import fileinput

from ..domains import domain_sort_key


def domainsort() -> None:
    """Read a list of domains from stdin or from file and sort them."""

    for x in sorted(
        fileinput.input(encoding="utf-8"),
        key=lambda x: domain_sort_key(x.strip()),
    ):
        print(x, end="")

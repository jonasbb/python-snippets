import random

from python_snippets.domains import domain_sort_key


def test_domainsort() -> None:
    # https://datatracker.ietf.org/doc/html/rfc4034#section-6.1
    solution = [
        "example",
        "a.example",
        "a.example.",  # Not in RFC, sort FQDN after
        "yljkjljk.a.example",
        "Z.a.example",
        "Z.a.example.",  # Not in RFC, sort FQDN after
        "zABC.a.EXAMPLE",
        "z.example",
        "\001.z.example",
        "*.z.example",
        "\200.z.example",
    ]

    # Copy domains list
    domains = solution[:]
    for _ in range(100):
        # Shuffle in place
        random.shuffle(domains)
        domains.sort(key=domain_sort_key)
        assert solution == domains, "Sorting resulted in a wrong domain order"

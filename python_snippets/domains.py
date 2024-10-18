def domain_sort_key(domain: str) -> tuple[list[str], bool]:
    """
    Create a sort key for a list of domains

    This function converts the `domain` into a sortable key.
    The keys sort using the "Canonical DNS Name Order" as defined in [RFC 4034](https://datatracker.ietf.org/doc/html/rfc4034#section-6.1).

    # Example

    ```python
    domains = ['z.example', 'Z.a.example', '*.z.example', 'example', 'a.example']
    domains.sort(key=python_snippets.domains.domain_sort_key)
    assert domains == ['example', 'a.example', 'Z.a.example', 'z.example', '*.z.example']
    ```
    """

    labels: list[str] = []
    is_escaped = False
    curr_label: list[str] = []

    # Domain sorting happens case insensitive
    domain = domain.lower()

    # Process labels char by char
    # Handling escaped internal dots, i.e.,
    # www.exa\.mple.net -> ["www", "exa.mple", "net"]
    for c in domain:
        if is_escaped:
            if c == ".":
                curr_label += c
                is_escaped = False
            else:
                raise ValueError("In domains only the `.` character can be escaped.")
        else:
            if c == "\\":
                is_escaped = True
            elif c == ".":
                labels.append("".join(curr_label))
                curr_label = []
            else:
                curr_label.append(c)

    # Add last label to the list of labels
    if len(curr_label) > 0:
        labels.append("".join(curr_label))
    is_fqdn = len(curr_label) == 0

    # Reverse labels to sort by TLD, SLD, etc
    labels.reverse()

    return (labels, is_fqdn)

from typing import Any


def pytest_markdown_docs_globals() -> dict[str, Any]:
    import python_snippets  # pylint: disable=import-outside-toplevel

    return {
        # Always inject the package itself
        "python_snippets": python_snippets,
    }

import os
from collections.abc import Callable
from typing import IO, TYPE_CHECKING, Any, TypeAlias, cast

if TYPE_CHECKING:
    from _typeshed import StrOrBytesPath
else:
    StrOrBytesPath: TypeAlias = str | bytes | os.PathLike


def fopen(
    filename: StrOrBytesPath,
    mode: str = "r",
    *,
    encoding: str | None = "utf-8",
    errors: str | None = None,
    buffering: int = -1,
    newline: str | None = None,
    closefd: bool = True,
    opener: Callable[[str, int], int] | None = None,
) -> IO[Any]:
    """
    Improved version of the Python `open()` function that transparently supports compressed files.

    If the filename ends in a supported ending, the file is being opened with the corresponding compression utility.
    This makes reading and writing from compressed files very simple and basically transparent.

    The function defaults to assuming "utf-8" as the encoding.

    The supported formats are:

    * `.bz2`
    * `.gz`
    * `.xz`

    # Examples

    Replacement for `open()`:

    ```python
    with python_snippets.fopen("./foobar.xz", "wt") as f:
        f.writelines(["Hello", "World", "again"])
    ```

    The function can be used together with the `fileinput` module for simple command line file processing.

    ```python notest
    import fileinput
    for line in fileinput.input(openhook=python_snippets.fopen):
        process(line)

    ```
    """

    ext = os.path.splitext(filename)[1]
    if ext == ".gz":
        import gzip  # pylint: disable=import-outside-toplevel

        return cast(IO[Any], gzip.open(filename, mode))
    elif ext == ".xz":
        import lzma  # pylint: disable=import-outside-toplevel

        return lzma.open(filename, mode)
    elif ext == ".bz2":
        import bz2  # pylint: disable=import-outside-toplevel

        return bz2.open(filename, mode)
    else:
        return open(
            filename,
            mode,
            encoding=encoding,
            errors=errors,
            buffering=buffering,
            newline=newline,
            closefd=closefd,
            opener=opener,
        )

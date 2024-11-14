import sys

import pyodide  # type: ignore[attr-defined]

# Cleanup any leftover matplotlib plots
try:
    import matplotlib.pyplot as plt

    plt.close("all")
    plt.rcParams["figure.figsize"] = (width, height)  # type: ignore[attr-defined]
    plt.rcParams["figure.dpi"] = dpi  # type: ignore[attr-defined]
except ModuleNotFoundError:
    pass

import asyncio

from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display
from IPython.utils import capture

InteractiveShell().instance()

with capture.capture_output() as output:
    value = None
    try:
        value = await asyncio.wait_for(pyodide.code.eval_code_async(code, globals=environment), timeout=3)  # type: ignore[attr-defined]
    except Exception as err:
        print(err, file=sys.stderr)
    if value is not None:
        display(value)

{
    "value": value,
    "stdout": output.stdout,
    "stderr": output.stderr,
    "outputs": output.outputs,
}

"""Run nbdev_test on Windows.

nbdev 3.0.18's `nbdev/test.py` calls `faulthandler.register(...)` unconditionally,
but `faulthandler.register` only exists on Unix, so `nbdev_test` crashes on Windows.
This wrapper installs a harmless no-op shim, then runs the tests serially in-process.
"""
import faulthandler, sys, os

if not hasattr(faulthandler, "register"):
    faulthandler.register = lambda *a, **k: None

os.chdir(os.path.join(os.path.dirname(__file__), ".."))
from nbdev.test import nbdev_test

if __name__ == "__main__":
    nbdev_test.__wrapped__(n_workers=0, do_print=True)
    print("nbdev_test: all notebooks passed")

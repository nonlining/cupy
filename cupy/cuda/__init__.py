import contextlib

from cupy.cuda import compiler  # NOQA
from cupy.cuda import device  # NOQA
from cupy.cuda import function  # NOQA
from cupy.cuda import memory  # NOQA
from cupy.cuda import nvtx  # NOQA
from cupy.cuda import pinned_memory  # NOQA
from cupy.cuda import profiler  # NOQA
from cupy.cuda import stream  # NOQA


# import class and function
from cupy.cuda.compiler import compile_with_cache  # NOQA
from cupy.cuda.device import Device  # NOQA
from cupy.cuda.device import get_cublas_handle  # NOQA
from cupy.cuda.device import get_device_id  # NOQA
from cupy.cuda.function import Function  # NOQA
from cupy.cuda.function import Module  # NOQA
from cupy.cuda.memory import alloc  # NOQA
from cupy.cuda.memory import Memory  # NOQA
from cupy.cuda.memory import MemoryPointer  # NOQA
from cupy.cuda.memory import MemoryPool  # NOQA
from cupy.cuda.memory import set_allocator  # NOQA
from cupy.cuda.pinned_memory import alloc_pinned_memory  # NOQA
from cupy.cuda.pinned_memory import PinnedMemory  # NOQA
from cupy.cuda.pinned_memory import PinnedMemoryPointer  # NOQA
from cupy.cuda.pinned_memory import PinnedMemoryPool  # NOQA
from cupy.cuda.pinned_memory import set_pinned_memory_allocator  # NOQA
from cupy.cuda.stream import Event  # NOQA
from cupy.cuda.stream import get_elapsed_time  # NOQA
from cupy.cuda.stream import Stream  # NOQA


@contextlib.contextmanager
def profile():
    """Enable CUDA profiling during with statement.

    This function enables profiling on entering a with statement, and disables
    profiling on leaving the statement.

    >>> with cupy.cuda.profile():
    ...    # do something you want to measure
    ...    pass

    """
    profiler.start()
    try:
        yield
    finally:
        profiler.stop()


@contextlib.contextmanager
def timerange(message, id_color=-1):
    """A context manager to describe the enclosed block as a nested time range

    >>> with cupy.cuda.timerange('some range in green', 0):
    ...    # do something you want to measure
    ...    pass

    Args:
        message (str): Name of a range.
        id_color (int): ID of color for a range.

    .. seealso:: :func:`cupy.cuda.nvtx.RangePush`
        :func:`cupy.cuda.nvtx.RangePop`
    """
    nvtx.RangePush(message, id_color)
    try:
        yield
    finally:
        nvtx.RangePop()


@contextlib.contextmanager
def timerangeC(message, color=0):
    """A context manager to describe the enclosed block as a nested time range

    >>> with cupy.cuda.timerangeC('some range in green', 0xFF00FF00):
    ...    # do something you want to measure
    ...    pass

    Args:
        message (str): Name of a range.
        color (uint32): ARGB color for a range.

    .. seealso:: :func:`cupy.cuda.nvtx.RangePushC`
        :func:`cupy.cuda.nvtx.RangePop`
    """
    nvtx.RangePushC(message, color)
    try:
        yield
    finally:
        nvtx.RangePop()

import operator
import re

from datetime import timedelta, datetime

from bytewax.dataflow import Dataflow
from bytewax.inputs import ManualInputConfig
from bytewax.outputs import StdOutputConfig
from bytewax.execution import run_main
from bytewax.window import SystemClockConfig, TumblingWindowConfig


def input_builder(worker_index, worker_count, resume_state):
    state = None  # ignore recovery
    for line in open("wordcount.txt"):
        yield state, line


def lower(line):
    return line.lower()


def tokenize(line):
    return re.findall(r'[^\s!,.?":;0-9]+', line)


def initial_count(word):
    return word, 1


def add(count1, count2):
    return count1 + count2


clock_config = SystemClockConfig()
window_config = TumblingWindowConfig(length=timedelta(seconds=5))

flow = Dataflow()
flow.input("input", ManualInputConfig(input_builder))
flow.map(lower)
flow.flat_map(tokenize)
flow.map(initial_count)
flow.reduce_window("sum", clock_config, window_config, add)
flow.capture(StdOutputConfig())

run_main(flow)
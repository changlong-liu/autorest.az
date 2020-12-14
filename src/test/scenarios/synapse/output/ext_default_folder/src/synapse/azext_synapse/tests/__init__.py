# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
import inspect
import logging
import os
import sys
import traceback
import datetime as dt

from azure.core.exceptions import AzureError
from azure.cli.testsdk.exceptions import CliTestError, CliExecutionError, JMESPathCheckAssertionError


logger = logging.getLogger('azure.cli.testsdk')
logger.addHandler(logging.StreamHandler())
__path__ = __import__('pkgutil').extend_path(__path__, __name__)
exceptions = []
test_map = dict()
SUCCESSED = "successed"
FAILED = "failed"


def try_manual(func):
    def import_manual_function(origin_func):
        from importlib import import_module
        decorated_path = inspect.getfile(origin_func).lower()
        module_path = __path__[0].lower()
        if not decorated_path.startswith(module_path):
            raise Exception("Decorator can only be used in submodules!")
        manual_path = os.path.join(
            decorated_path[module_path.rfind(os.path.sep) + 1:])
        manual_file_path, manual_file_name = os.path.split(manual_path)
        module_name, _ = os.path.splitext(manual_file_name)
        manual_module = "..manual." + \
            ".".join(manual_file_path.split(os.path.sep) + [module_name, ])
        return getattr(import_module(manual_module, package=__name__), origin_func.__name__)

    def get_func_to_call():
        func_to_call = func
        try:
            func_to_call = import_manual_function(func)
            logger.info("Found manual override for %s(...)", func.__name__)
        except (ImportError, AttributeError):
            pass
        return func_to_call

    def wrapper(*args, **kwargs):
        func_to_call = get_func_to_call()
        logger.info("running %s()...", func.__name__)
        try:
            test_map[func.__name__] = dict()
            test_map[func.__name__]["result"] = SUCCESSED
            test_map[func.__name__]["error_message"] = ""
            test_map[func.__name__]["error_stack"] = ""
            test_map[func.__name__]["error_normalized"] = ""
            test_map[func.__name__]["start_dt"] = dt.datetime.utcnow()
            ret = func_to_call(*args, **kwargs)
        except (AssertionError, AzureError, CliTestError, CliExecutionError, SystemExit,
                JMESPathCheckAssertionError) as e:
            use_exception_cache = os.getenv("TEST_EXCEPTION_CACHE")
            if use_exception_cache is not None and use_exception_cache.lower() == "true":
                raise
            test_map[func.__name__]["end_dt"] = dt.datetime.utcnow()
            test_map[func.__name__]["result"] = FAILED
            test_map[func.__name__]["error_message"] = str(e).replace("\r\n", " ").replace("\n", " ")[:500]
            test_map[func.__name__]["error_stack"] = traceback.format_exc().replace(
                "\r\n", " ").replace("\n", " ")[:500]
            logger.info("--------------------------------------")
            logger.info("step exception: %s", e)
            logger.error("--------------------------------------")
            logger.error("step exception in %s: %s", func.__name__, e)
            logger.info(traceback.format_exc())
            exceptions.append((func.__name__, sys.exc_info()))
        else:
            test_map[func.__name__]["end_dt"] = dt.datetime.utcnow()
            return ret

    if inspect.isclass(func):
        return get_func_to_call()
    return wrapper


def calc_coverage(filename):
    filename = filename.split(".")[0]
    coverage_name = filename + "_coverage.md"
    with open(coverage_name, "w") as f:
        f.write("|Scenario|Result|ErrorMessage|ErrorStack|ErrorNormalized|StartDt|EndDt|\n")
        total = len(test_map)
        covered = 0
        for k, v in test_map.items():
            if not k.startswith("step_"):
                total -= 1
                continue
            if v["result"] == SUCCESSED:
                covered += 1
            f.write("|{step_name}|{result}|{error_message}|{error_stack}|{error_normalized}|{start_dt}|"
                    "{end_dt}|\n".format(step_name=k, **v))
        f.write("Coverage: {}/{}\n".format(covered, total))
    print("Create coverage\n", file=sys.stderr)


def raise_if():
    if exceptions:
        if len(exceptions) <= 1:
            raise exceptions[0][1][1]
        message = "{}\nFollowed with exceptions in other steps:\n".format(str(exceptions[0][1][1]))
        message += "\n".join(["{}: {}".format(h[0], h[1][1]) for h in exceptions[1:]])
        raise exceptions[0][1][0](message).with_traceback(exceptions[0][1][2])

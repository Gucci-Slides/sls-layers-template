def pandas_version(event, context):
    import pandas as pd

    pandas_version = pd.__version__

    response = pandas_version
    return response


def numpy_version(event, context):
    import numpy as np

    numpy_version = np.__version__

    response = numpy_version
    return response

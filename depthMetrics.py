
from glob import glob
import time
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_squared_log_error
from icecream import ic
from PIL import Image

import warnings

warnings.filterwarnings("ignore") 

#.....................................................................................................................................................
#   Hyperparameters
#.....................................................................................................................................................

EPSILON = 1e-10

target_path = glob("C:/Users/hunte/Downloads/Paper_Fingerprinting/Augmentation Images/Coffee Stain/*")
predicted_path = glob("C:/Users/hunte/Downloads/Paper_Fingerprinting/Augmentation Images/Murder Stain/*")

#.....................................................................................................................................................


def _error(actual: np.ndarray, predicted: np.ndarray):
    """ Simple error """
    return actual - predicted

def _naive_forecasting(actual: np.ndarray, seasonality: int = 1):
    """ Naive forecasting method which just repeats previous samples """
    return actual[:-seasonality]


def _relative_error(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Relative Error """
    if benchmark is None or isinstance(benchmark, int):
        # If no benchmark prediction provided - use naive forecasting
        if not isinstance(benchmark, int):
            seasonality = 1
        else:
            seasonality = benchmark
        return _error(actual[seasonality:], predicted[seasonality:]) /\
               (_error(actual[seasonality:], _naive_forecasting(actual, seasonality)) + EPSILON)

    return _error(actual, predicted) / (_error(actual, benchmark) + EPSILON)

def abs_relative_error(actual: np.ndarray, predicted: np.ndarray, benchmark: np.ndarray = None):
    """ Absolute Relative Error """
    return np.abs(_relative_error(actual, predicted, benchmark))


def mse(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Squared Error """
    return np.mean(np.square(_error(actual, predicted)))


def rmse(actual: np.ndarray, predicted: np.ndarray):
    """ Root Mean Squared Error """
    return np.sqrt(mse(actual, predicted))


def rmse_log(actual: np.ndarray, predicted: np.ndarray):    # Takes only 2 dimensional Params max
    """ Root Mean Squared Error Logarithmic"""
    return np.sqrt(mean_squared_log_error(actual, predicted))


def mae(actual: np.ndarray, predicted: np.ndarray):
    """ Mean Absolute Error """
    return np.mean(np.abs(_error(actual, predicted)))


def rrse(actual: np.ndarray, predicted: np.ndarray):
    """ Root Relative Squared Error """
    return np.sqrt(np.sum(np.square(actual - predicted)) / np.sum(np.square(actual - np.mean(actual))))


def rae(actual: np.ndarray, predicted: np.ndarray):
    """ Relative Absolute Error (aka Approximation Error) """
    return np.sum(np.abs(actual - predicted)) / (np.sum(np.abs(actual - np.mean(actual))) + EPSILON)

def δ1(actual: np.ndarray, predicted: np.ndarray):
    """ δ1 Threshold Error """

    actual = actual.reshape(-1)
    predicted = predicted.reshape(-1)
    δ1 = 0

    for i in zip(actual, predicted):
        if max((i[0]/i[1]), (i[1]/i[0])) < 1.25:
            δ1 += 1

    δ1 = δ1/len(actual)

    return δ1

def δ2(actual: np.ndarray, predicted: np.ndarray):
    """ δ2 Threshold Error """

    actual = actual.reshape(-1)
    predicted = predicted.reshape(-1)
    δ2 = 0

    for i in zip(actual, predicted):
        if max((i[0]/i[1]), (i[1]/i[0])) < 1.25*1.25:
            δ2 += 1

    δ2 = δ2/len(actual)

    return δ2

def δ3(actual: np.ndarray, predicted: np.ndarray):
    """ δ3 Threshold Error """

    actual = actual.reshape(-1)
    predicted = predicted.reshape(-1)
    δ3 = 0

    for i in zip(actual, predicted):
        if max((i[0]/i[1]), (i[1]/i[0])) < 1.25*1.25*1.25:
            δ3 += 1

    δ3 = δ3/len(actual)

    return δ3


#....................................................................................................

METRICS = {
    'MSE': mse,
    'RMSE': rmse,
    'RMSE_log': rmse_log,
    'Abs_Rel': abs_relative_error,
    'Square_Rel': rrse,
    'Rel_Abs': rae,
    'δ1': δ1,
    'δ2': δ2,
    'δ3': δ3,
       
}

#.......................................................................................................



def evaluate(actual: np.ndarray, predicted: np.ndarray, metrics=set(METRICS.keys())):
    results = {}
    for name in metrics:
        try:
            results[name] = METRICS[name](actual, predicted)
        except Exception as err:
            results[name] = np.nan
            print('Unable to compute metric {0}: {1}'.format(name, err))
    return results

def readImages(folder_path):
    images = []
    folder_path.sort()
    for i in range(len(folder_path)):
        img = Image.open(folder_path[i])
        images.append(np.array(img))
    
    images = np.array(images)
    return images

def dict_mean(dict_list):
    mean_dict = {}
    for key in dict_list[0].keys():
        mean_dict[key] = sum(d[key] for d in dict_list) / len(dict_list)
    return mean_dict


def calculateMetrics():

    actual = readImages(target_path)
    ic(np.shape(actual))
    predicted = readImages(predicted_path)
    ic(np.shape(predicted))

    start_time = time.time()

    results = []

    for data in zip(actual, predicted):
        results.append(evaluate(data[0], data[1]))
    
    results = dict_mean(results)

    ic(results)


#........................................................................................................................................

if __name__ == "__main__":
    calculateMetrics()

#........................................................................................................................................
from enum import Enum


class ExecPhase(Enum):
    TRAIN = "Train"
    EVAL = "Eval"
    VALID = "Valid"
    TEST = 'Test'
    ANY = 'Any'
    

class ModelType(Enum):
    GENERATOR = "Generator"
    DISCRIMINATOR = "Discriminator"


class EvaluatorType(Enum):
    LOSS = "Loss"
    METRIC = "Metric"


class LossName(Enum):
    TOTAL = "Total"
    ADVERSARIAL = "Adversarial"
    BCE = "BCE"
    L1 = "L1"
    WASSERSTEIN = "Wasserstein"
    GP = "Gradient Penalty"


class MetricsName(Enum):
    PRECISION = "Precision"
    F1 = "F1"
    IOU = "IoU"
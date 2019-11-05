import torch
from torch import nn


def gram_matrix(input: torch.Tensor) -> torch.Tensor:
    a, b, c, d = input.size()  # a=batch size(=1)
    # b=number of feature maps
    # (c,d)=dimensions of a f. map (N=c*d)

    features = input.view(a * b, c * d)  # resise F_XL into \hat F_XL

    G = torch.mm(features, features.t())  # compute the gram product

    # we 'normalize' the values of the gram matrix
    # by dividing by the number of element in each feature maps.
    return G.div(a * b * c * d)


def clean_layer(layer):
    return nn.ReLU(inplace=False) if isinstance(layer, nn.ReLU) else layer


def find_indices(iterable, predicate):
    return [i for i, x in enumerate(iterable) if predicate(x)]


def is_instance_of_any(types):
    return lambda x: any(isinstance(x, t) for t in types)

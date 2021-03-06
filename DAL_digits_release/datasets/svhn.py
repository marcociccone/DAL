from scipy.io import loadmat
import numpy as np
import sys

sys.path.append('./utils/')
from utils.utils import dense_to_one_hot


def load_svhn(base_dir, scale=32):
    svhn_train = loadmat(base_dir + '/svhn_train_{}x{}.mat'.format(scale, scale))
    svhn_test = loadmat(base_dir + '/svhn_test_{}x{}.mat'.format(scale, scale))
    svhn_train_im = svhn_train['X']
    svhn_train_im = svhn_train_im.transpose(3, 2, 0, 1).astype(np.float32)
    svhn_label = dense_to_one_hot(svhn_train['y'])

    # sample train set
    idx = np.random.permutation(svhn_train_im.shape[0])
    svhn_train_im = svhn_train_im[idx]
    svhn_label = svhn_label[idx]
    svhn_train_im = svhn_train_im[:25000]
    svhn_label = svhn_label[:25000]

    svhn_test_im = svhn_test['X']
    svhn_test_im = svhn_test_im.transpose(3, 2, 0, 1).astype(np.float32)
    svhn_label_test = dense_to_one_hot(svhn_test['y'])

    # sample test set
    svhn_test_im = svhn_test_im[:14459]
    svhn_label_test = svhn_label_test[:14459]

    print('svhn train X shape->', svhn_train_im.shape)
    print('svhn train y shape->', svhn_label.shape)
    print('svhn test X shape->', svhn_test_im.shape)
    print('svhn test y shape->', svhn_label_test.shape)
    print("====================")

    return svhn_train_im, svhn_label, svhn_test_im, svhn_label_test

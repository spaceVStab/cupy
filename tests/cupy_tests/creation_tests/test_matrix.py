import unittest

from cupy import testing


@testing.gpu
class TestMatrix(unittest.TestCase):

    @testing.numpy_cupy_array_equal()
    def test_diag1(self, xp):
        a = testing.shaped_arange((3, 3), xp)
        return xp.diag(a)

    @testing.numpy_cupy_array_equal()
    def test_diag2(self, xp):
        a = testing.shaped_arange((3, 3), xp)
        return xp.diag(a, 1)

    @testing.numpy_cupy_array_equal()
    def test_diag3(self, xp):
        a = testing.shaped_arange((3, 3), xp)
        return xp.diag(a, -2)

    @testing.numpy_cupy_array_equal()
    def test_diag_extraction_from_nested_list(self, xp):
        a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        r = xp.diag(a, 1)
        self.assertIsInstance(r, xp.ndarray)
        return r

    @testing.numpy_cupy_array_equal()
    def test_diag_extraction_from_nested_tuple(self, xp):
        a = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
        r = xp.diag(a, -1)
        self.assertIsInstance(r, xp.ndarray)
        return r

    @testing.numpy_cupy_array_equal()
    def test_diag_construction(self, xp):
        a = testing.shaped_arange((3,), xp)
        r = xp.diag(a)
        self.assertIsInstance(r, xp.ndarray)
        return r

    @testing.numpy_cupy_array_equal()
    def test_diag_construction_from_list(self, xp):
        a = [1, 2, 3]
        r = xp.diag(a)
        self.assertIsInstance(r, xp.ndarray)
        return r

    @testing.numpy_cupy_array_equal()
    def test_diag_construction_from_tuple(self, xp):
        a = (1, 2, 3)
        r = xp.diag(a)
        self.assertIsInstance(r, xp.ndarray)
        return r

    @testing.numpy_cupy_raises()
    def test_diag_scaler(self, xp):
        return xp.diag(1)

    @testing.numpy_cupy_raises()
    def test_diag_0dim(self, xp):
        return xp.diag(xp.zeros(()))

    @testing.numpy_cupy_raises()
    def test_diag_3dim(self, xp):
        return xp.diag(xp.zeros((2, 2, 2)))

    @testing.numpy_cupy_array_equal()
    def test_diagflat1(self, xp):
        a = testing.shaped_arange((3, 3), xp)
        return xp.diagflat(a)

    @testing.numpy_cupy_array_equal()
    def test_diagflat2(self, xp):
        a = testing.shaped_arange((3, 3), xp)
        return xp.diagflat(a, 1)

    @testing.numpy_cupy_array_equal()
    def test_diagflat3(self, xp):
        a = testing.shaped_arange((3, 3), xp)
        return xp.diagflat(a, -2)

    @testing.numpy_cupy_array_equal()
    def test_diagflat_from_scalar(self, xp):
        return xp.diagflat(3)

    @testing.numpy_cupy_array_equal()
    def test_diagflat_from_scalar_with_k0(self, xp):
        return xp.diagflat(3, 0)

    @testing.numpy_cupy_array_equal()
    def test_diagflat_from_scalar_with_k1(self, xp):
        return xp.diagflat(3, 1)

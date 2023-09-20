import unittest
import sys

sys.path.insert(1, '../')
from src import biquadratic_oop

import math

biquadratic_oop.Testing = True

class TestOopMethod(unittest.TestCase):

	def testDefault1(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([1, 1, -2])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, {-1, 1})

	# def testDefault2(self):
	# 	self.assertEqual(biquadratic_procedure.solve([1, -3, -4]), {-2, 2})

	# def testDefault3(self):
	# 	self.assertEqual(biquadratic_procedure.solve([9, 8, -1]), {-1/3, 1/3})

	# def testDefault4(self):
	# 	self.assertEqual(biquadratic_procedure.solve([20, -1, -1]), {-1/2, 1/2})

	# def testDefault5(self):
	# 	self.assertEqual(biquadratic_procedure.solve([1, -26, 25]), {-5, -1, 1, 5})

	# def testDefault6(self):
	# 	self.assertEqual(biquadratic_procedure.solve([1, -40, 144]), {-2, 6, 2, -6})

	# def testNoRoots1(self):
	# 	self.assertEqual(biquadratic_procedure.solve([0, 0, -2]), set())

	# def testNoRoots2(self):
	# 	self.assertEqual(biquadratic_procedure.solve([1, 10, 9]), set())

	# def testNoRoots3(self):
	# 	self.assertEqual(biquadratic_procedure.solve([1, 8, 20]), set())

	# def testInfRoots1(self):
	# 	self.assertEqual(biquadratic_procedure.solve([0, 0, 0]), {math.inf})

	# def testFloatInput1(self):
	# 	res = sorted(biquadratic_procedure.solve([2.3, 4.75, 34.2]))
	# 	ans = [-1.7202802072903838, 1.7202802072903838]
	# 	for i in range(len(res)):
	# 		self.assertAlmostEqual(res[i], ans[i], 4)

	# def testFloatInput2(self):
	# 	res = sorted(biquadratic_procedure.solve([1234.5, 1237, -32]))
	# 	ans = [-0.15885084433120192, 0.15885084433120192]
	# 	for i in range(len(res)):
	# 		self.assertAlmostEqual(res[i], ans[i], 4)

	# def testFloatInput3(self):
	# 	res = sorted(biquadratic_procedure.solve([-32, 32, 32]))
	# 	ans = [-1.272019649514069, 1.272019649514069]
	# 	for i in range(len(res)):
	# 		self.assertAlmostEqual(res[i], ans[i], 4)

	# def testHugeNumbers1(self):
	# 	res = sorted(biquadratic_procedure.solve([76865322222243, -22223333232, 321654]))
	# 	ans = sorted([0.01654808161028118, 0.003909143365149529, 
	# 				 -0.003909143365149529, -0.01654808161028118])

	# 	for i in range(len(res)):
	# 		self.assertAlmostEqual(res[i], ans[i], 4)

	# def testHugeNumbers2(self):
	# 	res = sorted(biquadratic_procedure.solve([12345678, -32185436218, 421412344544]))
	# 	ans = sorted([50.929960320420626, 3.6276285909758386, 
	# 				 -3.6276285909758386, -50.929960320420626])

	# 	for i in range(len(res)):
	# 		self.assertAlmostEqual(res[i], ans[i], 4)

	# def testHugeNumbers3(self):
	# 	res = sorted(biquadratic_procedure.solve([123456780987654321, 
	# 											-32185436321218976312312321, 
	# 											 421412344544321321321321]))
	# 	ans = sorted([16146.27057498828, 0.11442579456979729, 
	# 				 -0.11442579456979729, -16146.27057498828])

	# 	for i in range(len(res)):
	# 		self.assertAlmostEqual(res[i], ans[i], 4)



if __name__ == "__main__":
	unittest.main()
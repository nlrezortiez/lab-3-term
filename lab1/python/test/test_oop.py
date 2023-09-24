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

	def testDefault2(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([1, -3, -4])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, {-2, 2})

	def testDefault3(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([9, 8, -1])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, {-1/3, 1/3})

	def testDefault4(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([20, -1, -1])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, {-1/2, 1/2})

	def testDefault5(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([1, -26, 25])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, {5, -5, 1, -1})

	def testDefault6(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([1, -40, 144])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, {-2, 2, -6, 6})

	def testNoRoots1(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([0, 0, -2])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, set())

	def testNoRoots2(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([1, 10, 9])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, set())

	def testNoRoots3(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([1, 8, 20])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, set())

	def testInfRoots1(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([0, 0, 0])
		eq.solve();
		self.assertEqual(eq.solution.solution_set, {math.inf})

	def testFloatInput1(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([2.3, 4.75, 34.2])
		eq.solve();
		res = sorted(eq.solution.solution_set)
		ans = [-1.7202802072903838, 1.7202802072903838]

		for i in range(len(res)):
			self.assertAlmostEqual(res[i], ans[i], 4)

	def testFloatInput2(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([1234.5, 1237, -32])
		eq.solve();
		res = sorted(eq.solution.solution_set)
		ans = [-0.15885084433120192, 0.15885084433120192]
		for i in range(len(res)):
			self.assertAlmostEqual(res[i], ans[i], 4)

	def testFloatInput3(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([-32, 32, 32])
		eq.solve();
		res = sorted(eq.solution.solution_set)
		ans = [-1.272019649514069, 1.272019649514069]
		for i in range(len(res)):
			self.assertAlmostEqual(res[i], ans[i], 4)

	def testHugeNumbers1(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([76865322222243, -22223333232, 321654])
		eq.solve();
		res = sorted(eq.solution.solution_set)
		ans = sorted([0.01654808161028118, 0.003909143365149529, 
					 -0.003909143365149529, -0.01654808161028118])

		for i in range(len(res)):
			self.assertAlmostEqual(res[i], ans[i], 4)

	def testHugeNumbers2(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([12345678, -32185436218, 421412344544])
		eq.solve();
		res = sorted(eq.solution.solution_set)
		ans = sorted([50.929960320420626, 3.6276285909758386, 
					 -3.6276285909758386, -50.929960320420626])

		for i in range(len(res)):
			self.assertAlmostEqual(res[i], ans[i], 4)

	def testHugeNumbers3(self):
		eq = biquadratic_oop.Equation();
		eq.get_coeffs([123456780987654321, 
					  -32185436321218976312312321, 
					   421412344544321321321321])
		eq.solve();
		res = sorted(eq.solution.solution_set)
		ans = sorted([16146.27057498828, 0.11442579456979729, 
					 -0.11442579456979729, -16146.27057498828])

		for i in range(len(res)):
			self.assertAlmostEqual(res[i], ans[i], 4)



if __name__ == "__main__":
	unittest.main()
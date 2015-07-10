import numpy as np
import unittest
import gol_utils
import kata

class TestGoL(unittest.TestCase):
    def setUp(self):
        self.empty = gol_utils.create_world()
        self.empty4x4 = gol_utils.create_world(shape=(4, 4))
        self.corners = gol_utils.create_world(alive=[(0, 0), (0, 2), (2, 0), (2, 2)])
        self.corners4x4 = gol_utils.create_world(shape=(4, 4), alive=[(0, 0), (0, 3), (3, 0), (3, 3)])

    def test_empty(self):
        for x, y in [(i, j) for i in range(3) for j in range(3)]:
            self.assertEqual(0, kata.alive(self.empty, x, y), "alive for {} {} in empty".format(x, y))
            self.assertEqual(0, kata.new_state(self.empty, x, y), "new_state for {} {} in empty".format(x, y))
        new_world = kata.evolve(self.empty)
        np.testing.assert_array_equal(new_world, self.empty)
        for x, y in [(i, j) for i in range(4) for j in range(4)]:
            self.assertEqual(0, kata.alive(self.empty4x4, x, y), "alive for {} {} in empty4x4".format(x, y))
            self.assertEqual(0, kata.new_state(self.empty4x4, x, y), "new_state for {} {} in empty4x4".format(x, y))
        new_world = kata.evolve(self.empty4x4)
        np.testing.assert_array_equal(new_world, self.empty4x4)
            
    def test_single(self):
        center = gol_utils.create_world(alive=[(1, 1)])
        for x, y in [(i, j) for i in range(3) for j in range(3)]:
            if x == 1 and y == 1:
                self.assertEqual(0, kata.alive(center, x, y), "alive for {} {} in center".format(x, y))
            else:
                self.assertEqual(1, kata.alive(center, x, y), "alive for {} {} in center".format(x, y))
            self.assertEqual(0, kata.new_state(center, x, y), "new_state for {} {} in center".format(x, y))
        new_world = kata.evolve(center)
        np.testing.assert_array_equal(new_world, self.empty)
        center4x4 = gol_utils.create_world(shape=(4,4), alive=[(1, 1)])
        for x, y in [(i, j) for i in range(4) for j in range(4)]:
            if x == 1 and y == 1 or x > 2 or y > 2:
                self.assertEqual(0, kata.alive(center4x4, x, y), "alive for {} {} in center4x4".format(x, y))
            else:
                self.assertEqual(1, kata.alive(center4x4, x, y), "alive for {} {} in center4x4".format(x, y))
            self.assertEqual(0, kata.new_state(center4x4, x, y), "new_state for {} {} in center4x4".format(x, y))
        new_world = kata.evolve(center4x4)
        np.testing.assert_array_equal(new_world, self.empty4x4)
                
    def test_filled(self):
        filled = np.ones((3, 3), dtype=int)
        for x, y in [(i, j) for i in range(3) for j in range(3)]:
            if x == 1 and y == 1:
                self.assertEqual(8, kata.alive(filled, x, y), "alive for {} {} in filled".format(x, y))
                self.assertEqual(0, kata.new_state(filled, x, y), "new_state for {} {} in filled".format(x, y))
            elif ((x == 0 or x == 2) and y == 1) or (x == 1 and (y == 0 or y == 2)):
                self.assertEqual(5, kata.alive(filled, x, y), "alive for {} {} in filled".format(x, y))
                self.assertEqual(0, kata.new_state(filled, x, y), "new_state for {} {} in filled".format(x, y))
            else:
                self.assertEqual(3, kata.alive(filled, x, y), "alive for {} {} in filled".format(x, y))
                self.assertEqual(1, kata.new_state(filled, x, y), "new_state for {} {} in filled".format(x, y))
        new_world = kata.evolve(filled)
        np.testing.assert_array_equal(new_world, self.corners)
        filled4x4 = np.ones((4, 4), dtype=int)
        for x, y in [(i, j) for i in range(4) for j in range(4)]:
            if x > 0 and x < 3 and y > 0 and y < 3:
                self.assertEqual(8, kata.alive(filled4x4, x, y), "alive for {} {} in filled4x4".format(x, y))
                self.assertEqual(0, kata.new_state(filled4x4, x, y), "new_state for {} {} in filled4x4".format(x, y))
            elif ((x == 0 or x == 3) and y > 0 and y < 3) or (x > 0 and x < 3 and (y == 0 or y == 3)):
                self.assertEqual(5, kata.alive(filled4x4, x, y), "alive for {} {} in filled4x4".format(x, y))
                self.assertEqual(0, kata.new_state(filled4x4, x, y), "new_state for {} {} in filled4x4".format(x, y))
            else:
                self.assertEqual(3, kata.alive(filled4x4, x, y), "alive for {} {} in filled4x4".format(x, y))
                self.assertEqual(1, kata.new_state(filled4x4, x, y), "new_state for {} {} in filled4x4".format(x, y))
        new_world = kata.evolve(filled4x4)
        np.testing.assert_array_equal(new_world, self.corners4x4)
                
    def test_still(self):
        block = gol_utils.create_world(alive=[(1, 1), (1, 2), (2, 1), (2, 2)])
        for x, y in [(i, j) for i in range(3) for j in range(3)]:
            if x == 0 or y == 0:
                if x == 0 and y == 0 :
                    self.assertEqual(1, kata.alive(block, x, y), "alive for {} {} in block".format(x, y))
                    self.assertEqual(0, kata.new_state(block, x, y), "new_state for {} {} in block".format(x, y))
                else:
                    self.assertEqual(2, kata.alive(block, x, y), "alive for {} {} in block".format(x, y))
                    self.assertEqual(0, kata.new_state(block, x, y), "new_state for {} {} in block".format(x, y))
            else:
                self.assertEqual(3, kata.alive(block, x, y), "alive for {} {} in block".format(x, y))
                self.assertEqual(1, kata.new_state(block, x, y), "new_state for {} {} in block".format(x, y))
        new_world = kata.evolve(block)
        np.testing.assert_array_equal(new_world, block)
        block4x4 = gol_utils.create_world(shape=(4, 4), alive=[(1, 1), (1, 2), (2, 1), (2, 2)])
        for x, y in [(i, j) for i in range(4) for j in range(4)]:
            if x == 0 or x == 3 or y == 0 or y == 3:
                if (x == 0 or x == 3) and (y == 0 or y == 3):
                    self.assertEqual(1, kata.alive(block4x4, x, y), "alive for {} {} in block4x4".format(x, y))
                    self.assertEqual(0, kata.new_state(block4x4, x, y), "new_state for {} {} in block4x4".format(x, y))
                else:
                    self.assertEqual(2, kata.alive(block4x4, x, y), "alive for {} {} in block4x4".format(x, y))
                    self.assertEqual(0, kata.new_state(block4x4, x, y), "new_state for {} {} in block4x4".format(x, y))
            else:
                self.assertEqual(3, kata.alive(block4x4, x, y), "alive for {} {} in block4x4".format(x, y))
                self.assertEqual(1, kata.new_state(block4x4, x, y), "new_state for {} {} in block4x4".format(x, y))
        new_world = kata.evolve(block4x4)
        np.testing.assert_array_equal(new_world, block4x4)
                
        boat = gol_utils.create_world(alive=[(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)])
        for x, y in [(i, j) for i in range(3) for j in range(3)]:
            if x == 1 and y == 1:
                self.assertEqual(5, kata.alive(boat, x, y), "alive for {} {} in boat".format(x, y))
                self.assertEqual(0, kata.new_state(boat, x, y), "new_state for {} {} in boat".format(x, y))
            elif (x == 0 and y == 1) or (x == 1 and y == 0):
                self.assertEqual(3, kata.alive(boat, x, y), "alive for {} {} in boat".format(x, y))
                self.assertEqual(1, kata.new_state(boat, x, y), "new_state for {} {} in boat".format(x, y))
            else:
                self.assertEqual(2, kata.alive(boat, x, y), "alive for {} {} in boat".format(x, y))
                if (x == 0 and y == 0) or x == 1 or y == 1:
                    self.assertEqual(1, kata.new_state(boat, x, y), "new_state for {} {} in boat".format(x, y))
                else:
                    self.assertEqual(0, kata.new_state(boat, x, y), "new_state for {} {} in boat".format(x, y))
        new_world = kata.evolve(boat)
        np.testing.assert_array_equal(new_world, boat)
        boat4x4 = gol_utils.create_world(shape=(4, 4), alive=[(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)])
        for x, y in [(i, j) for i in range(4) for j in range(4)]:
            if x == 1 and y == 1:
                self.assertEqual(5, kata.alive(boat4x4, x, y), "alive for {} {} in boat4x4".format(x, y))
                self.assertEqual(0, kata.new_state(boat4x4, x, y), "new_state for {} {} in boat4x4".format(x, y))
            elif (x == 0 and y == 1) or (x == 1 and y == 0):
                self.assertEqual(3, kata.alive(boat4x4, x, y), "alive for {} {} in boat4x4".format(x, y))
                self.assertEqual(1, kata.new_state(boat4x4, x, y), "new_state for {} {} in boat4x4".format(x, y))
            elif x < 3 and y < 3:
                self.assertEqual(2, kata.alive(boat4x4, x, y), "alive for {} {} in boat4x4".format(x, y))
                if (x == 0 and y == 0) or x == 1 or y == 1:
                    self.assertEqual(1, kata.new_state(boat4x4, x, y), "new_state for {} {} in boat4x4".format(x, y))
                else:
                    self.assertEqual(0, kata.new_state(boat4x4, x, y), "new_state for {} {} in boat4x4".format(x, y))
            elif x == 3 and y == 3:
                self.assertEqual(0, kata.alive(boat4x4, x, y), "alive for {} {} in boat4x4".format(x, y))
                self.assertEqual(0, kata.new_state(boat4x4, x, y), "new_state for {} {} in boat4x4".format(x, y))
            else:
                self.assertEqual(1, kata.alive(boat4x4, x, y), "alive for {} {} in boat4x4".format(x, y))
                self.assertEqual(0, kata.new_state(boat4x4, x, y), "new_state for {} {} in boat4x4".format(x, y))
        new_world = kata.evolve(boat4x4)
        np.testing.assert_array_equal(new_world, boat4x4)
                
    def test_oscillator(self):
        oscillator1 = gol_utils.create_world(alive=[(1, 0), (1, 1), (1, 2)])
        oscillator2 = gol_utils.create_world(alive=[(0, 1), (1, 1), (2, 1)])
        for x, y in [(i, j) for i in range(3) for j in range(3)]:
            if (x == 0 or x == 2):
                if y == 1:
                    self.assertEqual(3, kata.alive(oscillator1, x, y), "alive for {} {} in oscillator1".format(x, y))
                    self.assertEqual(1, kata.new_state(oscillator1, x, y), "new_state for {} {} in oscillator1".format(x, y))
                else:
                    self.assertEqual(2, kata.alive(oscillator1, x, y), "alive for {} {} in oscillator1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator1, x, y), "new_state for {} {} in oscillator1".format(x, y))
            else:
                if y == 1:
                    self.assertEqual(2, kata.alive(oscillator1, x, y), "alive for {} {} in oscillator1".format(x, y))
                    self.assertEqual(1, kata.new_state(oscillator1, x, y), "new_state for {} {} in oscillator1".format(x, y))
                else:
                    self.assertEqual(1, kata.alive(oscillator1, x, y), "alive for {} {} in oscillator1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator1, x, y), "new_state for {} {} in oscillator1".format(x, y))
        new_world = kata.evolve(oscillator1)
        np.testing.assert_array_equal(new_world, oscillator2)
        new_world = kata.evolve(oscillator2)
        np.testing.assert_array_equal(new_world, oscillator1)
        oscillator4x4_1 = gol_utils.create_world(shape=(4, 4), alive=[(1, 0), (1, 1), (1, 2)])
        oscillator4x4_2 = gol_utils.create_world(shape=(4, 4), alive=[(0, 1), (1, 1), (2, 1)])
        for x, y in [(i, j) for i in range(4) for j in range(4)]:
            if (x == 0 or x == 2):
                if y == 1:
                    self.assertEqual(3, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(1, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
                elif y == 3:
                    self.assertEqual(0, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
                else:
                    self.assertEqual(2, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
            elif x == 3:
                if y == 3:
                    self.assertEqual(0, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
                else:
                    self.assertEqual(1, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
            else:
                if y == 1:
                    self.assertEqual(2, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(1, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
                elif y == 3:
                    self.assertEqual(0, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
                else:
                    self.assertEqual(1, kata.alive(oscillator4x4_1, x, y), "alive for {} {} in oscillator4x4_1".format(x, y))
                    self.assertEqual(0, kata.new_state(oscillator4x4_1, x, y), "new_state for {} {} in oscillator4x4_1".format(x, y))
        new_world = kata.evolve(oscillator4x4_1)
        np.testing.assert_array_equal(new_world, oscillator4x4_2)
        new_world = kata.evolve(oscillator4x4_2)
        np.testing.assert_array_equal(new_world, oscillator4x4_1)

if __name__ == "__main__":
    unittest.main()
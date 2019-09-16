import unittest

from matplotlib import pyplot as plt

from atoms.polygon import Polygon
from atoms.regular_polygon import RegularPolygon
from complex_objs.polygonal_prism_net import PolygonalPrismNet

# from utils import FIGURES_DIR


class TestPolygonalNets(unittest.TestCase):
    def test_polygonal_prism_nets(self):

        polygon: Polygon = RegularPolygon(23)
        polygonal_prism_net: PolygonalPrismNet = PolygonalPrismNet(polygon, 10)

        figure, axis = plt.subplots()
        polygonal_prism_net.draw(axis)

        axis.axis("equal")
        figure.show()

        # figure.savefig(os.path.join(FIGURES_DIR, 'heptagonal_prisum_net.png'))

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
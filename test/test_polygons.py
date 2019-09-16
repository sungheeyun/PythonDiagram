import unittest
from typing import Tuple

from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from atoms.polygon import Polygon
from atoms.regular_polygon import RegularPolygon
from atoms.vector2d import Vector2D
from drawing.utils import get_figure


class PolygonsTestCase(unittest.TestCase):
    @staticmethod
    def _get_fig_axis() -> Tuple[Figure, Axes]:
        return plt.subplots()

    @staticmethod
    def _finish_fig(figure: Figure, axis: Axes) -> None:
        axis.axis("equal")
        figure.show()

    def test_pentagon(self):
        figure, axis = PolygonsTestCase._get_fig_axis()
        RegularPolygon(5, (0, 0), 2, 90.0).draw(axis)
        PolygonsTestCase._finish_fig(figure, axis)

        self.assertEqual(True, True)

    def test_get_polygon_from_edges_and_angles(self):
        start_point = (1, 1)
        edge_list = [2, 3, 5]
        angle_list = [45, 60, 60]

        figure, axis = PolygonsTestCase._get_fig_axis()
        Polygon.get_polygon_from_edges_and_angles(start_point, edge_list, angle_list).draw(axis)
        PolygonsTestCase._finish_fig(figure, axis)

        self.assertEqual(True, True)

    def test_get_polygon_from_edges_and_angles_with_starting_vector(self):
        start_point_list: list = list()
        start_vector_list: list = list()
        edge_list_list: list = list()
        angle_list_list: list = list()

        start_point_list.append((1, 1))
        start_vector_list.append((2, 2))
        edge_list_list.append([2, 3])
        angle_list_list.append([45, 120])

        start_point_list.append((1, 1))
        start_vector_list.append((2, 2))
        edge_list_list.append([5, (Vector2D(start_vector_list[-1]) - Vector2D(start_point_list[-1])).norm()])
        angle_list_list.append([90, 90])

        figure = get_figure(len(start_point_list), 1)

        for idx, axis in enumerate(figure.get_axes()):
            Polygon.get_polygon_from_edges_and_angles_with_two_start_points(
                start_point_list[idx], start_vector_list[idx], edge_list_list[idx], angle_list_list[idx]
            ).draw(axis)
            axis.axis("equal")

        figure.show()

        self.assertEqual(True, True)


if __name__ == "__main__":
    unittest.main()
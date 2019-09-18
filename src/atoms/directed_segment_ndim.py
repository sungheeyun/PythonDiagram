from typing import Iterable, Union

from atoms.segment_ndim import SegmentNDim


class DirectedSegmentNDim(SegmentNDim):

    def __init__(
            self,
            start_point: Iterable[Union[float, int]],
            end_point: Iterable[Union[float, int]]
    ):
        super(DirectedSegmentNDim, self).__init__(start_point, end_point)

    def get_name(self) -> str:
        return f'{self.get_num_dimensions()}-D directed line segment'

    def __repr__(self) -> str:
        return f'DiSeg({self.point1}, {self.point2})'

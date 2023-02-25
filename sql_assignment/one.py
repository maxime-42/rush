#!/usr/local/env python3


# @dataclass
# class PeopleCount:
#     """Instances of this class represent a number of people
#     detected by a sensor **since the previous detection**,
#     and their direction. In other words, a list of instances of
#     this class represents a people flow."""
#     sensor: str
#     timestamp: datetime
#     in_count: int
#     out_count: int

# def in_flow(people_counts: List[PeopleCount]) -> int:
#     """Given a list of people counts associated with a single room,
#     calculates the total number of people who entered the room
#     based on all input data. Returns a sum of all in_count values.
#     Input data is limited in size and is guaranteed to fit in memory."""
#     ...

# def test_in_flow():
#     input = [
#         PeopleCount("A", datetime(2021, 5, 1, 10, 0, 0), 21, 4),
#         PeopleCount("A", datetime(2021, 5, 1, 11, 0, 0), 10, 0),
#         PeopleCount("A", datetime(2021, 5, 1, 12, 0, 0), 11, 5),
#     ]
#     output = in_flow(input)
#     expected_output = 42
#     assert expected_output == output

# if __name__ == "__main__":
#     test_in_flow()

from datetime import date, timedelta
from typing import Optional


class Employment:
    def __init__(self, start_date: date, end_date: Optional[date]):
        """

        Parameters
        ----------
        start_date
            The date the employment started.
        end_date
            The date the employment ended (set to None if the employment is still active).
        """
        self.start_date = start_date
        self.end_date = end_date



class EmploymentHistory:
    def __init__(self, employments: list[Employment]):
        self.employments = employments

    @property
    def earliest(self) -> Employment:
        """Returns the employment started the earliest."""
        # should check if sorting by start_date is actually sorting in non-decreasing
        if self.is_empty:
            raise ValueError("We don't have any employment in our history")
        earliest = sorted(self.employments, key=lambda emp: emp.start_date)
        return earliest[0]

    @property
    def current(self) -> list[Employment]:
        """Return a list of ongoing employments."""
        if self.is_empty:
            raise ValueError("We dont't have any employment in our history")
        return [emp for emp in self.employments if emp.end_date == None]
        #return active

    @property
    def is_empty(self) -> bool:
        """Return True if the employment history is empty, False otherwise"""
        return len(self.employments) == 0

    @property
    def total_time_employed(self) -> timedelta:
        """Returns the total amount of time spent employed..
        If working multiple jobs concurrently, they should not be double counted."""
        
        # go through the list of employment, we could sort by start_time
        # if start_time > end_time of next then we should pick either not both employments
        # calculate delta between start_time and end_time and add to our result


        # JOB A: Jan 1st - Jan 5th
        # JOB B: Jan 3rd - Jan 10th
        # JOB C: Jan 4th - Jan 15th

        # res = 15

        # skipping time between Jan3rd to Jan5th under JOB B

        # res = 5 days of JOB A + 5 days of JOB B == 10/11 

        if not self.is_empty:
            if len(self.employments) == 1:
                return self.employments[0].end_date - self.employments[0].start_date
            
            sorted_employments = sorted(self.employments, key=lambda emp: emp.start_date)

            # res = 5
            res = sorted_employments[0].end_date - sorted_employments[0].start_date

            # prev = JOB A 
            prev = sorted_employments[0]

            # employment = JOB B 
            for employment in sorted_employments[1:]:
                # = is really needed ? 
                if employment.start_date >= prev.end_date:
                    res += (employment.end_date - employment.start_date)
                    prev = employment
                # if there is an overlap simply continue
                else:
                    res += employment.end_date - prev.end_date if employment.end_date > prev.end_date else timedelta(days=0)
                    prev = employment if employment.end_date > prev.end_date else prev
            return res

        return 0 # check what should be returned here in this case?





# A quick summary of the behaviour of timedelta:
# d1 = date(2021, 4, 23)
# d2 = date(2023, 5, 21)
# 
# td1 = d2-d1
# td2 = td1 + timedelta(days=5)
# assert td1 == timedelta(days=758)
# assert td2 == timedelta(days=763)

# January 1st-30th 
emp1 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 20))
emp2 = Employment(start_date=date(2020, 1, 20),end_date=date(2020, 1, 30))

january_no_overlap_employment_hist = EmploymentHistory([emp1, emp2])


print("Total time employed for january_no_overlap_employment_hist is: ", january_no_overlap_employment_hist.total_time_employed)

# January 1st-10th 20th-30th (testing for gaps)
emp1 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 10))
emp2 = Employment(start_date=date(2020, 1, 20),end_date=date(2020, 1, 30))

january_gap_employment_hist = EmploymentHistory([emp1, emp2])

print("Total time employed for january_gap_employment_hist is: ", january_gap_employment_hist.total_time_employed)

# January 1st-10th 20th-30th 1st-30th (testing for gaps & overlap)
emp1 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 10))
emp2 = Employment(start_date=date(2020, 1, 20),end_date=date(2020, 1, 30))
emp3 = Employment(start_date=date(2020, 1, 1),end_date=date(2020, 1, 30))

january_gap_and_overlap_employment_hist = EmploymentHistory([emp1, emp2, emp3])

print("Total time employed for january_gap_and_overlap_employment_hist is: ", january_gap_and_overlap_employment_hist.total_time_employed)

# Dense overlapping (answer should be 365 days for total_time_employed)
employments = [
    Employment(start_date=date(2020, 1, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 7, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 8, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 9, 1), end_date=date(2020, 12, 31)),
    Employment(start_date=date(2020, 10, 1), end_date=date(2020, 12, 31)),
]

densely_overlapping_employment_hist = EmploymentHistory(employments=employments)


print("Total time employed for densely_overlapping_employment_hist is: ", densely_overlapping_employment_hist.total_time_employed)


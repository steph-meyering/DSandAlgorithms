class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan": "1",
                  "Feb": "2",
                  "Mar": "3",
                  "Apr": "4",
                  "May": "5",
                  "Jun": "6",
                  "Jul": "7",
                  "Aug": "8",
                  "Sep": "9",
                  "Oct": "10",
                  "Nov": "11",
                  "Dec": "12"}
        d, m, y = date.split(" ")
        d = re.sub("\D", "", d)
        m = months[m]
        if len(d) == 1:
            d = f"0{d}"
        if len(m) == 1:
            m = f"0{m}"
        return f"{y}-{m}-{d}"

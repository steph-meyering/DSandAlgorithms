# @param {Integer[][]} points
# @return {Integer}
def min_time_to_visit_all_points(points)
    res = 0
    (0...points.length-1).each do |i|
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        res += [(x1-x2).abs, (y1-y2).abs].max
    end
    res
end
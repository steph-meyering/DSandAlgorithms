# 690. Employee Importance

=begin
# Definition for Employee.
class Employee
    attr_accessor :id, :importance, :subordinates
    def initialize( id, importance, subordinates)
        @id = id
        @importance = importance
        @subordinates = subordinates
    end
end
=end

# @param {Employee} employees
# @param {Integer} id
# @return {Integer}

def get_importance(employees, id)
    $hash = {}
    employees.each do |employee|
        $hash[employee.id] = employee
    end
    target = $hash[id]
    sub_importance = sub_sum(target.subordinates) || 0
    total_importance = target.importance + sub_importance
    return total_importance
end

def sub_sum(employees_arr)
    return 0 if employees_arr.empty?
    sum = 0
    employees_arr.each do |id|
        employee = $hash[id]
        sum += employee.importance + sub_sum(employee.subordinates)
    end
    return sum
end
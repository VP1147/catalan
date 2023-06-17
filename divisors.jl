
function s(x)
    l = []
    for i in 1:x
        if x % i == 0
            push!(l, i)
            #println(i, " is a divisor of ", x)
        end
    end
    return sum(l)
end

function iter(x)
    println("n = ", x)
    i = 1
    while x != 0
        x = s(x)
        println(x)
        if x == s(x)
			return x
        end
        i += 1
    end
end

iter(276)
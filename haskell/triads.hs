-- get a list of divisors of x
divisors :: Int -> [Int]
divisors x = [d | d <- [2..x-1], x `mod` d == 0]

-- check if x and y have coprime
coprime :: Int -> Int -> Bool
coprime x y = disjoint (divisors x) (divisors y)

-- check if xs and ys have common elements
disjoint :: [Int] -> [Int] -> Bool
disjoint xs ys = if      length xs == 0 then True
                 else if elem (xs!!0) ys then False
                 else    disjoint ys $ tail xs

-- output all Pythagorean triads less than n
triads :: Int -> [(Int,Int,Int)]
triads n = [(x,y,z) | x <- [1..n], y <- [x+1..n], z <- [y+1..n], coprime x y, x*x + y*y == z*z]


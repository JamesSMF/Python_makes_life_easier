chain :: (Integral a) => a -> [a]  
chain 1 = [1]
chain n
   | even n = n:chain (n `div` 2)
   | odd  n = n:chain (3 * n + 1)

longerThanFifteen :: Int
longerThanFifteen = length (filter (isLonger) (map chain [1..100]))
                  where isLonger xs = length xs > 15

-- or
-- longerThanFifteen = length (filter (\xs -> length xs > 15) (map chain [1..100]))
